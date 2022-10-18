print("Digite a tabuada de desejada")
varTabuada = int(input())
varContador = 0
while varContador <= 10:
    varResultado = varTabuada * varContador
    print(str(varTabuada) + " x " + str(varContador) + " = " + str(varResultado))
    varContador = varContador + 1

