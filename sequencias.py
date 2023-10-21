def fib(n):
    seq_fib = [1,1]
    if n > 2:
        for i in range(n-2):
            seq_fib.append(seq_fib[len(seq_fib) - 2 ] + seq_fib[len(seq_fib) - 1])
        return seq_fib
    if n <= 2 : return seq_fib
def pell(n):
    pell = [0,1]
    for i in range (2,n):
        pell.append((2*(pell[i-1]) + pell[i-2]))
    return pell
def mmc(a,b):
    return (a*b) / mdc(a,b)
    
def mdc(a,b):
    maior, menor = max(a,b), min(a,b)
    count = 1
    while maior % menor:
        count +=1
        aux = maior % menor
        maior = menor
        menor = aux
    return menor, count

def div(fib):
    quocientes_abaixo = []
    restos = []
    for i in range(1,len(fib)):
        quocientes_abaixo.append(fib[i] / fib[i-1])
        restos.append(fib[i] % fib[i-1])
    return quocientes_abaixo, restos
q,r = div(fib(10))
#print(f"Sequência = {fib(10)}\nQuocientes= {q}\nRestos= {r}")
#print(mdc(fib(10)[4-2],fib(10)[4-1]))
print(mdc(pell(20)[9-2],pell(20)[9-1]))

#print(55%34, 34%55) # 2 

print(pell(5))