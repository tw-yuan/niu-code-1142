import math

# 第一題：計算圓面積
print("=== 計算圓面積 ===")
radius = float(input("請輸入圓的半徑："))
area = radius ** 2 * math.pi
print(f"圓的半徑為 {radius}，面積為 {area:.4f}")

# 第二題：計算 BMI
print("\n=== 計算 BMI ===")
height_cm = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    status = "過低"
elif bmi <= 24:
    status = "適中"
else:
    status = "過高"

print(f"您的 BMI 為 {bmi:.2f}，體重{status}")
