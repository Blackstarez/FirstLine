<<<<<<< HEAD


from . import bert_model
import torch
from kobert.pytorch_kobert import get_pytorch_kobert_model

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


bertmodel1, vocab1 = get_pytorch_kobert_model()
bertmodel2, vocab2 = get_pytorch_kobert_model()
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab1, lower=False)
max_len = 64
batch_size = 64

global model1 = BERTClassifier(bertmodel1, num_classes=3, dr_rate=0.5).to(device)
model1.load_state_dict(torch.load("bert_model/saved_P_UP_NU_ep_20.pt")) ## P_UP_NU

global model2 = BERTClassifier(bertmodel2, dr_rate=0.5).to(device)
model2.load_state_dict(torch.load("bert_model/saved_P_NU_ep_20.pt")) ## P_NU

model1.eval()
model2.eval()

=======
>>>>>>> 7c2286ac2c86279da5ae8777aa1dcbc70a49610d
