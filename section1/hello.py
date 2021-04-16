def welcome(name: str) -> str:
    if name:
        return "Welcome " + name.title()
    return "Welcome"


def greeting(name: str) -> str:
    return "welcome " + name.title() if name else "Welcome"


print(welcome("john"))
print(3 / 5)
print(3 // 5)
print(greeting("leon"))
print("Pycharm lens mode")
