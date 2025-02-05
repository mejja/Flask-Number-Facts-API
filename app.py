from flask import Flask, request, jsonify
import math
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Local Fun Facts (Avoiding slow API calls)
FUN_FACTS = {
    0: "The only number that can't be represented in Roman numerals.",
    1: "1 is not a prime number and is the loneliest number.",
    2: "2 is the only even prime number.",
    3: "3 is the first odd prime number.",
    4: "Only one number spelled with the same number of letters as itself.",
    5: "In Thailand, '555' Is Hilarious as 5 is pronounched as ha hence 555=hahaha.",
    6: "6 is a perfect number (sum of divisors = itself).",
    7: "7 is considered a lucky number in many cultures.",
    9: "9 is considered a 'magic' number because its multiples sum to 9.",
    10: "10 is the base of the decimal number system.",
    12: "12 is the smallest abundant number.",
    13: "13 is considered an unlucky number in many cultures.",
    21: "21 is the product of the first two consecutive triangular numbers.",
    23: "23 is the first prime number in which both digits are prime numbers.",
    27: "27 is the cube of 3.",
    59: "59 is the number of stellations of an icosahedron.",
    69: "(6 × 9) + (6 + 9) = 69",
    71: "71 is the mirror image of the number 17.",
    371: "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.",
    1000: "1000 is the smallest number with one thousand divisors."
}

# ThreadPool for fast execution
executor = ThreadPoolExecutor(max_workers=4)


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Validate input
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": "Not a valid number"}), 400

    num = int(number)

    # Execute all calculations in parallel
    future_prime = executor.submit(is_prime, num)
    future_perfect = executor.submit(is_perfect_square, num)
    future_properties = executor.submit(get_properties, num)
    future_digit_sum = executor.submit(get_digit_sum, num)
    future_fun_fact = executor.submit(get_fun_fact, num)

    response = {
        "number": num,
        "is_prime": future_prime.result(),
        "is_perfect": future_perfect.result(),
        "properties": future_properties.result(),
        "digit_sum": future_digit_sum.result(),
        "fun_fact": future_fun_fact.result()
    }

    return jsonify(response)


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect_square(n):
    """Check if a number is a perfect square"""
    return int(math.sqrt(n)) ** 2 == n


def get_properties(n):
    """Determine number properties (odd/even, Armstrong, Happy)"""
    properties = ["odd" if n % 2 else "even"]
    if is_armstrong(n):
        properties.append("armstrong")
    if is_happy(n):
        properties.append("happy")
    return properties


def is_armstrong(n):
    """Check if a number is an Armstrong number"""
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n


def is_happy(n):
    """Check if a number is a happy number"""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def get_digit_sum(n):
    """Calculate the sum of digits of a number"""
    return sum(map(int, str(n)))


def get_fun_fact(n):
    """Fetch a fun fact (Uses local database for speed)"""
    if is_happy(n):
        return f"{n} is a happy number!"
    return FUN_FACTS.get(n, f"{n} is an interesting number!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
