import json
from collections import defaultdict

# Загрузка данных из файла
with open('orders_july_2023.json', 'r') as file:
    orders = json.load(file)

# Инициализация переменных для хранения результатов
max_price = 0
max_order = ''
max_items = 0
max_items_order = ''
orders_count_by_day = defaultdict(int)
user_orders_count = defaultdict(int)
user_total_price = defaultdict(float)
total_price = 0
total_orders = 0
total_orders_price = 0
total_items = 0

# Обработка данных
for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    order_date = orders_data['date']  # Предполагаем, что дата в формате 'YYYY-MM-DD'
    user_id = orders_data['user_id']

    # 1. Номер самого дорогого заказа за июль
    if price > max_price:
        max_price = price
        max_order = order_num

    # 2. Номер заказа с самым большим количеством товаров
    if quantity > max_items:
        max_items = quantity
        max_items_order = order_num

    # 3. Подсчет заказов по дням в июле
    orders_count_by_day[orders_data['date']] += 1

    # 4. Подсчет количества заказов пользователей
    user_orders_count[user_id] += 1

    # 5. Подсчет суммарной стоимости заказов пользователей
    user_total_price[user_id] += price

    total_orders_price += orders_data['price']
    total_items += orders_data['quantity']

# 6. Определяем день с максимальным количеством заказов в июле
max_orders_day = max(orders_count_by_day.items(), key=lambda x: x[1])[0]

# 7. Пользователь с самым большим количеством заказов за июль
max_user_orders = max(user_orders_count.items(), key=lambda x: x[1])[0]

# 8. Пользователь с самой большой суммарной стоимостью заказов за июль
max_user_total_price = max(user_total_price.items(), key=lambda x: x[1])[0]

# 9. Средняя стоимость заказа в июле
average_order_price = total_orders_price / len(orders)

# 10. Средняя стоимость товаров в июле (в данном случае предполагаем, что items_count - это количество товаров)
average_items_price = total_orders_price / total_items

# Вывод результатов
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
print(f'2. Номер заказа с самым большим количеством товаров: №{max_items_order}, количество товаров: {max_items}')
print(f'3. День с наибольшим количеством заказов в июле: {max_orders_day}, количество заказов: {orders_count_by_day[max_orders_day]}')
print(f'4. Пользователь с самым большим количеством заказов за июль: ID {max_user_orders}, количество заказов: {user_orders_count[max_user_orders]}')
print(f'5. Пользователь с самой большой суммарной стоимостью заказов за июль: ID {max_user_total_price}, сумма: {user_total_price[max_user_total_price]}')
print(f'6. Средняя стоимость заказа в июле: {average_order_price}')
print(f'7. Средняя стоимость товаров в июле: {average_items_price}')
