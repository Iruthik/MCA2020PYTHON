import Graphics.Rectangle
import Graphics.Circle
import Graphics.Three_d_graphics.Cuboid
import Graphics.Three_d_graphics.Sphere
print("RECTANGLE\n\n")

length = int(input("Enter Length of Rectangle:"))
bredth = int(input("Enter bredth Rectangle:"))
print("\nArea of Rectangle:"+str(Graphics.Rectangle.area(length,bredth))+"cm^2")
print("\nPerimeter of Rectangle:"+str(Graphics.Rectangle.perimeter(length,bredth))+"cm")

print("\n\nCIRCLE AND SPHERE\n\n")
radius = int(input("\nEnter Radius:"))
print("\nArea of circle:" + str(Graphics.Circle.area(radius)) + "cm^2")
print("\nCircumference of circle:" + str(Graphics.Circle.perimeter(radius)) + "cm")
print("\nVolume of Sphere:" + str(Graphics.Three_d_graphics.Sphere.volume(radius)) + "cm^3")
print("\nSurface area of Sphere:" + str(Graphics.Three_d_graphics.Sphere.area(radius)) + "cm^2")

print("\n\nCUBOID\n\n")
leng = int(input("\nEnter length of Cuboid:"))
bred = int(input("\nEnter Bredth of Cuboid:"))
heig = int(input("\nEnter Height of Cuboid:"))
print("\nSurface area of Cuboid:" + str(Graphics.Three_d_graphics.Cuboid.s_area(leng,bred,heig)) + "cm^2")
print("\nPerimeter of Cuboid:" + str(Graphics.Three_d_graphics.Cuboid.perimeter(leng,bred,heig)) + "cm")
