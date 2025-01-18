import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")

cursor.execute("DELETE FROM Users")
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.execute("SELECT id FROM Users")
ids = [row[0] for row in cursor.fetchall()]
for i in range(0, len(ids), 2):
    cursor.execute("UPDATE Users SET balance = 500 WHERE id = ?", (ids[i],))

cursor.execute("SELECT id FROM Users")
ids = [row[0] for row in cursor.fetchall()]
for i in range(0, len(ids), 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (ids[i],))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
records = cursor.fetchall()

print("Вывод на консоль:")
for record in records:
    print(f"Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}")

connection.commit()
connection.close()
