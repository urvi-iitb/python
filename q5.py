def max_marks(subject):
    return max(list, key = lambda x: x[subject])[subject]

def toppers(subject):
    marks = max_marks(subject)
    topper_names = []
    for student in list:
        if student[subject]==marks:
            topper_names.append(student["Name"])
    return topper_names


with open ("Marks.txt","r") as f:
    data = f.readlines()
list = []
for line in data:
    student_dict={}
    student = line.split(",")
    student_dict["Name"]=student[0]
    student_dict["Gender"]=student[1]
    student_dict["Roll_No"]= student[2]
    total = 0
    for i in range (3,len(student)-1):
        student_dict[student[i].split(":")[0]]= int(student[i].split(":")[1])
        total += int(student[i].split(":")[1])
    student_dict["Total"] = total
    student_dict["P/F"] = student[len(student)-1].rstrip()
    list.append(student_dict)
print(toppers("English")) #similarly for other subjects
print(toppers("Total"))