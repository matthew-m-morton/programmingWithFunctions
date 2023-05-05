import random as rd

def main():
    numbers = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        numbers.append(round(rd.uniform(0, 100), 1))

if __name__ == "__main__":
    main()