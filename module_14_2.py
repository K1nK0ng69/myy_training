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

cursor.execute("SELECT id FROM Users ORDER BY id")
ids = [row[0] for row in cursor.fetchall()]
for i in range(0, len(ids), 2):
    cursor.execute("UPDATE Users SET balance = 500 WHERE id = ?", (ids[i],))


cursor.execute("SELECT id FROM Users ORDER BY id")
ids = [row[0] for row in cursor.fetchall()]
for i in range(0, len(ids), 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (ids[i],))

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 100 ORDER BY id")
records = cursor.fetchall()

cursor.execute("SELECT COUNT(*) FROM Users")
user_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]

print(f"Количество пользователей: {user_count}")
print(f"Баланс: {balance_sum}")
print(balance_sum/user_count)


connection.commit()
connection.close()
