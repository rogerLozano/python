import random
import time

jogador = input("Insira sua jogada : PEDRA, PAPEL OU TESOURA!") 

if jogador == "PEDRA" or jogador == "PAPEL" or jogador == "TESOURA": 
    
    print("JO")
    time.sleep(3)
    print("KEN")
    time.sleep(3)
    print("POOOOO")
    
    maquina = ["PEDRA","PAPEL","TESOURA"]
    valor_randomico = random.randrange(0,3)
    maquina = maquina[valor_randomico] 
    if maquina == jogador:
        print("empate")
    elif maquina == "PEDRA" and jogador == "TESOURA":
        print("MAQUINA GANHOU POIS PEDRA GANHA DE TESOURA!")
    elif maquina == "TESOURA" and jogador == "PAPEL":
        print("MAQUINA GANHOUU POIS TESOURA GANHA DE PAPEL")
    elif maquina == "PAPEL" and jogador == "PEDRA": 
        print("MAQUINA GANHOU PAPEL GANHA DE TESOURA")
    else:
        print("JOGADOR GANHOU")    
else:
    print("Errado!")

