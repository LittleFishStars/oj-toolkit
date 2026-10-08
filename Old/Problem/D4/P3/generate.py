from generator import Generator
import random

def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

MAX_P = 10000
_primes = primes_up_to(MAX_P)

class D4P3(Generator):
    def generate_input(self) -> str:
        p = random.choice(_primes)
        return str(p)

    def generate_output(self, input_data: str) -> str:
        p = int(input_data.strip())
        return str(_primes.index(p) + 1)

problem_generator = D4P3(test_num=10)
problem_generator.generate()
