from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n - 2, -1, -1):
            next_day = i + 1
            while next_day < n and temperatures[i] >= temperatures[next_day]:
                if answer[next_day] == 0:
                    break
                next_day += answer[next_day]

            if next_day < n and temperatures[i] < temperatures[next_day]:
                answer[i] = next_day - i

        return answer