import time
import sys
sys.set_int_max_str_digits(0)

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    number = 400000
    print(f"Calculating factorial of {number}...")
    start_time = time.time()
    factorial_result = calculate_factorial(number)
    end_time = time.time()
    print(f"Factorial of {number} is {factorial_result}")
    print(f"Time taken: {end_time - start_time} seconds")
