from random import randint

def sortieren(Liste):
    
    
    Outtput = []
    index= -1

    
    while len(Liste) > 0:
        min = float("inf")
        for i in range(len(Liste)):
            if Liste[i] < min:#neues minimum gefunden
                min = Liste[i]
                index = i#index des minimums
        Outtput.append(min)
        Liste.pop(index)
    print(Outtput)

L=[]
for b in range(10):
    L.append(randint(-100,100))
sortieren(L)