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
