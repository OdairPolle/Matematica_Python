# -*- coding: utf-8 -*-
"""Aula_15_LPDA_SENAI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18ApyXViZEizF6o39H5iBDuaLENgfz2mL

#Matriz Inversa
"""

import numpy as np

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

invA=np.linalg.inv(A)
print('A inversa da matriz A é: ', invA)

"""#Fatores Primos"""

def fatora_primo():

    n = int(input("Digite um numero positivo e inteiro: "))

    fator = 2 # primeiro primo
    while n != 1:
        # Contador para verificar a quantidade de vezes que o fator foi utilizado
        mult = 0;
        while n%fator == 0:
            n = n / fator;
            mult = mult + 1;

        # imprime a quantidade de vezes que o fator foi utilizado
        if mult != 0:
            print("%d elevado à %d" %(fator, mult))

        fator = fator + 1


fatora_primo()

"""#Autovalores e Autovetores"""

import numpy as np

a = np.array([[0, 2],
              [2, 3]])
w,v=np.linalg.eig(a)
print('E-value:', w)
print('E-vector', v)

import numpy as np
aa=np.random.randint(5, size=(2, 4))
print(aa)

