def is_prime(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if result < 2:
            print('составное')
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")  # Если не нашли делителей
        return result  # Возвращаем результат функции
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

result1 = sum_three(2,3,6)
print(result1)
result2 = sum_three(0.5,0.4,1)
print(result2)
