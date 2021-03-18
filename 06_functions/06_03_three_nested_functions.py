def func_1():
    print(name)

    def func_2():
        print(name)
        name1 = 'danny'

        def func_3():
            print(name)
            print(name1)
            name2 = 'renee'
            return "This is from func_3"

        from_3 = func_3()
        print(from_3)
        return "This is from func_2"

    from_2 = func_2()
    print(from_2)
    return "This is from func_1"

name = 'jim'
from_1 = func_1()
print(from_1)

