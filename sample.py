def calculate(a, b, c=10):
    x = a + b
    y = x * c
    if y > 100:
        print("big value")
    else:
        print("small value")
    return y


def getdata(data):
    result = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            result.append(data[i])
    return result


def user_info(name, age):
    print("Name:", name)
    print("Age:", age)
    if age > 18:
        print("Adult")
    else:
        print("Minor")


def duplicate_function(x):
    return x * 2


def duplicate_function2(x):
    return x * 2


def read_file(filename):
    try:
        f = open(filename, "r")
        data = f.read()
        f.close()
        return data
    except Exception:
        print("Something went wrong")


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = getdata(numbers)
    print("Even numbers:", result)
    total = calculate(10, 20)
    user_info("John", 22)
    print("Total:", total)
    print("Duplicate:", duplicate_function(5))
    print("Duplicate:", duplicate_function2(5))
    read_file("test.txt")


if __name__ == "__main__":
    main()
