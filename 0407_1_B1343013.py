# 基本題：使用巢狀 for/in 迴圈畫聖誕樹
height = int(input("請輸入樹葉層的高度："))

# 等腰三角形樹葉（用 *）
for i in range(1, height + 1):
    for s in range(height - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

# 長方形樹幹（用 #，寬度 3，高度 3）
trunk_width = 3
trunk_height = 3
for t in range(trunk_height):
    for s in range(height - trunk_width // 2 - 1):
        print(" ", end="")
    for h in range(trunk_width):
        print("#", end="")
    print()

# 進階題：兩段式聖誕樹，附裝飾
print("\n=== 進階：兩段式聖誕樹 ===\n")

upper = 4
lower = 5
max_width = 2 * (upper + lower) - 1
half = max_width // 2

# 上層三角形（較小，4 層）
for i in range(1, upper + 1):
    row = ""
    for s in range(half - (i - 1)):
        row = row + " "
    for j in range(2 * i - 1):
        # 裝飾規則：偶數列且奇數位置放 o
        if i % 2 == 0 and j % 2 == 1:
            row = row + "o"
        else:
            row = row + "*"
    print(row)

# 下層三角形（較大，5 層）
for i in range(1, lower + 1):
    row = ""
    for s in range(half - (upper + i - 1)):
        row = row + " "
    w = 2 * (upper + i) - 1
    for j in range(w):
        # 裝飾規則：偶數列且每隔 3 個位置放 @，奇數列每隔 4 個位置放 +
        if i % 2 == 0 and j % 3 == 1:
            row = row + "@"
        elif i % 2 == 1 and j % 4 == 2:
            row = row + "+"
        else:
            row = row + "*"
    print(row)

# 樹幹（# 組成，寬度 3，高度 3，置中）
for t in range(3):
    row = ""
    for s in range(half - 1):
        row = row + " "
    for h in range(3):
        row = row + "#"
    print(row)

print("\n裝飾規則說明：")
print("  上層：偶數列的奇數位置以 o 裝飾")
print("  下層：偶數列每隔 3 格以 @ 裝飾，奇數列每隔 4 格以 + 裝飾")
