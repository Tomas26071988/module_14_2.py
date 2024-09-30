import sqlite3

connection = sqlite3.connect('Module14_2.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
) 
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# Без этого - у меня каждый раз добавляет новые значения!!! Очищаем таблицу перед вставкой новых данных
cursor.execute("DELETE FROM Users")

for i in range(9):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                   (f"User1{i}", f"{i}example1@gmail.com", i * 10, 1000))

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
cursor.execute("DELETE FROM Users WHERE id = 6")
# записываю изменения
connection.commit()

# выделяю все (можно со звездочкой делать ) и прописываю где нет возраста 60)
cursor.execute('SELECT * FROM Users')
res = cursor.fetchall()

for record in res:
   print(f'ID: {record[0]} | Имя: {record[1]} | Почта: {record[2]} | Возраст: {record[3]} | Баланс: {record[4]}')



# считаю общее кол-во пользователей

cursor.execute("SELECT COUNT(*) FROM Users")
all_users = cursor.fetchone()[0]

# считаю сумму всех балансов

cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]

# средний баланс

cursor.execute("SELECT AVG(balance) FROM Users")
average_balance = cursor.fetchone()[0]

# Вывод среднего баланса
print(average_balance)


connection.commit()
connection.close()
