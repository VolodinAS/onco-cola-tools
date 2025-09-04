from src.onco_cola_utils.key_param_class import KeyParamClass as KPC


class MyKeyParamClass(KPC):
    KEY1: KPC = ('key1', 'param1')
    KEY2: KPC = ('key2', 'param2')

def main():
    print(f"{str(MyKeyParamClass)=}")
    print(f"{str(MyKeyParamClass.KEY1)=}")
    print(f"{str(MyKeyParamClass.KEY2.name)=}")
    print(f"{str(MyKeyParamClass.KEY1.desc)=}")
    print(f"{MyKeyParamClass.choices=}")
    print(f"{MyKeyParamClass.from_name("key1")=}")
    print(f"{MyKeyParamClass.get("KEY2")=}")
    print(f"{MyKeyParamClass.dict()=}")

if __name__ == '__main__':
    main()
