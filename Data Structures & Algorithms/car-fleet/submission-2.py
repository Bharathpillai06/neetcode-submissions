class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed), reverse=True)
        arrival = [(target - pairs[0][0])/pairs[0][1]]
        groups = 1
        for x in range(len(pairs)):
            if (target - pairs[x][0])/pairs[x][1] > arrival[0]:
                groups += 1
                arrival[0] =(target - pairs[x][0])/pairs[x][1]                
        return groups


        