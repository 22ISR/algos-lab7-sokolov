"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""




# Задание №1

# def isPalindrom(word):
#     cleaner_word = word.replace(" ", "").lower()
#     reversed_word = cleaner_word[::-1]
#     return reversed_word == cleaner_word
# a = input("word")
# if isPalindrom(a):
#     print("Палиндром")
# else:
#     print("не Палиндром")

# def isPalindrom(word):
#     cleaner_word = word.replace(" ", "").lower()
#     reversed_word = cleaner_word[::-1]
#     return reversed_word == cleaner_word
# a = input("word")
# if isPalindrom(a):
#     print("Палиндром")
# else:
#     print("не Палиндром")

# Задание №2

# def isPalindrom(words):
#     cleaner_word = words.replace(" ", "").lower()
#     reversed_word = cleaner_word[::-1]
#     return reversed_word == cleaner_word

# def isPalindromList(words):
#     palindroms = []
#     for word in words:
#         if isPalindrom(word):
#             palindroms.append(word)
#     return palindroms

# print(isPalindromList(["hello", "ро тор", "list", "level"]))

# Задание №3
def isPalindrom(words):
    cleaner_word = words.replace(" ", "").lower()
    reversed_word = cleaner_word[::-1]
    return reversed_word == cleaner_word

def isPalindromString(string):
    palindroms = []
    for word in words:
        if isPalindrom(word):
            palindroms.append(word)
    return palindroms

print(isPalindromString("Madam, Anna went to the civic center"))
