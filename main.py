# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Alternate way

#total_height = sum(student_heights)
#print(total_height)
#total_count = len(student_heights)
#print(total_count)

#Look what's under the hood of sum and length

#sum function within list
total_height_value = 0
for height in student_heights:
  total_height_value = height + total_height_value
print(total_height_value)

#Length function within list
number_of_student_count = 0
for count in student_heights:
  number_of_student_count = number_of_student_count +1
print(number_of_student_count)

average = round(total_height_value/number_of_student_count)
print(average)