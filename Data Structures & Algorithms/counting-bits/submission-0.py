class Solution:
    def countBits(self, n: int) -> List[int]:
        li = []
        for x in range(n + 1):
            li.append(x.bit_count())
        return li