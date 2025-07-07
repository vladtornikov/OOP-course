"""Класс CaesarCipher
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].

Тестовые задания: https://github.com/python-generation/OOP/tree/main/Module_9/Module_9.1/Module_9.1.3"""

import string

class CaesarCipher:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    def __init__(self, shift: int) -> None:
        self.shift = shift

    def encode(self, to_encode: str) -> str:
        return ''.join(self.shift_char(letter, self.shift) for letter in to_encode)

    def decode(self, to_decode: str) -> str:
        return ''.join(CaesarCipher.shift_char(letter, -self.shift) for letter in to_decode)

    @staticmethod
    def shift_char(char: str, shift: int):
        if char in CaesarCipher.lowercase:
            return CaesarCipher.lowercase[(CaesarCipher.lowercase.index(char) + shift) % 26]
        elif char in CaesarCipher.uppercase:
            return CaesarCipher.uppercase[(CaesarCipher.uppercase.index(char) + shift) % 26]
        else:
            return char