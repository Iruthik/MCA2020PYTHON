# 1.  Create  Rectangle  class  with  attributes  length  and  breadth  and  methods  to  find  area  and
# perimeter. Compare two Rectangle objects by their area

class rectangle:
    def __init__(self,length,bredth):
        self.length =length
        self.bredth = bredth
    def area(self):
        area = self.length * self.bredth
        print("Area of Rectangle: "+str(area))
    def perimeter(self):
        peri_meter = 2*(self.length+self.bredth)
        print("Perimeter of Rectangle: "+str(peri_meter))

leng1 = int(input("Enter length of First Rectangle:"))
bred1 = int(input("Enter bredth of First Rectangle:"))
leng2 = int(input("Enter length of Second Rectangle:"))
bred2 = int(input("Enter bredth of Second rectangle:"))

rect1 = rectangle(leng1,bred1)
rect2 = rectangle(leng2,bred2)
print("FIRST RECTANGLE\n\n")
rect1.area()
rect1.perimeter()
print("\n\nSECOND RECTANGLE\n\n")
rect2.area()
rect2.perimeter()
if rect1.length * rect1.bredth < rect2.length * rect2.bredth:
    print("Area of second rectangle is greater")
elif  rect1.length * rect1.bredth > rect2.length * rect2.bredth:
    print("Area of first rectangle is greater")
else:
    print("Both are samee")







