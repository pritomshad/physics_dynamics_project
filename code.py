import math
import turtle
#lets work with 3d space
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def scaler_length(self):
        return math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
    def print_vector(self):
        print(self.x,"i +",self.y, "j +", self.z, "k")

class vector_operations:
    def scaler_mul(scaler_value : int, v : vector) :
        return vector(scaler_value*v1.x, scaler_value*v1.y, scaler_value*v1.z)
        
    def add(v1 : vector, v2 : vector):
        return vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)
        
    def subtraction(v1 : vector, v2 : vector):
        return vector(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z)
        
    def dot_product(v1 : vector, v2 : vector):
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
        
    def cross_product(v1 : vector, v2 : vector):
        a = v1.x ; b = v1.y ; c = v1.z
        x = v2.x ; y = v2.y ; z = v2.z
        return vector(b*z-c*y, c*x-a*z, a*y-b*x)
r1 = vector(1,2,3)
r2 = vector(5,2,3)
print(r1.scaler_length())
ada = vector_operations.add(r1,r2)
ada.print_vector()
