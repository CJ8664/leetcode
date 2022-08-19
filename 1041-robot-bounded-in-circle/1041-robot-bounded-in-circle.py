class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        turns = {
            (0, 1): ((-1, 0), (1, 0)),
            (0, -1): ((1, 0), (-1, 0)),
            (1, 0): ((0, 1), (0, -1)),
            (-1, 0): ((0, -1), (0, 1)),
        }
        
        dir, pos = (0, 1), (0, 0)
        
       
        for ins in instructions:
            if ins == "G":
                pos = (dir[0] + pos[0], dir[1] + pos[1])
            if ins == "L":
                dir = turns[dir][0]
            if ins == "R":
                dir = turns[dir][1]
            
        return pos == (0,0) or dir != (0, 1)
                
            
        