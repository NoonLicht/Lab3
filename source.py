import random
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 4, 1)

sp500 = []
for i in range((end_date - start_date).days):
    date = start_date + timedelta(days=i)
    price = random.uniform(4000, 4500) # Здесь можно изменить диапазон цен
    sp500.append((date.strftime('%Y-%m-%d'), price))

# Передача данных второй программе (серверу)
with open('sp500_data.txt', 'w') as f:
    for date, price in sp500:
        f.write(f"{date},{price}\n")
