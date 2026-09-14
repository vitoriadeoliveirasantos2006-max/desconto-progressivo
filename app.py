# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a faixa de desconto
if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

# Calcula o valor do desconto e o total a pagar
valor_desconto = valor_compra * percentual_desconto
total_pagar = valor_compra - valor_desconto

# Exibe os resultados
print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")