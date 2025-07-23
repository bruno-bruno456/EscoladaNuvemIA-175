"""
Crie um programa que converte um valor em reais para dólares e euros.
Use os seguintes dados:

Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 

O programa deve calcular e exibir os valores convertidos,
arredondando para duas casas decimais.
"""

valor_em_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_em_dolares = valor_em_reais / taxa_dolar
valor_dolar_arredondado = round(valor_em_dolares, 2)

valor_em_euro = valor_em_reais / taxa_euro
valor_euro_arredondado = round(valor_em_euro, 2)

print(f"Valor em Reais: R$ {valor_em_reais:.2f}")
print(f"Valor em Dólares: USD $ {valor_dolar_arredondado}")
print(f"Valor em Euro: € {valor_euro_arredondado}")

