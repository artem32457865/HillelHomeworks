import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("homework.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def divide(a, b):
    logger.debug(f"Виклик divide з аргументами: a={a}, b={b}")

    try:
        result = a / b
        logger.info(f"Результат ділення: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Помилка: ділення на нуль")
        return None


divide(10, 2)
divide(10, 0)