# Проект №2
## Описание:
Проект представляет собой виджет на Python для работы крупного банка, который показывает несколько последних успешных банковских операций клиента
## Модули
Проект содержит в себе следующие модули:
+ masks.py
+ widget.py
+ processing.py

### Модуль masks.py
Данный модуль предназначен для маскировки номеров счета и карты клиента
### Модуль widget.py
Работа модуля заключается в получении номера карты или счета, а также преобразования даты и времени к формату ДД.ММ.ГГ
### Модуль processing.py 
Модуль работает со списком словарей и необязательным значением для ключа и сортировки
## Установка
1. Клонируйте репозиторий:
git@github.com:Alexandr-Celestial/Projeck-Lesson1.git
2. Установите зависимости:
Используйте Poetry для создания виртуального окружения и установки зависимостей, включая инструменты разработки такие как: flake 8, black, isort и mypy
## Тестирование
Для запуска тестов выполните следующую команду:
```
pytest --cov=src --cov-report=html
```
Отчет о покрытии кода будет создан в папке Отчет будет сгенерирован в папке `htmlcov` и храниться в файле с названием `index.html`
# Генераторы
## Модуль generators
Этот модуль содержит функции-генераторы для обработки данных транзакций.
### Функция filter_by_currency
Функция фильтрует транзакции по указанной валюте.
```
from src.generators import filter_by_currency
transactions = [ваши данные о транзакциях]
usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
print(transaction)
```
### Функция transaction_descriptions
Функция возвращает описание каждой операции по очереди.
```
from src.generators import transaction_descriptions
descriptions = transaction_descriptions(transactions)
for description in descriptions:
print(description)
```
### Функция card_number_generator
Генератор для создания номеров банковских карт в заданном диапазоне.
```
from src.generators import card_number_generator
for card_number in card_number_generator(1, 5):
print(card_number)
```
## Модуль decorators
Модуль `decorators` содержит декораторы для логирования функций.
### Декоратор log
Декоратор для логирования функций. Может логировать как в файл, так и в консоль.
```
@log(filename="mylog.txt")
def my_function(x, y):
return x + y

my_function(1, 2)
```
