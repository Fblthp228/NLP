#  Нам нужно считать наш датасет
#  дать нейронке на исправление ошибок
#  записать всё в датасет в новую колонку

import numpy as np
import pandas as pd
import re
import nltk
import string

#перед предобработкой удалим из датасета пустые колонки (см файл удаления)
#  читаем наш датасетик с уже удалёнными пустыми отзывами и очищенный от эмодзи, ссылок
path_to_dataset = "/home/fblthp/PYNLP/NLP/AI/ommited.csv"
df = pd.read_csv(path_to_dataset, encoding='UTF8', sep="\t")
print("the data has been read")



#сделаем предобработку от beginning и до конца
#reviews = df["review"][beginning:]
#reviews = df["review"]


##### ОЧИСТКА ДАННЫХ С ПОМОЩЬЮ ИИ ##### (оно работает, но ОООоочень долго. Будет обрабатывать 11 дней весь датасет. только этот этап)

#в отдельном файле будем хранить переменную, которая будет говорить нам сколько отзывов было уже предобработано
progress_file = open("/home/fblthp/PYNLP/NLP/AI/progress_file.txt", "r")
beginning = int(progress_file.readline())
progress_file.close()

print("importing AI")
#импортируем ИИ, который будет чистить текст. (да, использовать ИИ, чтобы подготовить данные, чтобы потом тренировать ИИ)
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer 
 
path_to_model = "ai-forever/RuM2M100-1.2B" 
 
model = M2M100ForConditionalGeneration.from_pretrained(path_to_model) 
tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")


'''
print("wiping the previous data")
proverka = open("/home/fblthp/PYNLP/NLP/AI/proverka.txt", "w")
proverka.write(" ")
proverka.close()
'''


print("correcting reviews using AI")

proverka = open("/home/fblthp/PYNLP/NLP/AI/proverka.txt", "a")


#aifix_revs = list()

for i in range(beginning,len(df["review"])): #сделаем предобработку от beginning и до конца
    current = df["review"][i]
    #i.strip()
    current = re.sub(r"[\n\t]*", " ", current)
    encodings = tokenizer(current, return_tensors="pt") 
    generated_tokens = model.generate( **encodings, forced_bos_token_id=tokenizer.get_lang_id("ru")) 
    answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True) 
    #print(answer)
    #aifix_revs.extend(answer)
    proverka.write(answer[0] + "\n")
    beginning += 1
    progress_file = open("/home/fblthp/PYNLP/NLP/AI/progress_file.txt", "w")
    progress_file.write(str(beginning))
    progress_file.close()
    print(beginning)

proverka.close()


#proverka = open("/home/fblthp/PYNLP/NLP/AI/proverka.txt", "w")
#proverka.writelines(aifix_revs)
#proverka.close()

##### ЛЕММАТИЗАЦИЯ #####