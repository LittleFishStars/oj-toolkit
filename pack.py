import argparse
from pathlib import Path
from zipfile import ZipFile


def pid_of(problem_dir: Path, problem_root: Path) -> str:
    """由题目录相对路径拼出 pid：Problem/W1/D1/P1 -> W1D1P1（兼容旧 Problem/D1/P1 -> D1P1）"""
    return "".join(problem_dir.relative_to(problem_root).parts)


def is_day_dir(d: Path, child_marker="config.yaml") -> bool:
    """题目天目录：其子目录中存在含标记文件的题目目录（Problem 用 config.yaml，Solution 用参考解答 .py）"""
    if child_marker == "config.yaml":
        return d.is_dir() and any(p.is_dir() and (p / child_marker).exists() for p in d.iterdir())
    return d.is_dir() and any(p.is_dir() and any(p.glob(child_marker)) for p in d.iterdir())


def find_days(root: Path, child_marker: str = "config.yaml") -> list[Path]:
    return sorted(d for d in root.rglob("*") if is_day_dir(d, child_marker))


def match_days(all_days: list[Path], base_root: Path, args_days: list[str]) -> list[Path]:
    """按天名（D1）或完整相对名（W1D1）匹配目录，找不到的打印警告"""
    targets = []
    for day in args_days:
        matched = [d for d in all_days if d.name == day or "".join(d.relative_to(base_root).parts) == day]
        if not matched:
            print(f"警告: 找不到 {day}，跳过")
        targets.extend(matched)
    return targets


def add_problem(zf: ZipFile, problem_dir: Path, problem_root: Path):
    """把一道题的 testdata/config.yaml/problem.yaml/题面写入 zip（Hydro 格式）"""
    pid = pid_of(problem_dir, problem_root)

    testdata_dir = problem_dir / "testdata"
    if testdata_dir.is_dir():
        for td_file in sorted(testdata_dir.iterdir()):
            zf.write(td_file, f"{pid}/testdata/{td_file.name}")

    config_file = problem_dir / "config.yaml"
    if config_file.exists():
        zf.write(config_file, f"{pid}/testdata/config.yaml")

    problem_yaml = problem_dir / "problem.yaml"
    if problem_yaml.exists():
        zf.write(problem_yaml, f"{pid}/problem.yaml")

    for md_file in sorted(problem_dir.glob("problem_*.md")):
        zf.write(md_file, f"{pid}/{md_file.name}")


def pack_day(problem_root: Path, day_dir: Path):
    zip_path = day_dir / f"{day_dir.name}.zip"
    with ZipFile(zip_path, "w") as zf:
        for problem_dir in sorted(p for p in day_dir.iterdir() if p.is_dir()):
            add_problem(zf, problem_dir, problem_root)


def pack_week(problem_root: Path, week_dir: Path):
    """把一周内所有天的题目合并打包为 Problem/Wn/Wn.zip"""
    zip_path = week_dir / f"{week_dir.name}.zip"
    with ZipFile(zip_path, "w") as zf:
        for day_dir in sorted(d for d in week_dir.iterdir() if is_day_dir(d)):
            for problem_dir in sorted(p for p in day_dir.iterdir() if p.is_dir()):
                add_problem(zf, problem_dir, problem_root)


def main():
    parser = argparse.ArgumentParser(description="打包每日/每周题目")
    parser.add_argument("--day", nargs="*", metavar="D", help="要打包的天，如 --day D1 W1D2；不提供则打包全部天")
    parser.add_argument("--week", nargs="*", metavar="W", help="打包整周：--week W1 或 --week（不带参数=全部周）")
    args = parser.parse_args()

    if args.day and args.week is not None:
        parser.error("--day 与 --week 不能同时使用")

    root = Path(__file__).parent
    problem_root = root / "Problem"

    if args.week is not None:
        weeks = sorted(d for d in problem_root.iterdir() if d.is_dir())
        if args.week:
            weeks = match_days(weeks, problem_root, args.week)
        for week_dir in weeks:
            pack_week(problem_root, week_dir)
            print(f"已打包 {week_dir.name}.zip")
        return

    all_days = find_days(problem_root)
    targets = all_days if not args.day else match_days(all_days, problem_root, args.day)

    for day_dir in targets:
        pack_day(problem_root, day_dir)
        print(f"已打包 {day_dir.name}.zip")


if __name__ == "__main__":
    main()
