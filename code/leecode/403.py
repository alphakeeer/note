class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        steps = dict()
        for stone in stones:
            steps[stone] = set()
        steps[0].add(0)
        for stone, ks in steps.items():
            for k in ks:
                if k-1 > 0 and stone+k-1 in steps:
                    steps[stone+k-1].add(k-1)
                if k > 0 and stone+k in steps:
                    steps[stone+k].add(k)
                if stone+k+1 in steps:
                    steps[stone+k+1].add(k+1)

        return len(steps[stones[-1]]) > 0


stones = [0, 1, 2, 3, 4, 8, 9, 11]
sol = Solution()
sol.canCross(stones)
