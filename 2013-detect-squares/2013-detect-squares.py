class DetectSquares:

    def __init__(self):
        self.xyx_pts = {}
        

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        if p not in self.xyx_pts:
            self.xyx_pts[p] = 0
        self.xyx_pts[p] += 1
        

    def count(self, point: List[int]) -> int:
        result = 0
        x1, y1 = point[0], point[1]
        for (x2, y2), c in self.xyx_pts.items():
            if (abs(x1-x2) != abs(y1-y2)) or (x1 == x2 and y1 == y2):
                continue
            if x2 > x1:
                x3, y3 = x1, y2
                x4, y4 = x2, y1
            else:
                x3, y3 = x2, y1
                x4, y4 = x1, y2
            if (x3, y3) in self.xyx_pts and (x4, y4) in self.xyx_pts:
                result += c * self.xyx_pts[(x3, y3)] * self.xyx_pts[(x4, y4)]
        return result
            
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)