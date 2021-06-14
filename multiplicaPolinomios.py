def multiplica_polinomios(polinomio_p, polinomio_q):
    produto_p_q = [0]*(len(polinomio_p) + len(polinomio_q)-1)
    
    for i in range(len(polinomio_p)):
        for k in range(len(polinomio_q)):
            produto_p_q[i+k] += polinomio_p[i] * polinomio_q[k]
        
    return produto_p_q
