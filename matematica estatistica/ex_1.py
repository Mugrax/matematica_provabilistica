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



# a)D={D E N} / representado na equaçao como 0<t<10 

# b)-----------------------------------------


def f(t):
    return 4/2+3*2**(t)

t=np.arange(0,10)

x = f(t)

plt.plot(t,x,color='green')
plt.xlabel('Tempo/anos')
plt.ylabel('Crescimento')
plt.grid(True)
plt.show()

# -------------------------------------------
# c) Crescente

# d)I={I E N| 5<I<1538}

print(f'D={t}\n\nI={x}')