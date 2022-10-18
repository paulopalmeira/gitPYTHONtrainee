sexo=""
idade=0
qtdMulheres=0
valorIdade=0

for i in range(0,3):
    sexo=input("Digite o sexo (M ou H)")
    idade=int(input("Digite a idade"))

    if(sexo=="M" or sexo=="m"):
        qtdMulheres+=1

    valorIdade+=idade

mediaIdade=valorIdade/qtdMulheres

print("A quantidade de mulheres é", qtdMulheres)
print("A média de idade das mulheres é", mediaIdade)
