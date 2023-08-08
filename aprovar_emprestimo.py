# Solicita ao usuário o valor da casa, o salário do comprador e o período de financiamento
casa = float(input("Qual o valor da casa: RS_"))
salario = float(input("Salário do comprador: RS_"))
anos = int(input("Quantos anos de financiamento?_"))

# Calcula a prestação mensal dividindo o valor da casa pelo total de meses no período de financiamento
prestacao = casa / (anos * 12)

# Calcula o valor mínimo da prestação permitido (30% do salário do comprador)
minimo = salario * 30 / 100

# Imprime uma mensagem formatada com o valor da casa, o período de financiamento e a prestação estimada
print(
    "Para pagar uma casa de {:.2f} em {} anos, a prestação será de {:.2f}".format(
        casa, anos, prestacao
    )
)

# Verifica se a prestação está dentro do limite permitido e exibe uma mensagem correspondente
if prestacao <= minimo:
    print("O empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
