from collections import defaultdict
import pandas as pd

sp500_data = defaultdict(list)

# Чтение данных из файла, переданного от первой программы
with open('sp500_data.txt', 'r') as f:
    for line in f:
        date, price = line.strip().split(',')
        sp500_data[date].append(float(price))

# Обработка данных
processed_data = []
for date, prices in sp500_data.items():
    avg_price = sum(prices) / len(prices)
    source = 'ALPHA VANTAGE' # Здесь можно изменить источник информации о курсе
    processed_data.append((date, avg_price, 'S&P500', source))

# Передача данных третьей программе (визуализатору)
with open('processed_data.txt', 'w') as f:
    f.write("Date,Price,Exchange,Source\n")
    for date, price, exchange, source in processed_data:
        f.write(f"{date},{price},{exchange},{source}\n")

df = pd.read_csv("processed_data.txt")
df.to_excel("processed_data.xlsx", index=False)