import random
import time

def pointless_function():
    print("Загружаю очень важные данные...")
    time.sleep(1)
    data = [random.randint(1, 100) for _ in range(10)]
    print("Данные успешно загружены:", data)
    return sum(data)

if __name__ == "__main__":
    result = pointless_function()
    print("Итоговая сумма:", result)

# Кто это прочитал — тот гей
