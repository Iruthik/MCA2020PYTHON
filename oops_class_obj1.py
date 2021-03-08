class students:
    def __init__(self,name,branch,marks):
        self.name = name
        self.branch = branch
        self.marks = marks
    def studentDisplay(self):
        print("Name:",self.name )
        print("Branch:", self.branch)
        print("Marks:", self.marks)
    def __del__(self):
        print("The above displayed record of" + self.name+" is deleted")

nam1 = input("Enter name:")
br1 = input("Enter Branch:")
mr1 = int(input("Enter marks:"))
nam2 = input("Enter name:")
br2 = input("Enter Branch:")
mr2 = int(input("Enter marks:"))
choice= input("Do you want to delet Student:")
if choice == 'y':
    stud1 = students(nam1, br1, mr1)
    stud2 = students(nam2, br2, mr2)
    stud1.studentDisplay()
    stud2.studentDisplay()

