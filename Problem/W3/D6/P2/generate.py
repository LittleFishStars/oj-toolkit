from generator import Generator
import random


class ProblemW3D6P2(Generator):
    def generate_input(self) -> str:
        i = self._i
        fixed = [
            "the cat and the dog and the bird",
            "a a b",
            "hello",
            "x y z",
            "aa aa bb bb cc",
        ]
        if i < len(fixed):
            return fixed[i]
        pool = ["apple", "the", "and", "cat", "dog", "bird", "sun", "sea", "run", "go"]
        words = [random.choice(pool) for _ in range(random.randint(1, 30))]
        return " ".join(words)

    def generate_output(self, input_data: str) -> str:
        words = input_data.split()
        counts = {}
        for w in words:
            if w in counts:
                counts[w] += 1
            else:
                counts[w] = 1
        items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        return "\n".join(f"{w} {c}" for w, c in items)


problem_generator = ProblemW3D6P2(test_num=10)
problem_generator.generate()
