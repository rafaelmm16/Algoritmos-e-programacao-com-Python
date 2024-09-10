def calcular_estatisticas():
    """Calcula a soma, média e quantidade de números digitados pelo usuário.

    O programa continua a ler números até que o usuário digite 0.
    """

    soma = 0
    quantidade = 0

    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"Quantidade de números: {quantidade}")
        print(f"Soma dos números: {soma}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número foi digitado.")

calcular_estatisticas()