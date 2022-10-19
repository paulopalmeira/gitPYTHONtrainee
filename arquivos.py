arq = open("acesso.txt")

linhas = arq.readlines()
for linha in linhas:
    print(linha)

    arq = open("acesso.txt","w+")
 
BotaLaNoFile = ["Fulano","Ciclano","Beltrano", \
"João","Maria"]
 
for lnh in BotaLaNoFile:
    arq.write(lnh)
    arq.write("\n")

arq.close()