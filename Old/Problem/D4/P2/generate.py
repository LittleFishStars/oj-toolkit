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

class D4P2(Generator):
    def generate_input(self) -> str:
        n = random.randint(10, 1000)
        return str(n)

    def generate_output(self, input_data: str) -> str:
        n = int(input_data.strip())
        return ' '.join(map(str, primes_up_to(n)))

problem_generator = D4P2(test_num=10)
problem_generator.generate()
