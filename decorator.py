# Decorator Program

def dec1(func):
    def inner():
        print("#" * 30)
        func()
        print("#" * 30)
    return inner

def dec2(func):
    def inner():
        print("*" * 30)
        func()
        print("*" * 30)
    return inner

@dec1
@dec2
def printer():
    print("Welcom!!!")


printer()