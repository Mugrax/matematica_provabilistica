'''
Em estudos realizados biológico, foi constatado que o número de indivíduos de
certa espécie (N) está crescendo em função do tempo t (dado em anos) ,
segundo a expressão:

N(t)=4/2+3*2**(t)

a) Qual o domínio da função?
b) Obter o gráfico da função.
c) A função é crescente ou decrescente?
d) Qual o conjunto imagem da função?

'''
from matplotlib import pyplot as plt
import numpy as np



# a)o domínio é (t)

# b)-----------------------------------------


def f(t):
    return 4/2+3*2**(t)

t=np.arange(1,10)

x = f(t)

plt.plot(t,x,color='green')
    
plt.show()

# -------------------------------------------
# c) Crescente

# d) a imagen é X

print(x)