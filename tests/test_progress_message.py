from datetime import timedelta

from src.onco_cola_utils.progress_message import ProgressMessage

total = 100_000_000

pm = ProgressMessage(
    total=total,
    every=timedelta(seconds=5)
)  # всего 1000 элементов

for i in range(1, total+1):
    # ... делаем полезную работу ...
    pm.update(i)
    pm.log_me("Обработка: {log}")  # или можно добавить в строку
