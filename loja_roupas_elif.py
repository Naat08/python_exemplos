valor_unitario = 12.5
quant = int(input("Digite a quantidade: "))
valor_total = valor_unitario * quant
if quant <= 5:
    valor_total = valor_total * 0.97
elif quant <= 10:
    valor_total = valor_total * 0.95
else:
    valor_total = valor_total * 0.93
print(f"Valor total R$ {valor_total}")
