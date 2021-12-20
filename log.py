from time import ctime
def log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt","a") as f:
            f.write(f"{ctime()}:{func.__name__} called with params ({','.join(args)}) and {kwargs}\n")
        val = func(*args,**kwargs)
        return val
    return wrapper