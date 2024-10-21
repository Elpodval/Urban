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
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()  # Разблокировка, если баланс >= 500
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
                    self.lock.acquire()  # Блокировка потока, если недостаточно средств
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

# Класс Bank: Имеет атрибуты balance и lock. balance хранит текущий баланс, а lock используется для управления
# доступом к этому атрибуту из разных потоков.
#
# Метод deposit: Выполняет 100 транзакций пополнения. Используется блокировка для безопасного изменения баланса.
# Если баланс становится 500 или больше и замок заблокирован, он разблокируется.
#
# Метод take: Выполняет 100 транзакций снятия. Также использует блокировку. Если запрашиваемая сумма больше текущего
# баланса, поток блокируется.
#
# Создание потоков: Создаются два потока, которые запускают методы deposit и take, после чего основной поток ожидает
# их завершения с помощью join.
#
# Вывод итогового баланса: После завершения потоков выводится текущий баланс.


