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
