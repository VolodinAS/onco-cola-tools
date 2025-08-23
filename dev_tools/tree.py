from pathlib import Path

import pathspec

from src.onco_cola_utils import System, logerr, loginf, logsuc, pretty_print


# print = log


def load_gitignore(root: Path) -> pathspec.PathSpec:
    gitignore_path = root / ".gitignore"
    if not gitignore_path.exists():
        return pathspec.PathSpec.from_lines("gitwildmatch", [])  # пусто

    with open(gitignore_path, "r", encoding="utf-8") as f:
        lines = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.startswith("#")
        ]
    return pathspec.PathSpec.from_lines("gitwildmatch", lines)


def print_tree(
    path: Path,
    spec: pathspec.PathSpec,
    prefix: str = "",
    is_last: bool = True,
    is_root: bool = True,
):
    if is_root:
        print(f"{path.name}/")

    # Относительный путь для проверки в pathspec
    rel_path = path.relative_to(path.parent if not is_root else path.parent)

    # Проверяем, должен ли путь быть проигнорирован
    if not is_root and spec.match_file(rel_path):
        return

    if path.is_dir():
        try:
            children = sorted(path.iterdir())
        except PermissionError:
            return

        # Фильтруем детей по .gitignore
        items = [child for child in children if not spec.match_file(child.relative_to(path))]

        # Разделяем на папки и файлы (для порядка)
        dirs = [d for d in items if d.is_dir()]
        files = [f for f in items if f.is_file()]
        ordered = dirs + files

        for i, child in enumerate(ordered):
            is_last_child = i == len(ordered) - 1
            connector = "└── " if is_last_child else "├── "
            extension = "    " if is_last_child else "│   "

            print(f"{prefix}{connector}{child.name}")

            if child.is_dir():
                print_tree(
                    child,
                    spec,
                    prefix + extension,
                    is_last_child,
                    is_root=False,
                )


if __name__ == '__main__':
    # В корне проекта
    root = Path(__file__).resolve().parent.parent
    logsuc(root)
    loginf(root)
    logerr(root)
    pretty_print(root, title=f"root", m2d=False)
    print(f"{System.ID=}")
    # exit()
    spec = load_gitignore(root)
    print_tree(root, spec)
