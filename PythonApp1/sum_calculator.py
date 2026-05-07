def process_numbers():
    try:
        # Пытаемся открыть и прочитать файл input.txt
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            content = input_file.read()
        
        # Разбиваем содержимое на числа (по пробелам, запятым, переносам строк)
        numbers = []
        for part in content.split():
            try:
                # Пробуем преобразовать в число с плавающей точкой
                # Если нужны только целые числа, замените float на int
                number = float(part)
                numbers.append(number)
            except ValueError:
                # Пропускаем нечисловые значения
                print(f"Предупреждение: '{part}' не является числом и будет пропущено")
        
        if not numbers:
            # Если чисел нет, записываем 0
            total = 0
            print("В файле не найдено чисел.")
        else:
            # Вычисляем сумму
            total = sum(numbers)
        
        # Записываем результат в output.txt
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(str(total))
        
        print(f"Сумма чисел: {total}")
        print("Результат записан в файл output.txt")
        
    except FileNotFoundError:
        # Обработка случая, когда файл не найден
        print("Ошибка: Файл 'input.txt' не найден.")
        print("Пожалуйста, создайте файл input.txt с числами.")

if __name__ == "__main__":
    process_numbers()