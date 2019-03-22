qtde_inverno=0
qtde_verao=0
qtde_outono=0
qtde_primavera=0
resposta=""

while(resposta!="SIM"):
    estacao_fav=""
    while estacao_fav!="OUTONO" and estacao_fav!= "VERAO" and estacao_fav!="PRIMAVERA" and estacao_fav!="INVERNO":
        estacao_fav = input("Qual a estação que você prefere?").upper()
    if estacao_fav=="OUTONO":
        qtde_outono+=1
    elif estacao_fav=="VERAO":
        qtde_verao+=1
    elif estacao_fav=="INVERNO":
        qtde_inverno+=1
    else:qtde_primavera+=1
    resposta=input("Deseja sair da pergunta? ").upper()


print("Com essa pesquisa vimos que: ")
print("Total de pessoas que responderam que preferem o inverno é : ", qtde_inverno, "pessoas")
print("Total de pessoas que responderam que preferem o outono é : ", qtde_outono, "pessoas")
print("Total de pessoas que responderam que preferem o primavera é : ", qtde_primavera, "pessoas")
print("Total de pessoas que responderam que preferem o verão é : ", qtde_verao, "pessoas")




