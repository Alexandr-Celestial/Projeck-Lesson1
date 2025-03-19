import os

from src.data_loader import read_csv_file, read_excel_file
from src.external_api import convert_currency_for_rub
from src.processing import filter_by_state, sort_by_date
from src.search import search_by_description
from src.utils import read_json_file


def get_transaction_info(transaction: dict) -> str:
    """Возвращает строку с информацией о транзакции."""
    date = transaction.get("date", "Дата не указана")
    description = transaction.get("description", "Описание не указано")
    account = transaction.get("from", transaction.get("fromAccount", "Счет не указан"))
    return f"{date}: {description}\nСчет: {account}"


def main() -> None:
    """Функция, отвечающая за основу логики проекта"""
    print(
        """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )

    while True:
        try:
            choice = input("Введите номер пункта меню: ")
            if choice in ["1", "2", "3"]:
                break
            else:
                print("Недопустимый выбор. Попробуйте еще раз.")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            return
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    file_paths: dict = {
        "1": ("data/operations.json", read_json_file),
        "2": ("data/transactions.csv", read_csv_file),
        "3": ("data/transactions_excel.xlsx", read_excel_file),
    }

    file_path, read_function = file_paths[choice]

    try:
        transactions = read_function(file_path)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return

    print(f"Для обработки выбран {os.path.splitext(file_path)[1][1:].upper()} файл")

    available_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        try:
            state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): "
            ).upper()
            if state in available_states:
                break
            else:
                print(
                    f"Статус операции {state} недоступен.\nВведите статус, по которому необходимо выполнить фильтрацию"
                )
                print("Доступны для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            return
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    try:
        filtered_transactions = filter_by_state(transactions, state)
        print(f"Операции отфильтрованы по статусу '{state}'")
    except Exception as e:
        print(f"Произошла ошибка при фильтрации: {e}")
        return

    operations: list[tuple] = [
        ("Отсортировать операции по дате", "Да/Нет", sort_by_date),
        ("Выводить только рублевые транзакции", "Да/Нет", lambda x: x),
        ("Отфильтровать список транзакций по определенному слову в описании", "Да/Нет", search_by_description),
    ]

    for operation, answer_type, func in operations:
        answer = input(f"{operation}? {answer_type} ")
        if answer.lower() == "да":
            try:
                if operation == "Отсортировать операции по дате":
                    sort_order = input("Отсортировать по возрастанию или по убыванию? ")
                    if sort_order.lower() == "по возрастанию":
                        filtered_transactions = func(filtered_transactions)
                    elif sort_order.lower() == "по убыванию":
                        filtered_transactions = func(filtered_transactions, reverse=True)
                    else:
                        print("Недопустимый порядок сортировки.")
                elif operation == "Выводить только рублевые транзакции":
                    filtered_transactions = [
                        transaction
                        for transaction in filtered_transactions
                        if "operationAmount" in transaction
                        and "currency" in transaction["operationAmount"]
                        and transaction["operationAmount"]["currency"]["code"] == "RUB"
                    ]
                elif operation == "Отфильтровать список транзакций по определенному слову в описании":
                    search_string = input("Введите слово для поиска: ")
                    filtered_transactions = func(filtered_transactions, search_string)
            except Exception as e:
                print(f"Произошла ошибка при {operation.lower()}: {e}. Проверьте данные и попробуйте еще раз.")
                return

    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print(get_transaction_info(transaction))
            if "operationAmount" in transaction and "amount" in transaction["operationAmount"]:
                try:
                    rub_amount = convert_currency_for_rub(transaction)
                    print(f"Сумма: {rub_amount} RUB")
                except Exception as e:
                    print(f"Произошла ошибка при конвертации валюты: {e}.")
            else:
                print("Сумма не указана")

            print()
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
