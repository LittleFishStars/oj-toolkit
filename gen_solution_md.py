import argparse
from pathlib import Path

from pack import find_days, match_days, pid_of


def gen_day(solution_root: Path, day_dir: Path):
    for problem_dir in sorted(day_dir.iterdir()):
        if not problem_dir.is_dir():
            continue
        pid = pid_of(problem_dir, solution_root)
        py_file = problem_dir / f"{pid}.py"
        md_file = problem_dir / "solution.md"

        if not py_file.exists():
            print(f"SKIP {problem_dir}: missing {pid}.py")
            continue

        py_code = py_file.read_text().rstrip("\n")
        md_file.write_text(f"Python\n```python\n{py_code}\n```\n")
        print(f"OK {md_file}")


def main():
    parser = argparse.ArgumentParser(description="生成每题 solution.md（Python）")
    parser.add_argument("--day", nargs="*", metavar="D", help="要生成的天，如 --day D1 W1D1；不提供则生成全部")
    args = parser.parse_args()

    root = Path(__file__).parent
    solution_root = root / "Solution"

    all_days = find_days(solution_root, child_marker="*.py")
    targets = all_days if not args.day else match_days(all_days, solution_root, args.day)

    for day_dir in targets:
        gen_day(solution_root, day_dir)


if __name__ == "__main__":
    main()
