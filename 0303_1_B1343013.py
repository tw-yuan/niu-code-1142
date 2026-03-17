# 作業 0303-1 基本題
# (1) 將 A, B, C, D, E 分別設定為 23, 5, 74, 12, 61
A, B, C, D, E = 23, 5, 74, 12, 61

# (2) 依序交換
# 將 B 與 D 交換
B, D = D, B
# 將 A 與 D 交換
A, D = D, A
# 將 C 與 B 交換
C, B = B, C
# 將 E 與 A 交換
E, A = A, E

# (3) 顯示多次交換後，目前 A, B, C, D, E 的值
print("多次交換後，A, B, C, D, E 的值為：")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")
print(f"E = {E}")

# 進階：找出最大值與平均數
max_value = max(A, B, C, D, E)
average = (A + B + C + D + E) / 5

# 找出最大值對應的變數名稱
if max_value == A:
    max_name = "A"
elif max_value == B:
    max_name = "B"
elif max_value == C:
    max_name = "C"
elif max_value == D:
    max_name = "D"
else:
    max_name = "E"

print(f"\n最大值的變數為 {max_name}，值為 {max_value}")
print(f"平均數為 {average}")
