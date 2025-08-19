# Calculadora de propinas en un restaurante

monto_total = float(input("Ingrese el monto de la cuenta: "))
propina = monto_total * 0.10
propina_sugerida = monto_total * 0.15

print(f"El total a pagar con la propina del 10% es: {monto_total + propina}")
print(f"El total a pagar con la propina del 15% es: {monto_total + propina_sugerida}")