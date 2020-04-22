from time import sleep
def delay(func):
    def return_str(*args, **kwargs):
        """Test docstring"""
        sleep(3)
        res = func(*args, **kwargs)
        return res
    return return_str
