def calcula_polinomio(polinomio, x):
    calculo = 0
    expoente = len(polinomio)-1
    
    for i in range(expoente):     
        calculo += x**expoente * polinomio[i]
        expoente -= 1
        
    return calculo
