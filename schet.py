import re

def num_to_text(x):
    cifri = ["","один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
    dcat = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    desatki = ["дцать","десят"]

    if re.search("[^0-9]", x) is not None: print("Я ЖДАЛ ЦИФРУ ИЛИ ДВУЗНАЧНОЕ ЧИСЛО, БЕЗ ВСЯКИХ СИМВОЛОВ И ПРОБЕЛОВ И ВАЩЕ Я ОБИДЕЛСЯ");return

    i = int(x)
    x = str(i)

    if len(x)>2 or x=="": print("НУЖНО ЧИСЛО ОТ 0 ДО 99 И ТОЧКА (НУ ВСМЫСЛЕ ТОЧКУ НЕ НАДО, НАДО ДВУЗНАЧНОЕ НАТУРАЛЬНОЕ ЧИСЛО)")
    if i==0: print("ноль")
    elif len(x)==2:
        match x[0]:
            case "1":
                print(dcat[i%10])
            case "4":
                print("сорок " +cifri[i%10])
            case "9":
                print("девяносто " +cifri[i%10])
            case _ :
                if i>=50:
                    print(cifri[i//10]+desatki[1]+ " " +cifri[i%10])
                else:
                    print(cifri[i//10]+desatki[0]+ " " +cifri[i%10])
    else: print(cifri[i])

num_to_text(input())

'''
for k in range(0,100):
    num_to_text(str(k))
'''

'''
for i in range(0,100):
    x = str(i)
    if i==0: print("ноль")
    elif len(x)==2:
        match x[0]:
            case "1":
                print(dcat[i%10])
            case "4":
                print("сорок " +cifri[i%10])
            case "9":
                print("девяносто " +cifri[i%10])
            case _ :
                if i>=50:
                    print(cifri[i//10]+desatki[3]+ " " +cifri[i%10])
                else:
                    print(cifri[i//10]+desatki[2]+ " " +cifri[i%10])
    else: print(cifri[i])
'''  

'''
for x in range(20,40):
    print(cifri[x//10]+desatki[2]+ " " +cifri[x%10])
for x in range(40,50):
    print("сорок " +cifri[x%10])
for x in range(50,90):
    print(cifri[x//10]+desatki[3]+ " " +cifri[x%10])
for x in range(90,100):
    print("девяносто " +cifri[x%10])
'''
