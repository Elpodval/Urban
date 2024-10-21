import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс
        self.lock = threading.Lock()  # Объект Lock для блокировки потоков

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайное число для пополнения
            with self.lock:  # Блокировка потока
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Ожидание

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)  # Случайное число для снятия
            print(f"Запрос на {amount}")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)  # Ожидание

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
