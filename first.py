a=2
b=4
frequencia=60

if not(frequencia<60):
    soma = a+b
    if (soma >= 6):
        print("Aluno aprovado")
    elif (soma > 2):
        print("Aluno pode ir para recuperação")
    else:
        print("Aluno reprovado")
else:
    print("Aluno reprovado direto")