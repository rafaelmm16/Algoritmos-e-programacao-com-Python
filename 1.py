velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    excesso_velocidade = velocidade - 80
    multa = excesso_velocidade * 7
    print(f"Você foi multado! O valor da multa é de R$ {multa:.2f}.")
else:
    print("Parabéns! Você está dentro do limite de velocidade.")