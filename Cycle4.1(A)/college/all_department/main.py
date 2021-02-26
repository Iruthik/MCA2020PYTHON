import college.all_department.cse
import college.all_department.it
un = input("Enter user name:")
pw = input("Enter password:")

college.all_department.it.admin(pw,un)
college.all_department.it.cabin(pw,un)
college.all_department.cse.admin(pw,un)
college.all_department.cse.cabin(pw,un)