#Zad 1
class Point:
    x:int = 0
    y:int = 0
    
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str: #Zad 2
        return f'Point({self.x},{self.y})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __mul__(self, m) -> "Point": #Zad 3
        return Point(self.x *m, self.y *m)
    
    def __eq__(self, __o: object) -> bool: #Zad 4
        if type(__o) == type(self):
            if(self.x == __o.x and self.y == __o.y):
                return True
        return False
           
p1 = Point()
p2 = Point(1)
p3 = Point(y=2)
p4 = Point(1,2)
print([p1,p2,p3,p4])
print(p1)

#Zad 3
print(p2)
p2 * 2
print(p2)
p2 *= 2
print(p2)

#Zad 4
p6 = Point()
print(p1==(1,2))
print(p1==p2)
print(p1==p6)

#Zad 5
class Polygon:
    points:list[Point]
    
    def __init__(self) -> None:
        self.points = []
        
    def add_point(self, point: Point) -> None:
        self.points.append(point)
        
    def __str__(self) -> str: #Zad 6
        return f'Polygon{self.points}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __getitem__(self, items) -> int|slice:
        try:
            return self.points[items]
        except TypeError: 
            print("Błędna wartość indexu")
            return self.points
    
pol1 = Polygon()
print(pol1)
pol1.add_point(p2)
print(pol1)

#Zad 7
pol1.add_point(p1)
pol1.add_point(p3)
pol1.add_point(p4)
pol1.add_point(p6)
print(pol1)
print(pol1[1])
print(pol1[:3])
print(pol1[::2])
print(pol1["ValueError"])
print(pol1[p1]) 
    