# Aprimore o desafio 93 para que ele funcione com vários jogadores
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador,jo=[],{}
while True:
    print("-"*40)
    jo={"Jogador": input("Nome do Jogador:").title(),"gols": [],"total":0}
    for c in range(0,int(input(f"Quantas prtidas {jo['Jogador']} jogou?:"))):
        jo["gols"].append(int(input(f"Quantos gols na {c+1}º partida?: ")))
        jo["total"] += jo["gols"][c]
    jogador.append(jo.copy())
    es=input("Quer continuar?:").strip()
    if es in "Nn":
        break
print("=-"*40)
print(f"cod {'nome':<18}{'gols':<30}total")
print("-"*80)
for d,c in enumerate(jogador):
    print(f"{d:>3}",end=" ")
    for k,v in c.items():
        if k=="gols":
            print(f"{str(v):<30}", end="")
        else:
            print(f"{v:<18}",end="")
    print()
while True:
    print("-"*50)
    num=int(input("Mostrar dados de que jogador?(999 para parar):"))
    if num==999:
        break
    if num>len(jogador):
        print(f"ERRO! Não existe jogador com código {num}! Tente novamente.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogador[num]['Jogador']}")
        for e,n in enumerate(jogador[num]["gols"]):
            print(f"{'=>':>5}No {e+1}º jogo, fez {n} gols. ")
print("<< VOLTE SEMPRE >>")
