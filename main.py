from requests import get
from sys import argv
from datetime import datetime
from statistics import mean


if len(argv) < 2:
    print("Not enough arguments")
    exit(1)

url = argv[1]
n = 10
time_list = []
data_list = []

for _ in range(n):
    checkpoint = datetime.now()
    result = get(url)
    difference = datetime.now() - checkpoint
    time_list.append(difference.total_seconds())
    data_list.append(len(result.content) * 8)

print(f"Среднее время запроса: {mean(time_list)} секунд")
print(f"Объем скачанных за {n} запросов данных: {sum(data_list) /8 / 2**20} мегабайт")
print(f"Средня скорость запроса: {(sum(data_list) / 10**6) / sum(time_list)} мегабит/с")
