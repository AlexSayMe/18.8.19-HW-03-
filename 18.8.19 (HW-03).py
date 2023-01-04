tickets = int(input('Колличество билетов которое вы хотите приобрести: '))
age = [int(input('Введите возраст посетителей: ')) for i in range(tickets)]
price = 0

for i in range(len(age)):
    if age[i] <= 18:
        price += 0
        print(price)
    elif 18 <= age[i] <= 25:
        price += 990
        print(price)
    else:
        price += 1390
        print(price)
if tickets >= 3:
    price = price * 0.9
print(price)







