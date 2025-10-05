def bubble_sort(numbers, ascending=True):
    """
    Функция для сортировки списка чисел методом пузырька
    с возможностью выбора направления сортировки
    
    Args:
        numbers: список чисел для сортировки
        ascending: если True - по возрастанию, False - по убыванию
    """
    n = len(numbers)
    
    # Проходим по всем элементам списка
    for i in range(n):
        # Флаг для оптимизации - если не было перестановок, список отсортирован
        swapped = False
        
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Выбираем условие сравнения в зависимости от направления сортировки
            if ascending:
                condition = numbers[j] > numbers[j + 1]
            else:
                condition = numbers[j] < numbers[j + 1]
            
            # Если условие выполняется, меняем элементы местами
            if condition:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        
        # Если не было перестановок, выходим досрочно
        if not swapped:
            break
    
    return numbers

def get_sorting_direction():
    """
    Функция для запроса направления сортировки у пользователя
    """
    print("\nВыберите направление сортировки:")
    print("1 - По возрастанию (от меньшего к большему)")
    print("2 - По убыванию (от большего к меньшему)")
    
    while True:
        choice = input("Ваш выбор (1 или 2): ").strip()
        
        if choice == "1":
            return True  # ascending
        elif choice == "2":
            return False  # descending
        else:
            print("Неверный выбор! Пожалуйста, введите 1 или 2.")

def main():
    """
    Основная функция программы
    """
    print("=== Программа сортировки чисел методом пузырька ===")
    print("С возможностью выбора направления сортировки")
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
        
        # Запрашиваем направление сортировки
        ascending = get_sorting_direction()
        
        # Сортируем список
        sorted_numbers = bubble_sort(numbers.copy(), ascending)
        
        # Выводим результат
        direction = "по возрастанию" if ascending else "по убыванию"
        print(f"\nСписок отсортированный {direction}: {sorted_numbers}")
        
        # Дополнительная информация
        if ascending:
            print(f"Минимальное число: {sorted_numbers[0]}")
            print(f"Максимальное число: {sorted_numbers[-1]}")
        else:
            print(f"Максимальное число: {sorted_numbers[0]}")
            print(f"Минимальное число: {sorted_numbers[-1]}")
        
    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число для количества!")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()