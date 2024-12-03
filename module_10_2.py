from threading import Thread
from time import sleep

# Общая переменная для врагов
total_enemies = 100


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global total_enemies
        days = 0
        print(f"{self.name}, на нас напали!")

        while total_enemies > 0:
            days += 1
            sleep(1)
            if total_enemies > 0:  # Проверка, остались ли враги
                total_enemies -= self.power
                total_enemies = max(total_enemies, 0)  # Чтобы врагов не стало меньше 0
                print(f"{self.name} сражается {days} день(дня)..., осталось {total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
