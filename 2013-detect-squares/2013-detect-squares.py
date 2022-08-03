class DetectSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) not in self.points:
            self.points[(x, y)] = 0
        self.points[(x, y)] += 1
        

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        result = 0
        for (x2, y2), c2 in self.points.items():
            # The slope has to be 1 for the two points
            # to be diagonal of the square. Also, the points cannot
            # have any common X or Y
            if (abs(x2-x1) != abs(y2 - y1)) or x1 == x2 or y1 == y2:
                continue

            # Square found 
            if (x1, y2) in self.points and (x2, y1) in self.points:
                result += c2 * self.points[(x1, y2)] * self.points[(x2, y1)] 
        return result
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)