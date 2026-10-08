from generator import Generator
import random

def nth_prime(n: int) -> int:
    if n < 1:
        return 0
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1]

class D4P1(Generator):
    def generate_input(self) -> str:
        n = random.randint(1, 10000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data.strip())
        return str(nth_prime(n))

problem_generator = D4P1(test_num=10)
problem_generator.generate()
