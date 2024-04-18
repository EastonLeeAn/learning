# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2.combine
   Description :
   Author :       lizhenhui
   date：          2024/3/24
-------------------------------------------------
   Change Activity:
                   2024/3/24:
-------------------------------------------------
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

a = Solution()
print(a.combine(4,2))