
# coding: utf-8

# In[ ]:

import random
import copy
import numpy as np

def descerAndar(andar):
    if andar == 0:
        return 0
    else:
        andar -= 1
        return andar

def dadoSeis(andar):
    andar += random.randint(1,6)
    return andar


andar = 0
dado = 0
chanceCair = 0.0
lista = []
matriz = []

for i in range(500):
    andar = 0
    lista.clear()

    for j in range(100):
        j += 1
        dado = random.randint(1,6)

        if dado == 1 or dado == 2:
            andar = descerAndar(andar)

        elif dado in range(3,6):
            andar += 1

        elif dado == 6:
            andar = dadoSeis(andar)
            
        chanceCair = np.random.random(1)[0]
        
        if chanceCair <= 0.01:
            andar = 0

        lista.append(andar)

    if i == 223:         #alterar número para comparar se está certo
        print(lista)
        
    
    i += 1
    matriz.append(copy.deepcopy(lista))


# In[ ]:

repetir = True

while(repetir):
    resposta = input("Selecionar interação (0 a 499): ")
    print("\n")
    intRes = int(resposta)
    
    if intRes >= 0 and intRes <= 499:
        print(matriz[intRes])
        repetir = False
    else:
        print("Interação inexistente, selecione um valor de 0 a 499.")


# In[ ]:



