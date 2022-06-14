studentList = {
    "123":["Tong","IC"],
    "456":["Chung","CSIE"],
    "789":["Light","ASIE"],
    "321":["Chu","DAB"],
    "654":["Wu","FDD"]
}

inp = input("輸入查詢學號為:")

print(f"學生資料為:{inp} {studentList[inp][0]} {studentList[inp][1]}")