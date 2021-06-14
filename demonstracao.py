# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:05:50 2018

@author: Victor Melly
"""

Px = [5,7,1,3]
Qx = [-1,-2,1,0,3]
x = 2

def imprime_polinomio(polinomio):
    expoente = len(polinomio)-1

    if polinomio[0] == 1:
        print("x^%d" %expoente, end=' ')

    elif polinomio[0] == -1:
        print("-x^%d" %expoente, end=' ')
        
    else:
        print("%dx^%d" %(polinomio[0], expoente), end=' ')    
    expoente -= 1
    
    for i in range(1, len(polinomio)):
        if polinomio[i] == 0:
            i += 1
            
        elif polinomio[i] > 1:
            if expoente > 1:
                print("+ %dx^%d" %(polinomio[i], expoente), end=' ')
            elif expoente == 1:
                print("+ %dx" %polinomio[i], end=' ')
            else:
                print("+ %d" %polinomio[i], end=' ')
                
        elif polinomio[i] < -1:
            if expoente > 1:
                print("%dx^%d" %(polinomio[i], expoente), end=' ')
            elif expoente == 1:
                print("%dx" %polinomio[i], end=' ')
            else:
                print(polinomio[i], end=' ')
                
        elif polinomio[i] == 1:
            if expoente > 1:
                print("+ x^%d" %expoente, end=' ')
            elif expoente == 1:
                print("+ x", end=' ')
            else:
                print(polinomio[i], end=' ')
                
        elif polinomio[i] == -1:
            if expoente > 1:
                print("-x^%d" %expoente, end=' ')
            elif expoente == 1:
                print("-x", end=' ')
            else:
                print(polinomio[i], end=' ')
        expoente -= 1

        
def calcula_polinomio(polinomio, x):
    calculo = 0
    expoente = len(polinomio)-1
    
    for i in range(expoente):     
        calculo += x**expoente * polinomio[i]
        expoente -= 1
        
    return calculo


    
def soma_polinomios(polinomio_p, polinomio_q):
    if len(polinomio_p) > len(polinomio_q):
        maior = polinomio_p
        menor = polinomio_q
    else:
        maior = polinomio_q
        menor = polinomio_p
        
    soma_p_q = [0]*len(maior)
    i = len(maior) -1
    k = len(menor) -1
      
    while k >= 0:
        soma_p_q[i] = maior[i] + menor[k]
        i -= 1
        k -= 1

    while i >= 0:
        soma_p_q[i] = maior[i]
        i -= 1
        
    return soma_p_q


def multiplica_polinomios(polinomio_p, polinomio_q):
    produto_p_q = [0]*(len(polinomio_p) + len(polinomio_q)-1)
    
    for i in range(len(polinomio_p)):
        for k in range(len(polinomio_q)):
            produto_p_q[i+k] += polinomio_p[i] * polinomio_q[k]
        
    return produto_p_q


def main():

    print("P(x) =", end=" ")
    imprime_polinomio(Px)
    print("\n")
    print("Q(x) =", end=" ")
    imprime_polinomio(Qx)
    print("\n")
    
    print("Cálculo do polinômio P com x valendo %d é:" %x, calcula_polinomio(Px, x), '\n')
    print("Cálculo do polinômio Q com x valendo %d é:" %x, calcula_polinomio(Qx, x), '\n')

    print("P(x) + Q(x) =", end=" ")
    imprime_polinomio(soma_polinomios(Px, Qx))
    print('\n')

    print("P(x) * Q(x) =", end=" ")
    imprime_polinomio(multiplica_polinomios(Px, Qx))
    
main()
