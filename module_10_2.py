import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # 1 секунда = 1 день сражения
            self.days += 1  # +1 день
            self.enemies -= self.power  # Уменьшаем количество врагов на силу рыцаря
            
            if self.enemies < 0:
                self.enemies = 0  # Убедимся, что количество врагов не отрицательное
            
            day_word = "день" if self.days % 10 == 1 and self.days % 100 != 11 else "дня" if (self.days % 10 in [2, 3, 4] and self.days % 100 not in [12, 13, 14]) else "дней"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

print("Все битвы закончились!")