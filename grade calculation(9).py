marks = []
for i in range(1,6):
    mark = float(input(f"enter marks for subject{i}:"))
    marks.append(mark)

#calculate total and percentage
total_marks = sum(marks)
percentage = (total_marks/500)*100 #assuming each subject out of 100

#determind grade
if percentage>=80:
    grade='a'
elif percentage>=70:
    grade='b'
elif percentage>=60:
    grade='c'
elif percentage>=40:
    grade='d'
else:
    grade='e'

#display result
print("\n------result------")
print(f"total marks:{total_marks}/500")
print(f"percentage:{percentage:.2f}%")
print(f"grade:{grade}")
