def calcular_aumento(salario):
  """Calcula o aumento salarial com base no valor atual.

  Args:
    salario: O salário atual do funcionário.

  Returns:
    O valor do aumento.
  """

  if salario > 1250:
    aumento = salario * 0.1  # Aumento de 10%
  else:
    aumento = salario * 0.15  # Aumento de 15%
  return aumento

# Entrada do salário
salario_atual = float(input("Digite o salário do funcionário: R$ "))

# Cálculo do aumento
aumento = calcular_aumento(salario_atual)

# Cálculo do novo salário
novo_salario = salario_atual + aumento

# Saída
print(f"O aumento será de R$ {aumento:.2f}")
print(f"O novo salário será de R$ {novo_salario:.2f}")