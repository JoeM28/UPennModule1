print("[app] __name__ =", __name__)
import math_utils

def greet(name):
    print(f"Hello, {name}!")

def main():
    print("Inside app main()")
    greet("Alice")
    result = math_utils.add(10, 20)
    print("10 + 20 =", result)

if __name__ == "__main__":
    main()