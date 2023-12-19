#FIRST EXTRACTING DATA
with open ("Marks.txt","r") as f:
    data = f.readlines()
list = []
for line in data:
    student_dict={}
    student = line.split(",")
    student_dict["Name"]=student[0]
    student_dict["Gender"]=student[1]
    student_dict["Roll_No"]= student[2]
    student_dict[student[3].split(":")[0]]= int(student[3].split(":")[1]) #English
    student_dict[student[4].split(":")[0]]= int(student[4].split(":")[1]) #Maths
    student_dict[student[5].split(":")[0]]= int(student[5].split(":")[1]) #Physics
    student_dict[student[6].split(":")[0]]= int(student[6].split(":")[1]) #Chemistry
    student_dict[student[7].split(":")[0]]= int(student[7].split(":")[1]) #Biology
    student_dict["Total"]= student_dict["English"] + student_dict["Maths"]+student_dict["Physics"]+student_dict["Chemistry"]+student_dict["Biology"]
    student_dict["P/F"] = student[8].rstrip()
    list.append(student_dict)
max_total = 0
gold_medal=[]
max_english =0
english_toppers=[]
max_maths = 0 
maths_toppers =[]
max_physics = 0
phy_toppers=[]
max_chemistry=0
chem_toppers=[]
max_biology = 0
bio_toppers=[]
for st in list:
    if st["English"]>max_english:
        max_english=st["English"]
        english_toppers.clear()
        english_toppers.append(st["Name"])
    elif st["English"] ==max_english:
        english_toppers.append(st["Name"])
    
    if st["Maths"]>max_maths:
        max_maths=st["Maths"]
        maths_toppers.clear()
        maths_toppers.append(st["Name"])
    elif st["Maths"] ==max_maths:
        maths_toppers.append(st["Name"])

    if st["Physics"]>max_physics:
        max_physics=st["Physics"]
        phy_toppers.clear()
        phy_toppers.append(st["Name"])
    elif st["Physics"] ==max_physics:
        phy_toppers.append(st["Name"])

    if st["Chemistry"]>max_chemistry:
        max_chemistry=st["Chemistry"]
        chem_toppers.clear()
        chem_toppers.append(st["Name"])
    elif st["Chemistry"] ==max_chemistry:
        chem_toppers.append(st["Name"])

    if st["Biology"]>max_biology:
        max_biology=st["Biology"]
        bio_toppers.clear()
        bio_toppers.append(st["Name"])
    elif st["Biology"] ==max_biology:
        bio_toppers.append(st["Name"])

    if st["Total"]>max_total:
        max_total=st["Total"]
        gold_medal.clear()
        gold_medal.append(st["Name"])
    elif st["Total"] ==max_total:
        gold_medal.append(st["Name"])

print("Maximum marks scored:", max_total)
print("Gold Medalists:")
for i in gold_medal:
    print(i)

print("Maximum marks in English:", max_english)
print("English Toppers:")
for i in english_toppers:
    print(i)

print("Maximum marks in Maths:", max_maths)
print("Maths Toppers:")
for i in maths_toppers:
    print(i)

print("Maximum marks in Physics:", max_physics)
print("Physics Toppers:")
for i in phy_toppers:
    print(i)

print("Maximum marks in Chemistry:", max_chemistry)
print("Chemistry Toppers:")
for i in chem_toppers:
    print(i)

print("Maximum marks in biology:", max_biology)
print("Biology Toppers:")
for i in bio_toppers:
    print(i)