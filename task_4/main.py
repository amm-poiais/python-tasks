def first_capital(func):
    def func_wrapper():
        new_username = func()
        if new_username != "":
            new_username = new_username[0].upper() + new_username[1:]

        return new_username

    return func_wrapper


@first_capital
def get_username():
    username = input("Introduce yourself: ")
    return username


username = get_username()
print("Hello, {}".format(username))