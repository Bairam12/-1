price = float(input())
quantity = int(input())

cost = price * quantity
nds = cost * 0.12
total = cost + nds

print("Стоимость покупки:", cost)
print("НДС 12%:", nds)
print("Итоговая стоимость:", total)
