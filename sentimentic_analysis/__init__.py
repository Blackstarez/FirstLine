from . import bert_model
import torch
from kobert.pytorch_kobert import get_pytorch_kobert_model

bertmodel1, vocab1 = get_pytorch_kobert_model()
bertmodel2, vocab2 = get_pytorch_kobert_model()
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab1, lower=False)
max_len = 64
batch_size = 64

global model1 = BERTClassifier(bertmodel1, num_classes=3, dr_rate=0.5).to(device)
model1.load_state_dict(torch.load("saved_P_UP_NU_ep_20.pt")) ## P_UP_NU

global model2 = BERTClassifier(bertmodel2, dr_rate=0.5).to(device)
model2.load_state_dict(torch.load("saved_P_NU_ep_20.pt")) ## P_NU

model1.eval()
model2.eval()

