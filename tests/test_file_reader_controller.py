from pathlib import Path

from src.onco_cola_utils import log, logerr, logsuc
from src.onco_cola_utils.file_reader_controller import FileReaderController


print = log


def get_curent_path() -> Path:
    return Path(__file__).resolve().parent


def test_file_reader_controller_initialization():
    """Проверка инициализации ReaderController"""
    file_path: Path = get_curent_path() / "text.txt"
    
    write_data: str = "some_data"
    
    print(f"{file_path=}")
    if not file_path.exists():
        result = FileReaderController.save_text(file_path, write_data)
        if not result:
            logerr("❌ ЗАПИСЬ В ФАЙЛ НЕ ПРОИЗОШЛА")
        else:
            logsuc("✅ ДАННЫЕ ЗАПИСАНЫ В ФАЙЛ")
    
    data: str = FileReaderController.read_text(file_path)
    print(f"{data=}")
    
    assert data == write_data
    
    print("✅ FileReaderController инициализирован корректно")


if __name__ == "__main__":
    # Запуск тестов напрямую
    test_file_reader_controller_initialization()
