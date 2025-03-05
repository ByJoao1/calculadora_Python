calculadora = int(input("Digite o número da operação desejada: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))
if calculadora == 1:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A soma dos números é: {n1 + n2}")
elif calculadora == 2:      
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A subtração dos números é: {n1 - n2}")
elif calculadora == 3:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A multiplicação dos números é: {n1 * n2}")
elif calculadora == 4:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"A divisão dos números é: {n1 / n2}")
else:   
    print("Operação inválida")