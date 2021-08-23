class Node:
    def __str__(self):
        return f"""<start: {self.start}, end: {self.end} total: {self.total}""" + \
               f", count: {self.count}>"

    def __init__(self, start: int, end: int, X: List[int]) -> None:
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None
        self.X = X

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid, self.X)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end, self.X)
        return self._right

    def update(self, i: int, j: int, val: int) -> int:
        # print(f"\t\t# update(i={i}, j={j}, val={val})")
        # print("\t\t", self)
        # print(f"\t\t left: {self.left}")
        # print(f"\t\t right: {self.right}")
        if i >= j:
            # print(f"\t\ti: {i} >= j: {j} \n\t\treturn 0")
            return 0
        if self.start == i and self.end == j:
            # print(f"\t\tcount: {self.count} += val: {val} == {self.count +val}")
            self.count += val
        else:
            # print(f"\t\tmid = {self.mid} i = {i} j = {j}")
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            # print(f"\t\tcount: {self.count} > 0")
            # print(f"\t\ttotal: {self.total} = self.X[{self.end}]: {self.X[self.end]} - " + \
            #      f"self.X[{self.start}]: {self.X[self.start]} == " + \
            #     f"{self.X[self.end] - self.X[self.start]}"
            #      )
            self.total = self.X[self.end] - self.X[self.start]
        else:
            # print(f"\t\ttotal: {self.total} = self.left.total: {self.left.total} + " + \
            #  f"self.right.total: {self.right.total} == " + \
            # f"{self.left.total + self.right.total}"
            #  )
            self.total = self.left.total + self.right.total
        # print("\t\t", self)
        # print(f"\t\t left: {self.left}")
        # print(f"\t\t right: {self.right}")
        # print(f"\t\treturn total={self.total}")
        return self.total


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        events = []

        X = set()
        for x1, y1, x2, y2 in rectangles:
            if (x1 < x2) and (y1 < y2):
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
                X.add(x1)
                X.add(x2)
        events.sort()

        X = sorted(X)
        # print("X ", X)
        x_index = {x: i for i, x in enumerate(X)}
        # print("x_index ", x_index)
        active = Node(0, len(X) - 1, X)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]
        # print(active)
        for y, typ, x1, x2 in events:
            # print(f"# event y: {y} typ: {typ} x1: {x1} x2: {x2}")
            # print(f"\tcur_x_sum {cur_x_sum} cur_y {cur_y}")
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(x_index[x1], x_index[x2], typ)
            # print(f"\t{active.left}, {active.right}\n\t ans {ans}")
            cur_y = y

        return ans % (10 ** 9 + 7)