prices = [57.8, 46.51, 97, 86.75, 50, 45, 99.99, 12.50]
# Задание А
for i in prices:
    print(f'{int(i)} руб. {int(i * 100 % 100):02} коп.')
# Цены, отсортированные по возрастанию
print(f"id {id(prices)}, list of prices {prices}")
print(f"id {id(prices)}, list of prices {sorted(prices)}")
# Цены, отсортированные по убыванию
print(f"id {id(prices)}, list of prices {sorted(prices, reverse = True)}")
# 5 дорогих товаров
print(sorted(prices[:5], reverse = True))
