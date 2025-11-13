from typing import Any

from src.onco_cola_utils.advanced_thread_processor import CompletionReport
from src.onco_cola_utils import loginf, log
from src.onco_cola_utils.advanced_thread_processor import AdvancedThreadProcessor

print = log

def your_processing_function(item: Any, thread_id: int):
    loginf(f"[TH={thread_id}] Обработка «{item}»...")
    return True

def on_processing_complete(report: CompletionReport):
    """Колбэк вызываемый при завершении обработки"""
    print(f"🎉 ОБРАБОТКА ЗАВЕРШЕНА!")
    print(
        f"📊 Статистика: {report.stats.success}/{report.stats.total} успешно ({report.success_percentage})"
    )
    print(f"⏱️ Время выполнения: {report.stats.total_duration_str}")
    print(f"🧵 Потоков использовано: {report.stats.threads_used}")

    if report.stats.exhausted_attempts_items:
        print(
            f"⚠️ Элементов с исчерпанными попытками: {len(report.stats.exhausted_attempts_items)}"
        )
    pass


# Использование
processor = AdvancedThreadProcessor(
    data_list=list(range(127)),
    process_method=your_processing_function,
    threads_count=7,
    on_complete_method=on_processing_complete  # Передаем колбэк
)

results = processor.run()

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================

# from src.onco_cola_utils import log, logerr, logsuc
# from src.onco_cola_utils.advanced_thread_processor import AdvancedThreadProcessor
#
#
# print = log
#
#
# def unreliable_processor(item, thread_id: int):
#     """Метод, который может иногда падать"""
#     import random
#     if random.random() < 0.3:  # 30% вероятность ошибки
#         logerr(f"[TH={thread_id}] Ошибка")
#         raise ValueError("Временная ошибка обработки")
#     logsuc(f"[TH={thread_id}] Успех")
#     return f"stable_{item}"
#
#
# # Использование
# processor = AdvancedThreadProcessor(
#     data_list=list(range(1101)),
#     process_method=unreliable_processor,
#     threads_count=10,
#     max_attempts=3,
#     base_timeout=1.0,
#     delta_timeout=0.5,
#     pass_thread_id=True,
#     enable_detailed_logging=True  # Включаем детальное логирование
# )
#
# results = processor.run()
# stats = processor.statistics
#
# print(f"=== ОБЩАЯ СТАТИСТИКА ===")
# print(f"Успешно: {stats.success}/{stats.total}")
# print(f"Неудачно: {stats.failed}/{stats.total}")
# print(f"Элементов с исчерпанными попытками: {len(stats.exhausted_attempts_items)}")
# print("")
# print(f"=== ОТЧЕТ О НЕУДАЧНЫХ ЭЛЕМЕНТАХ ===")
# failed_report = processor.get_failed_items_report()
# for item_report in failed_report:
#     print(
#         f"Элемент {item_report['item']}: {item_report['error_message']} "
#         f"(попыток: {item_report['attempts_made']}/{item_report['max_attempts']})"
#     )

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# import time
#
# from src.onco_cola_utils import log, loginf
# from src.onco_cola_utils.advanced_thread_processor import AdvancedThreadProcessor
#
#
# print = log
#
#
# def process_with_thread_id(item, thread_id: int):
#     loginf(f"Поток {thread_id}: Обрабатываю {item}")
#     time.sleep(0.1)
#     return f"processed_{item}_by_thread_{thread_id}"
#
#
# # Использование
# data = list(range(101))
#
# processor = AdvancedThreadProcessor(
#     data_list=data,
#     process_method=process_with_thread_id,
#     threads_count=10,
#     pass_thread_id=True
# )
#
# results = processor.run()
# stats = processor.statistics
#
# # Теперь работаем с Pydantic моделью
# print(f"Успешно: {stats.success}")
# print(f"Ошибки: {stats.failed}")
# print(f"Общее время: {stats.total_duration_str}")
#
# # Доступ к данным потока
# for thread_id, timing in stats.thread_timings.items():
#     print(f"Поток {thread_id}: {timing.duration_str}")
