import random
from abc import ABC, abstractmethod
from pathlib import Path


class Generator(ABC):
    """题目数据生成器基类。

    子类实现 generate_input() 和 generate_output()，然后实例化并调用 generate()，
    测试数据会写入当前目录下的 testdata/（须在题目目录内运行）。
    """

    @abstractmethod
    def generate_input(self) -> str:
        """返回一组输入（不含末尾换行）。可用 self._i 读取当前测例序号（从 0 开始）。"""
        ...

    @abstractmethod
    def generate_output(self, input_data: str) -> str:
        """根据输入计算标准答案（多行用 \n 连接，不含末尾换行）。"""
        ...

    def __init__(self, test_num: int):
        self.test_num = test_num

    def generate(self, clear: bool = True):
        """生成 testdata/ 下的 1.in/1.out ... N.in/N.out。

        - 以类名为随机种子：同一道题无论重新生成多少次，测例都完全一致；
        - clear=True 时先删除 testdata 里旧的 .in/.out，避免 test_num 变小后残留旧测例；
        - 每次调用 generate_input 前，self._i 自动置为当前序号（0 开始），
          子类可直接 `i = self._i` 实现固定边界测例 + 随机测例。
        """
        random.seed(type(self).__name__)
        testdata_dir = Path("./testdata")
        testdata_dir.mkdir(exist_ok=True)
        if clear:
            for old in list(testdata_dir.glob("*.in")) + list(testdata_dir.glob("*.out")):
                old.unlink()

        for index in range(1, self.test_num + 1):
            self._i = index - 1
            input_data = self.generate_input()
            output_data = self.generate_output(input_data)
            (testdata_dir / f"{index}.in").write_text(input_data + "\n")
            (testdata_dir / f"{index}.out").write_text(output_data + "\n" if output_data else "")
