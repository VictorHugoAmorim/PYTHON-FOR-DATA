from forex_python.converter import CurrencyRates

c = CurrencyRates()

# Solicita o valor que será convertido $ -> R$
valor = float(input("\nDigite o valor (USD) que será convertido (R$):\n"))

# Converte e formata o resultado
resultado = round(c.convert("USD", "BRL", valor), 2)

# Exibe o resultado
print(f'${valor} = R${resultado}')

