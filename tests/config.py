from pathlib import Path

from src.onco_cola_utils import log


print = log


class Config:
    def __init__(self):
        self.current_path: Path = Path(__file__).resolve().parent
        self.root_path: Path = self.current_path.parent
        self.tests_path: Path = self.root_path / "tests"
        if not self.tests_path.exists():
            self.tests_path.mkdir(exist_ok=True)
        self.tests_temp_path: Path = self.tests_path / "temp"
        if not self.tests_temp_path.exists():
            self.tests_temp_path.mkdir(exist_ok=True)
