# 基本題：分數等第判斷
score = int(input("請輸入分數 (0~100)："))

if score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C+"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"分數 {score} 的等第為：{grade}")

# 進階題：判斷是否及格，以及等第分數的百分制範圍
if score >= 60:
    print("判定：及格")
else:
    print("判定：不及格")

grade_ranges = {
    "A":  "90 ~ 100",
    "B+": "85 ~ 89",
    "B":  "80 ~ 84",
    "C+": "70 ~ 79",
    "C":  "60 ~ 69",
    "F":  "0 ~ 59",
}
print(f"等第 {grade} 的百分制分數範圍為：{grade_ranges[grade]}")
