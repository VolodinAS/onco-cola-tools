from pydantic.v1.validators import ordered_dict_validator

from src.onco_cola_utils.dual_alphabetic_controller import DualAlphabeticController


def main():
    dab: DualAlphabeticController = DualAlphabeticController("привeт")

    print(f"{dab.highlight=}")

if __name__ == '__main__':
    main()