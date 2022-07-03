'''
Em uma cerimônia de colação de grau de certa universidade, 30 mulheres e
20 homens receberam seus diplomas de concluintes em curso de nível
superior. Entre as mulheres, formaram-se 10 arquitetas, 14 médicas e 6
engenheiras. Entre os homens, formaram-se 2 arquitetos, 10 médicos e 8
engenheiros. Durante essa cerimônia, um dos formandos foi escolhido ao
acaso para fazer o juramento em nome de todos. Sabendo que o formando
sorteado foi uma mulher, qual é a probabilidade de que ela seja uma médica
formada?

'''

# discionario dos formados ---------------------------------
sx = ['homen','mulher']
formacao = ['arquiteto','medico','engenheiro']
formados=[]

for i in range(2):
    if sx[i] == 'homen':
        for j in range(3):
            if formacao[j]=='arquiteto':
                for k in range(2):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]
            elif formacao[j]=='medico':
                for k in range(10):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]
            else:
                for k in range(8):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]
    elif sx[i] == 'mulher':
        for j in range(3):
            if formacao[j]=='arquiteto':
                for k in range(10):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]
            elif formacao[j]=='medico':
                for k in range(14):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]
            else:
                for k in range(6):
                    formado={'sexo':None,'formação':None}
                    formado['sexo'] = sx[i]
                    formado['formação'] = formacao[j]
                    formados+=[formado]

# ----------------------------------------------------------

# fazendo os conjuntos com base no indice do discionario --- 0 a 49

mulheres=set()
medicos=set()

for indice,i in enumerate(formados):
    if i['sexo'] == 'mulher':
        mulheres.add(indice)
    if i['formação'] == 'medico':
        medicos.add(indice)

# ----------------------------------------------------------

# calculando a provabilidade -------------------------------

medicas=mulheres & medicos

quantidade_medicas=len(medicas)
quantidade_de_mulheres=len(mulheres)
quantidade_medicos=len(medicos)

provabilidade=quantidade_medicas/quantidade_de_mulheres
provabilidade_por100=provabilidade*100

# caso queira ter uma busca precisa de algumas informaçoes, usar o metodo com indices ajuda a localizar algo de forma precisa caso o discionario tenha mais informações
print(f'\nconjunto das mulheres com {quantidade_de_mulheres} mulheres e seus indices no discionario:\n\n{mulheres}')
print(f'\nconjunto de medicos/as com {quantidade_medicos} medicos/as e seus indices no discionario:\n\n{medicos}')
print(f'\nconjunto de medicas com {quantidade_medicas} medicas e seus indices no discionario:\n\n{medicas}')
print(f'\na provabilidade de a escolhida ser medica é de 14/30 ou {round(provabilidade,2)} ou {round(provabilidade_por100,2)}%\n')
