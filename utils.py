### COMMENTED OUT FOR NOW
def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    return a + b


def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


if __name__ == "__main__":
    print(greet("world"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
### MORE COMMENTED OUT FOR NOW