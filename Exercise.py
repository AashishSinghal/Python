print("Twinkle Twinle little stars,\n\tHow i wonder what you are,"
      "\n\t\tUp above the world so high,\n\tlike a diamond in the sky,"
      "\nTwinkle Twinkle little stars,\n\tHow i wonder what you are\n")


import sys
print("\nPython Version")
print(sys.version)
print("Version Info")
print(sys.version_info)


import datetime
now = datetime.datetime.now()
print("\n\nCurrent Date & Time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print("\n")


'''
f_name = input("Enter First Name: ")
l_name = input("Enter Last Name: ")
print("Hello ",l_name,f_name," !")
print("\n")
'''

"""values = input("Input some comma separated numbers : ")
list = values.split(",")
tuple =tuple(list)
print("List : ",list)
print("Tuple : ",tuple)

print("\n")"""

'''r = int(input("Input the radius of a Circle : "))
area = float(3.14)*r*r
print("Area of The Circle with radius ",r," is ",area)

print("\n")'''

'''f_name = input("Input a filename with its extension : ")
ext = f_name.split(".")
print("The extension of file is :",ext[1])

print("\n")'''


'''
colors = input("Enter names of colors separated by commas : ")
color_list = colors.split(", ")
print("The first and the lsat color respectively are : ", color_list[0], " & ",  color_list[-1])
print("\n")
'''


'''
exam_st_date = input("Enter Date Separated by a forward slash: ")
exam_st_date = exam_st_date.split("/")
print("The Examination will start from : ", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])
print("\n")
'''


'''
d, m, y = input("Enter the date : ").split()
print("The Exam will Start From: ", d, "/", m, "/", y)
'''

'''
# Python program showing how to 
# multiple input using split 

# taking two inputs at a time 
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time 
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x) 
'''


# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a date: ").split()))
print("List of students: ", x)


