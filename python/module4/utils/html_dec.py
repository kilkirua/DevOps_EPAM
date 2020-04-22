def underline(func):
    def return_str(*args, **kwargs):
        res = func(*args, **kwargs)
        return "<u>" + str(res) + "</u>"
    return return_str

def bold(func):
    def return_str(*args, **kwargs):
        res = func(*args, **kwargs)
        return "<b>" + str(res) + "</b>"
    return return_str

def italic(func):
    def return_str(*args, **kwargs):
        res = func(*args, **kwargs)
        return "<i>" + str(res) + "</i>"
    return return_str
