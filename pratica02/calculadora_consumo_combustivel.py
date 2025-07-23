"""
Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo.
 Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e
exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais.
"""

# Dados da viagem
distancia_percorrida = 300 # Em Km (quilômetros)
combustivel_gasto = 25 # Em L (litros)

consumo_medio = distancia_percorrida / combustivel_gasto

print("Dados da viagem:")
print(f"Distância percorrida: {distancia_percorrida} quilômetros")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
#print(round(consumo_medio,2))
