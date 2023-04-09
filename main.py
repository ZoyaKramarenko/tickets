ticket_count = int(input("Введите количество билетов"))
summa = 0
for i in range(1, ticket_count + 1):
    age = int(input("Введите возраст посетителя"))
    if age >= 18 and age <= 25:
        summa = summa + 990
    if age > 25:
        summa = summa + 1390
if ticket_count > 3:
    summa = summa*0.9

print("Сумма к оплате =", summa)
