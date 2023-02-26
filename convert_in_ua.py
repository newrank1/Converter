#Функції для перетворення
def hex_to_decimal(hex_num):
    return int(hex_num, 16)

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def decimal_to_hex(decimal_num):
    return hex(decimal_num).replace("0x", "")

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

#Підтримувані системи числення
NUMBER_FORMATS = ["hex", "binary", "decimal"]

#Вибір формату числа та його значення
number_format = ""
while number_format not in NUMBER_FORMATS:
    number_format = input("Виберіть формат числа (hex, binary або decimal): ")
    if number_format not in NUMBER_FORMATS:
        print("Недопустимий формат числа, спробуйте ще раз.")

number_value = input(f"Введіть число у форматі {number_format}: ")

#Перетворення числа в десяткову систему числення
if number_format == "hex":
    decimal_value = hex_to_decimal(number_value)
elif number_format == "binary":
    decimal_value = binary_to_decimal(number_value)
else:
    decimal_value = int(number_value)

#Вибір формату для виведення результату та вивід результату
output_format = ""
while output_format not in NUMBER_FORMATS:
    output_format = input("Виберіть формат для виведення результату (hex, binary або decimal): ")
    if output_format not in NUMBER_FORMATS:
        print("Недопустимий формат числа, спробуйте ще раз.")

if output_format == "hex":
    output_value = decimal_to_hex(decimal_value)
elif output_format == "binary":
    output_value = decimal_to_binary(decimal_value)
else:
    output_value = str(decimal_value)

print(f"Результат: {output_value} ({output_format})")
