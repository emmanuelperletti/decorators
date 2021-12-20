from log import log


@log
def func(param,*args,**kwargs) -> None:
    """ dummy function printing parameters and returning them """
    print(f"positionnal argument = '{param}', remaining arguments (*args) = {args} and keyword arguments (**kwargs) = {kwargs}")
    return (param,args,kwargs)   


if __name__ == "__main__":
    func("positionnal_arg1", "remaining_arg1", arg1="named_arg1")