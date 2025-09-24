import traceback
from pathlib import Path

from src.onco_cola_utils import logsuc, pretty_print
from src.onco_cola_utils.json_reader_controller import JsonReader
from tests.config import Config


config: Config = Config()


def main():
    """MAIN"""
    json_dict_file_path: Path = config.tests_temp_path / "test_json_dict.json"
    json_list_file_path: Path = config.tests_temp_path / "test_json_list.json"

    try:
        json_dict_reader: JsonReader = JsonReader(json_dict_file_path)
    except FileNotFoundError as e:
        traceback.print_exc()
        logsuc("Тут должна быть ошибка, что файла не существует")
        logsuc("---")
        logsuc("---")

    try:
        json_list_reader: JsonReader = JsonReader(json_list_file_path)
    except FileNotFoundError as e:
        traceback.print_exc()
        logsuc("Тут должна быть ошибка, что файла не существует")
        logsuc("---")
        logsuc("---")

    JsonReader.write_pretty({"dict": "ok"}, json_dict_file_path)
    JsonReader.write_pretty(["list", "ok"], json_list_file_path)

    json_dict_reader: JsonReader = JsonReader(json_dict_file_path)
    json_list_reader: JsonReader = JsonReader(json_list_file_path)

    pretty_print(json_dict_reader.info(), title=f"json_dict_reader.info()", m2d=False)
    pretty_print(json_list_reader.info(), title=f"json_list_reader.info()", m2d=False)
    
    pretty_print(json_dict_reader.data, title=f"json_dict_reader.data", m2d=False)
    pretty_print(json_list_reader.data, title=f"json_list_reader.data", m2d=False)

if __name__ == '__main__':
    main()
