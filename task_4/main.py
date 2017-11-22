def first_capital(func):
    def func_wrapper():
        new_username = func().__str__()
        if new_username != "":
            new_username = new_username[0].upper() + new_username[1:]

        return new_username

    return func_wrapper


@first_capital
def get_str1():
    return ""


@first_capital
def get_str2():
    return "test_str"


@first_capital
def get_str3():
    return 43


@first_capital
def get_str4():
    return "Capital"


strings = [get_str1(), get_str2(), get_str3(), get_str4()]

for line in strings:
    print(line)
