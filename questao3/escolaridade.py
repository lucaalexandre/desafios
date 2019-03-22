

qtde_medio=0
qtde_superior=0
qtde_pos=0
resposta=""

while(resposta!="SIM"):
    nivel=""
    while nivel!="MEDIO" and nivel!= "POS" and nivel!="SUPERIOR":
       nivel = input("Qual é o seu nivel de escolaridade? (Médio, Superior ou Pós)").upper()
    if nivel=="SUPERIOR":
        qtde_medio+=1
    elif nivel=="POS":
        qtde_pos+=1
    else:qtde_superior+=1
    resposta=input("Deseja sair da pergunta? ").upper()


print("Com essa pesquisa vimos que: ")
print("Total de pessoas que responderam que sao pos-graduadas é : ", qtde_medio, "pessoas")
print("Total de pessoas que responderam que tem o ensino medio é : ", qtde_pos, "pessoas")
print("Total de pessoas que responderam que sao graduadas é : ", qtde_superior, "pessoas")

