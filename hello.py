def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(greet("GitHub Actions"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 is even: {is_even(4)}")