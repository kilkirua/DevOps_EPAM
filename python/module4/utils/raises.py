def raises(error):
    def wrapper(func):
        def return_error(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except:
                raise error
        return return_error
    return wrapper
