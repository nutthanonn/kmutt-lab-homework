DEFAULT = object()
def foo(param=DEFAULT):
    if param is DEFAULT:
        print("Not paramiter")
    else:
        print("Hello")
foo()
foo("")