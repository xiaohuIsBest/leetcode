class Solution:

    def combine(self, n: int, k: int):
        result = []   #存放结果
        path = []     #存放路径
        def backtracking(n, k, startIndex):
            if k == len(path):
                result.append(path[:])
                return
            for i in range(startIndex, n+1):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()  # 回溯，撤销处理结果
        backtracking(n, k, 1)
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(5, 2))
