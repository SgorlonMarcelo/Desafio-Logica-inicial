nh = input("Digite o nome do seu Herói: ")
xp = input("Digite a quantidade de XP do seu Herói: ")
xp = int(xp)


if xp < 1000:
    print("O Herói de nome", nh," está no nível Ferro")
elif xp < 2000:
    print("O Herói de nome", nh," está no nível Bronze")
elif xp < 5000:
    print("O Herói de nome", nh," está no nível Prata") 
elif xp < 7000:
    print("O Herói de nome", nh," está no nível Ouro")        
elif xp < 8000:
    print("O Herói de nome", nh," está no nível Platina")
elif xp < 9000:
    print("O Herói de nome", nh," está no nível Ascendente")    
elif xp < 10000:
    print("O Herói de nome", nh," está no nível Imortal")
else:
    print("O Herói de nome", nh," está no nível Radiante")        


