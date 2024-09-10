def encontrar_maior_e_menor(num1, num2, num3):
  """Encontra o maior e o menor número entre três."""
  numeros = [num1, num2, num3]
  maior = max(numeros)
  menor = min(numeros)
  return maior, menor

# Entrada dos números pelo usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chamando a função e armazenando os resultados
maior_numero, menor_numero = encontrar_maior_e_menor(num1, num2, num3)

# Imprimindo os resultados
print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)