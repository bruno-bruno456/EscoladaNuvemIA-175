"""
Desenvolva um programa que calcula o desconto em uma loja.
Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 

O programa deve calcular o valor do desconto e o preço final,
exibindo todos os detalhes.
"""
# Dados do enunciado
nome_produto = "Camiseta"
preco_original = 50.00
porgentagem_desconto = 20

# Cálculo do valor de desconto
valor_desconto = preco_original * (porgentagem_desconto / 100)

# Calculo do Preço Final
preco_final = preco_original - valor_desconto


print("Produto:", nome_produto)
print(f"Preço Original: R$ {preco_original:.2f}")
print("Desconto:", porgentagem_desconto, "%")
#print(f"Desconto: {porgentagem_desconto} %")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
