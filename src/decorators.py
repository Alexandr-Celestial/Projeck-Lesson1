from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования функции, а также её результата или ошибок"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if filename:
                    with open(filename, "a") as f:
                        f.write(
                            f"Начало выполнения функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}\n"
                        )
                else:
                    print(f"Начало выполнения функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}")

                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a") as f:
                        f.write(f"Функция {func.__name__} завершилась успешно. Результат: {result}\n")
                else:
                    print(f"Функция {func.__name__} завершилась успешно. Результат: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"Функция {func.__name__} завершилась с ошибкой: {e}\n")
                else:
                    print(f"Функция {func.__name__} завершилась с ошибкой: {e}")
                raise

        return wrapper

    return decorator
