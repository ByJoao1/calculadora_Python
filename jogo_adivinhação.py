import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        try:
            chute = int(input("Adivinhe um número entre 1 e 100: "))
            tentativas += 1
            
            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()
