'''
#импортируем ИИ, который будет чистить текст. (да, использовать ИИ, чтобы подготовить данные, чтобы потом тренировать ИИ)
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer 
 
path_to_model = "ai-forever/RuM2M100-1.2B" 
 
model = M2M100ForConditionalGeneration.from_pretrained(path_to_model) 
tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")


#проверяем, что всё работает
sentence = "я пришол в тгу и недумал что буду ченит компьютер, сламавшейся вчира вечером" 
 
encodings = tokenizer(sentence, return_tensors="pt") 
generated_tokens = model.generate( 
        **encodings, forced_bos_token_id=tokenizer.get_lang_id("ru")) 
answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True) 
print(answer)

#  Нам нужно считать наш датасет,
#  добавть туда разделители в тексты,
#  слепить тексты в один,
#  дать нейронке на обработку,
#  разделить полученные куски на фрагменты
#  записать всё в датасет в новую колонку

'''




import numpy as np
import pandas as pd
import re
import nltk
import string

#  читаем наш датасетик
path_to_dataset = "/home/fblthp/PYNLP/NLP/AI/reviews.csv"
df = pd.read_csv(path_to_dataset, encoding='UTF8', sep="\t")

#  читаем ревьюшки, склеиваем их в одну строку с сепаратором konetsblin,
#  чтобы наша нейроночка исправила ошибки в текстах за 1 прогон.
reviews = df["review"][:10]
c_revs = " konetsblin ".join(reviews)
print("*****C REVS*****")
print(c_revs)
c_revs.strip()


#теперь исправляем текст с помощью нейроночки


#импортируем ИИ, который будет чистить текст. (да, использовать ИИ, чтобы подготовить данные, чтобы потом тренировать ИИ)
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer 
 
path_to_model = "ai-forever/RuM2M100-1.2B" 
 
model = M2M100ForConditionalGeneration.from_pretrained(path_to_model) 
tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")



 
encodings = tokenizer(c_revs, return_tensors="pt") 
generated_tokens = model.generate( 
        **encodings, forced_bos_token_id=tokenizer.get_lang_id("ru")) 
answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True) 
print("*****ANSWER*****")
print(len(answer))
print(answer)


#сплитуем исправленный текст и записываем в файл проверки
resul = list()

for i in answer:
    i = i.strip()
    i = i + "\n"
    resul.extend(i.split('konetsblin'))

#print("            *********************   ")
    

print("*****RESUL*****")
print(resul[0])
print(resul[1])

proverka = open("/home/fblthp/PYNLP/NLP/AI/proverka.txt", "w")
proverka.writelines(resul)
proverka.close()
