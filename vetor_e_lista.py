Lista_vazia = []

Lista_inteiros = [2, 4, 6, 8, 10]

Lista_reais = [9.0, 10.0, 8.5, 7.8]

Lista_frutas = ["abacaxi", "pera", "uva", "abacate"]

Lista_zerada = [0]*5

Lista_strings = [""]*4

print(Lista_vazia)
print(Lista_inteiros)
print(Lista_reais)
print(Lista_frutas)
print(Lista_zerada)
print(Lista_strings)

comprimento = len(Lista_inteiros)
print (comprimento)

#primeiro elemento da lista
print(Lista_inteiros[0])
print(Lista_frutas[0])

#primeiro elemento da lista
print(Lista_inteiros[1])
print(Lista_frutas[1])

#primeiro elemento da lista
print(Lista_inteiros[-1])
print(Lista_frutas[-1])



i=0
while (i<len(Lista_inteiros)):
    print(Lista_inteiros[i])
    i=i+1

for i in Lista_inteiros:
    print(i)

lista = [3,5,7,9]
print(lista)

lista = [2]
print(lista)

lista=[]
print(lista)


lista = [3,5,7,9]
print(lista)

lista[1] = 10
print(lista)

lista[0] = 8
print(lista)

lista[3] = 1
print(lista)


lista=[2,4,6,8,10]
print(lista)
lista = lista + [5.0]
print(lista)

lista=[2,4,6,8,10]
print(lista)
lista.append(99.0)
print(lista)

lista=[2,4,6,8,10]
print(lista)
lista.extend([99.0, 10.1, 50])
print(lista)

#Entrada de dados em uma lista de tamanho fixo.

nomes=[""] * 4
print(nomes)

print ("Digite 4 nomes: ")
for i in range(4):
    nomes[i]=input()
print(nomes)

#Entrada de dados em uma lista de tamanho variável.

notas=[] * 4
print(notas)

nota=float(input("Digite as notas (Digite -1 para sair): "))

while (nota>=0):
    notas.append(nota)
    nota=float(input("Digite as notas (Digite -1 para Sair): "))
print(notas)
