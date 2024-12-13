
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print("Пример данных:", response.json()[:2])
else:
    print("Ошибка при запросе:", response.status_code)

import pandas as pd

data = response.json()
df = pd.DataFrame(data)
print("\nСтруктура данных:")
print(df.info())
print("\nОписание числовых данных:")
print(df.describe())
print("\nЧастота встречаемости значений в userId:")
print(df['userId'].value_counts())

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
df['userId'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Распределение количества постов по userId")
plt.xlabel("userId")
plt.ylabel("Количество постов")
plt.show()
