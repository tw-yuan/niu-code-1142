# 基本題：字典的建立與資料處理
print("=== 基本題：字典的建立與資料處理 ===")

# 使用大括號 {} 建立 student1
student1 = {
    "name": "John",
    "age": 21,
    "grades": [88, 91, 89],
    "major": "Electrical Engineering"
}

# 使用 dict() 建立 student2
student2 = dict(
    name="Brian",
    age=20,
    grades=[93, 89, 92],
    major="Computer Science"
)

student1["average"] = sum(student1["grades"]) / len(student1["grades"])
student2["average"] = sum(student2["grades"]) / len(student2["grades"])

print(f"學生姓名：{student1['name']}")
print(f"主修科系：{student1['major']}")
print(f"平均成績：{student1['average']:.2f}")
print()

print(f"學生姓名：{student2['name']}")
print(f"主修科系：{student2['major']}")
print(f"平均成績：{student2['average']:.2f}")

# 進階題：多名學生總成績統計
print("\n=== 進階題：多名學生總成績統計 ===")

students = {
    "Amy": {"grades": [90, 85, 88], "age": 18},
    "Ben": {"grades": [70, 78, 80], "age": 20},
    "Cara": {"grades": [95, 92, 98], "age": 19}
}

for name in students:
    grades = students[name]["grades"]
    students[name]["average"] = sum(grades) / len(grades)

highest_name = ""
highest_average = 0

for name in students:
    if students[name]["average"] > highest_average:
        highest_name = name
        highest_average = students[name]["average"]

print(f"成績最高的學生：{highest_name}")
print(f"最高平均成績：{highest_average:.2f}")
print()

sorted_students = sorted(
    students.items(),
    key=lambda item: item[1]["average"],
    reverse=True
)

print("依平均成績由高到低排序：")
for name, info in sorted_students:
    print(f"{name}：平均成績 {info['average']:.2f}，年齡 {info['age']}")
