class Circle:
    seqNumber = 1
    def __init__(self, radius = 0.0, color = "red"):
        self.radius = radius
        self.color = color
        self.circleId = "CIR_" + f"{Circle.seqNumber}"
        Circle.seqNumber += 1
    
    @property
    def getRadius(self):
        return self.radius
    
    @property
    def getColor(self):
        return self.color
    
    @property
    def getCircleId(self):
        return self.circleId
    
   
    def getPerimeter(self):
        return self.radius * 2 * 3.14
    
   
    def getArea(self):
        return self.radius * self.radius * 3.14
    
    def __str__(self):
        return f"Circle Id : {self.circleId} \tRadius : {self.radius} \tColor : {self.color} \tPerimeter : {self.getPerimeter()} \tArea : {self.getArea()}"

    def __del__(self):
         className = self.__class__.__name__
