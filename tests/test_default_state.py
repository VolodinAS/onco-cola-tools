from time import sleep

from src.onco_cola_utils import pretty_print
from src.onco_cola_utils.default_state import DefaultState


def main():
    test_data: DefaultState = DefaultState()
    pretty_print(test_data, title=f"test_data", m2d=False)
    test_data.update(detail="Обновлённый стейт")
    pretty_print(test_data, title=f"test_data", m2d=False)
    sleep(5)
    test_data.success(detail="Успешный ответ")
    pretty_print(test_data, title=f"test_data", m2d=False)
if __name__ == '__main__':
    main()
