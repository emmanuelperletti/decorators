from time import ctime, time


def log(func):
    """ fonction de log """
    def wrapper(*args, **kwargs):
        t = time()
        val = func(*args, **kwargs)
        with open("log.txt", "a") as f:
            f.write(
                f"{ctime()}:{func.__module__+'.'+func.__name__} called with params ({','.join(args)}) and {kwargs} -> returned:{val} in {time()-t} seconds\n"
            )
        return val

    return wrapper
