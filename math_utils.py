print("[math_utils] __name__ =", __name__)
print("inside math_utils")

def add(a, b):
    print("Inside math_utils add()")
    return a + b

def main():
    print("Inside math_utils main()")
    print(add(5,10))

if __name__ == "__main__":
    main()

print("out of math_utils")