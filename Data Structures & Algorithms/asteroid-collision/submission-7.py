class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        li = [asteroids[0]]
        for roid in asteroids[1:]:
            alive = True
            while li and li[-1] > 0 and roid < 0:
                if abs(li[-1]) < abs(roid):
                    li.pop()
                elif abs(li[-1]) == abs(roid):
                    li.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                li.append(roid)
        return li