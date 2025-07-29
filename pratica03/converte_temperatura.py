"""
Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

# Solitação da temperatura ao usuário
temperatura = float(input("Digite a temperatura: "))

# Solitar a unidade de origem e unidade de destino:
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade do destino (C, F, K): ").upper()

if origem == destino:
    resultado = temperatura

elif origem == "C": # Origem Celsius
    if destino == "F": # origem Celsius e destino Fahrenheit
        resultado = (temperatura * 9/5) + 32
    else: # origem Celsius e destino Kelvin
        resultado = temperatura + 273.15

elif origem == "F": # Origem Fahrenheit
    if destino == "C": # origem Fahrenheit e destino Celsius  
        resultado = (temperatura - 32) * 5/9
    else: # origem Fahrenheit e destino Kelvin  
        resultado =  (temperatura - 32) * 5/9 + 273.15 

else: # Origem Kelvin
    if destino == "C": # origem Kelvin e destino Celsius     
        resultado = temperatura - 273.15 
    else: # origem Kelvin e destino Fahrenheit
        resultado = (temperatura - 273.15) * 9/5 + 32   
           

print(f"{temperatura} {origem} é igual a {resultado:.2f} {destino}")    

