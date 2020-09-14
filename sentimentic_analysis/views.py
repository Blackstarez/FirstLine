from django.shortcuts import render
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(post))))
from .model import Post




# Create your views here.
def sentimenticAnalysis(postNum):
    try:
        post = Post.object.get(id=postNum)
        sentences = post['content'].value()
        sentences = sentences.split('\n')

        sentiments_P_UP_NU = ['Unpleasure', 'pleasure', 'Neutrality']
        sentiments_P_NU = ['Pleasure', 'Neutrality']

        for sentence in sentences:
            sent_data = [[sentence, '1']]

            sent_dataset =BERTDataset(sent_data, 0, 1, tok, max_len, True, False)
            sent_dataloader = torch.utils.data.DataLoader(sent_dataset, batch_size=1, num_workers=0)

            for idx, (token_ids, valid_length, segment_ids, label) in enumerate(sent_dataloader):
                token_ids = token_ids.long().to(device)
                segment_ids = segment_ids.long().to(device)
                valid_length= valid_length
                
                out1 = model1(token_ids, valid_length, segment_ids)
                out2 = model2(token_ids, valid_length, segment_ids)

                sm1 = torch.nn.Softmax()
                probabilities1 = sm1(out1)

                sm2 = torch.nn.Softmax()
                probabilities2 = sm2(out2)

                prob1_list = max(probabilities1.cpu().detach().tolist())
                prob1_index = prob1_list.index(max(prob1_list))
                tag = sentiments_P_UP_NU[prob1_index]
                if(prob1_index):
                    #긍정 or 중성이 부정보다 높은경우
                    prob2_list = max(probabilities2.cpu().detach().tolist())
                    prob2_index = prob2_list.index(max(prob2_list))
                    tag = sentiments_P_NU[prob2_index]
                    newPost = Post(id = )
                else:
                    #그렇지 아니한 경우


                result.append([sentence, tag])
    except :
        pass
    