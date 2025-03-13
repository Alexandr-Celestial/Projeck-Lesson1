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
Для тестирования проекта используется библиотека `pytest`. Тесты написаны для всех функций проекта и находятся в директории `tests/`.
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
## Модуль utils
Модуль `utils` содержит функцию для чтения JSON-файла.
### Функция read_json_file
Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
```transactions = read_json_file('data/operations.json')```
## Модуль external_api
Модуль `external_api` содержит функцию для конвертации валют.
### Функция convert_currency
Конвертирует сумму транзакции в рубли.
```
transaction = {
'operationAmount': {
'amount': '100.0',
'currency': {
'code': 'USD'
}
}
}
amount_in_rub = convert_currency(transaction)
```
##Чтение CSV и Excel файлов
Проект поддерживает чтение финансовых операций из CSV и Excel файлов благодаря библиотеке `pandas`.
### Установка pandas
Для использования функций необходимо установить `pandas`. Вы можете сделать это с помощью Poetry:
```
poetry add pandas
```
### Примеры использования
#### Чтение CSV файла
```from src.data_loader import read_csv_file```
Пример чтения CSV файла
```
file_path = "data/transactions.csv"
transactions = read_csv_file(file_path)
print(transactions)
```
#### Чтение Excel файла
```from src.data_loader import read_excel_file```
Пример чтения Excel файла
```
file_path = "data/transactions_excel.xlsx"
transactions = read_excel_file(file_path)
print(transactions)
```
### Тестирование
Для тестирования функций используйте команду:
```pytest tests/test_data_loader.py```
Эта команда запустит тесты для функций чтения CSV и Excel файлов.