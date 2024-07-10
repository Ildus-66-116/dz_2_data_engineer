# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX = 16
hex_digits = "0123456789abcdef"

num = int(input('Введите число: '))

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print(f"Шестнадцатеричное представление числа:, 0x{hex_num}")
print("Проверка результата:", test_hex_num)
