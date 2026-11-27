"""Smart Calculator - a tiny command-line calculator used for a Git assignment."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Error: division by zero")
    return a / b


def modulo(a, b):
    return a % b


def main():
    print("Smart Calculator")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("10 % 3 =", modulo(10, 3))


if __name__ == "__main__":
    main()
