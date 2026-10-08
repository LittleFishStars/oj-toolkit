"""生成每天题目目录下的 README.md（当日题目简介）。

用法：
    uv run python gen_day_readme.py            # 生成全部天
    uv run python gen_day_readme.py W1D1       # 只生成指定天

天目录下的 problem.yaml 只有题目标题和标签，没有天的主题信息，
所以每天的一句话简介维护在本文件的 DAY_INTRO 里，新增天数时补一行即可。
"""
import argparse
from pathlib import Path

DAY_INTRO = {
    "D1": ("输出与输入入门", "认识 print 与 input：从 Hello World 开始，学会固定输出、读入数据，并用 f-string 拼出第一句问候。"),
    "D2": ("输入与运算", "练习整数与小数的输入和四则运算，掌握整除 // 与取余 %，学会用 f-string 保留指定位小数。"),
    "D3": ("分支语句基础", "if/else 二选一：用比较运算和取余写出条件判断，解决年龄、奇偶、最值和简易计算器问题。"),
    "D4": ("多分支与逻辑运算", "elif 多分支链与 and/or 逻辑组合，处理成绩等级、闰年、三角形类型和 BMI 这类多条件场景。"),
    "D5": ("分支与数据类型综合", "把字符串、列表、元组、字典请进 if 里：切片比较回文、sorted 排序去重、in 判季节、字典做查询。"),
    "D6": ("综合挑战", "小型实战：读题 + 把规则翻译成条件。石头剪刀布、字符统计、日期合法性、分段计费，难度逐题递进。"),
    "D7": ("数据类型大综合", "一题一个数据类型收官战：元组解包交换、列表内置函数、集合交集、布尔逻辑与多分支定价。"),
}


def parse_problem_yaml(path: Path) -> dict:
    info = {"title": "", "tags": []}
    for line in path.read_text().splitlines():
        if line.startswith("title:"):
            info["title"] = line.split(":", 1)[1].strip()
        elif line.startswith("- ") and not line.startswith("---"):
            info["tags"].append(line[2:].strip())
    return info


def gen_day_readme(day_dir: Path, problem_root: Path) -> bool:
    day_name = day_dir.name
    if day_name not in DAY_INTRO:
        print(f"SKIP {day_dir}: DAY_INTRO 中没有 {day_name} 的主题信息")
        return False

    week_name = day_dir.parent.name
    day_id = f"{week_name}{day_name}"  # 如 W1D1
    title, intro = DAY_INTRO[day_name]
    rows = []
    for problem_dir in sorted(p for p in day_dir.iterdir() if p.is_dir()):
        yaml_path = problem_dir / "problem.yaml"
        if not yaml_path.exists():
            continue
        info = parse_problem_yaml(yaml_path)
        pid = "".join(problem_dir.relative_to(problem_root).parts)
        rows.append((pid, info["title"], "、".join(info["tags"])))

    lines = [
        f"# {day_id} {title}",
        "",
        intro,
        "",
        f"本日共 {len(rows)} 题，均只允许使用 Python 提交（100ms / 10MB）。参考解答见 `Solution/` 对应目录。",
        "",
        "| 题号 | 题目 | 考查点 |",
        "| --- | --- | --- |",
    ]
    lines.extend(f"| {pid} | {t} | {tags} |" for pid, t, tags in rows)
    lines.append("")

    (day_dir / "README.md").write_text("\n".join(lines))
    print(f"OK {day_dir / 'README.md'}")
    return True


def main():
    parser = argparse.ArgumentParser(description="生成每天题目目录的 README.md 简介")
    parser.add_argument("--day", nargs="*", metavar="D", help="如 --day W1D1；不提供则生成全部")
    args = parser.parse_args()

    root = Path(__file__).parent
    problem_root = root / "Problem"
    day_dirs = sorted(d for d in problem_root.rglob("D*") if d.is_dir() and (d / "P1").exists())
    if args.day:
        day_dirs = [d for d in day_dirs if "".join(d.relative_to(problem_root).parts) in args.day]

    for day_dir in day_dirs:
        gen_day_readme(day_dir, problem_root)


if __name__ == "__main__":
    main()
