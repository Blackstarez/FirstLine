import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
from transformers import AdamW
from transformers.optimization import WarmupLinearSchedule

class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i],))

    def __len__(self):
        return (len(self.labels))

class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size=768,
                 num_classes=2,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
        self.dr_rate = dr_rate

        self.classifier = nn.Sequential(
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )
        
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)

    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)

        _, pooler = self.bert(input_ids=token_ids, token_type_ids=segment_ids.long(),
                              attention_mask=attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)


class SentimentAnalyszer:
   __instance = None
   model1 = None
   model2 = None
   max_len = 64
   batch_size = 64
   tok = None
   @staticmethod
   def get_instance():
      if SentimentAnalyszer.__instance == None:
        SentimentAnalyszer()
      return SentimentAnalyszer.__instance
   def __init__(self):
        if SentimentAnalyszer.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            try:
                SentimentAnalyszer.__instance = self
                bertmodel1, vocab1 = get_pytorch_kobert_model()
                bertmodel2, vocab2 = get_pytorch_kobert_model()
                tokenizer = get_tokenizer()
                self.tok = nlp.data.BERTSPTokenizer(tokenizer, vocab1, lower=False)
                self.model1 = BERTClassifier(bertmodel1, num_classes=3, dr_rate=0.5).to('cpu')
                self.model1.load_state_dict(torch.load("./bert_model/saved_P_DP_NU_ep_16.pt",  map_location=torch.device('cpu'))) ## P_UP_NU
                self.model2 = BERTClassifier(bertmodel2, num_classes=2, dr_rate=0.5).to('cpu')
                self.model2.load_state_dict(torch.load("./bert_model/saved_P_NU_ep_18.pt",  map_location=torch.device('cpu'))) ## P_NU
                self.model1.eval()
                self.model2.eval()
                print("1")
            except Exception as ex:
                print(ex)
            
   def get_analysis_result(self,post_content):
        postSementic=[0,0,0]
        sentences = post_content.split('\n')
        for sentence in sentences:
            sent_data = [[sentence, '1']]
            sent_dataset =BERTDataset(sent_data, 0, 1, self.tok, self.max_len, True, False)
            sent_dataloader = torch.utils.data.DataLoader(sent_dataset, batch_size=1, num_workers=0)

            for idx, (token_ids, valid_length, segment_ids, label) in enumerate(sent_dataloader):
                token_ids = token_ids.long().to('cpu')
                segment_ids = segment_ids.long().to('cpu')
                valid_length= valid_length
                
                out1 = self.model1(token_ids, valid_length, segment_ids)
                out2 = self.model2(token_ids, valid_length, segment_ids)

                sm1 = torch.nn.Softmax()
                probabilities1 = sm1(out1)

                sm2 = torch.nn.Softmax()
                probabilities2 = sm2(out2)

                prob1_list = max(probabilities1.cpu().detach().tolist())
                prob1_index = prob1_list.index(max(prob1_list))
                postSementic[0] += prob1_list[0]
                if(prob1_index):
                    #긍정 or 중성이 부정보다 높은경우
                    prob2_list = max(probabilities2.cpu().detach().tolist())
                    prob2_index = prob2_list.index(max(prob2_list))
                    postSementic[1] += (1 - prob1_list[0])*prob2_list[1] #긍정
                    postSementic[2] += (1 - prob1_list[0])*prob2_list[0] #중성
                else:
                    #그렇지 아니한 경우
                    postSementic[1] += prob1_list[1]
                    postSementic[2] += prob1_list[2]
        temperature= ((-8.5*postSementic[0]/len(sentences))+36.5+((5.5*postSementic[1])/len(sentences)))
        prob_n= postSementic[2]/len(sentences)
        prob_p= postSementic[1]/len(sentences)
        prob_dp= postSementic[0]/len(sentences)
        return prob_n, prob_p, prob_dp, temperature


