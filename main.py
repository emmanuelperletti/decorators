from log import log


@log
def func(param,*args,**kwargs) -> None:
    """ fonction bateau, prenant des arguments et les retournant"""
    print(f"Le parametre positionnel = '{param}', les arguments restant (*args) = {args} et les arguments nommés (**kwargs) = {kwargs}")
    return (param,args,kwargs)   


if __name__ == "__main__":
    func("Hello", "test", name="toto")