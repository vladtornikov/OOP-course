"""Классы Domain и DomainException
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():

domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:

Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен.

Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.

Тестовые задания: https://github.com/python-generation/OOP/tree/main/Module_9/Module_9.1/Module_9.1.5"""

from __future__ import annotations

from re import fullmatch, search


class DomainException(Exception):
    def __init__(self, error_message: str = 'Недопустимый домен, url или email'):
        self.error_message = error_message
        super().__init__(self.error_message)

class Domain:
    domain_pattern = '[A-Za-z]+\.[A-Za-z]+'

    def __init__(self, domain: str) -> None:
        if fullmatch(f'{self.__class__.domain_pattern}', domain):
            self._domain = domain
        else:
            raise DomainException

    @classmethod
    def from_url(cls, url: str) -> Domain:
        match = fullmatch(rf'https?://({cls.domain_pattern})', url)
        if match:
            domain = match.group(1)
            return cls(domain)
        else:
            raise DomainException

    @classmethod
    def from_email(cls, email: str) -> Domain:
        match = fullmatch(rf'[A-Za-z]+@({cls.domain_pattern})', email)
        if match:
            domain = match.group(1)
            return cls(domain)
        else:
            raise DomainException

    def __str__(self) -> str:
        return self._domain


