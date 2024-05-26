# with open("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

from os import write


with open("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-24/my_file.txt", mode="a") as file:
    file.write("\nNew text1.")