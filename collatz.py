def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    start = 27
    sequence = collatz_sequence(start)
    for number in sequence:
        print(number)
    steps = len(sequence) - 1
    print(f"Steps: {steps}")


if __name__ == "__main__":
    main()
