
# coding: utf-8

# In[19]:

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
andarFinal = []


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

    #if i == 223:         #alterar número para comparar se está certo
     #   print(lista)
        
    i += 1
    matriz.append(copy.deepcopy(lista))
    andarFinal.append(andar)


# In[47]:

# Get matplotlib graphics to show up inline.
get_ipython().magic('matplotlib inline')

plt.rcParams['figure.figsize'] = (20, 6)

import matplotlib.pyplot as plt

rodada = andarFinal

# With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot.
plt.plot(rodada)

# labels
xlab = 'Rodadas'
ylab = 'Andar final'
title = 'Joguinho Python'

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.yticks([0,25,50,75,100,125,150])


get_ipython().magic('time plt.show()')

