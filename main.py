from log import log


@log
def func(chaine: str,*args,**kwargs) -> None:
    print(f"La chaine {chaine}")   


if __name__ == "__main__":
    func("Hello", "test", name="toto")