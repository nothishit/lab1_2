def bubble_sort(numbers):
    """
    Функция для сортировки списка чисел методом пузырька
    """
    n = len(numbers)
    
    # Проходим по всем элементам списка
    for i in range(n):
        # Флаг для оптимизации - если не было перестановок, список отсортирован
        swapped = False
        
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        
        # Если не было перестановок, выходим досрочно
        if not swapped:
            break
    
    return numbers

def main():
    """
    Основная функция программы
    """
    print("=== Программа сортировки чисел методом пузырька ===")
    print()
    
    try:
        # Запрашиваем количество чисел
        n = int(input("Введите количество чисел для сортировки: "))
        
        if n <= 0:
            print("Количество чисел должно быть положительным!")
            return
        
        numbers = []
        print(f"\nВведите {n} чисел:")
        
        # Запрашиваем n чисел
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Число {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Пожалуйста, введите корректное число!")
        
        # Выводим исходный список
        print(f"\nИсходный список: {numbers}")
        
        # Сортируем список
        sorted_numbers = bubble_sort(numbers.copy())  # Используем copy чтобы не изменять оригинал
        
        # Выводим отсортированный список
        print(f"Отсортированный список: {sorted_numbers}")
        
        # Дополнительная информация
        print(f"\nМинимальное число: {sorted_numbers[0]}")
        print(f"Максимальное число: {sorted_numbers[-1]}")
        
    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число для количества!")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()