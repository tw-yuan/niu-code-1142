from decimal import Decimal, getcontext

# 基本題
a = int(input("請輸入被除數 (預設 20)：") or 20)
b = int(input("請輸入除數 (預設 6)：") or 6)

# (1) 使用浮點數計算
float_result = a / b
print(f"\n(1) 浮點數計算 {a}/{b} = {float_result}")

# (2) 使用 decimal 類別中的 Decimal() 建構式計算
getcontext().prec = 50
decimal_result = Decimal(a) / Decimal(b)
print(f"(2) Decimal 計算 {a}/{b} = {decimal_result}")

# 進階：找出兩者從第幾位數開始不一樣
float_str = f"{float_result:.20f}"
decimal_str = f"{decimal_result:.20f}"

print(f"\n--- 進階比較 ---")
print(f"浮點數 (20位): {float_str}")
print(f"Decimal (20位): {decimal_str}")

diff_pos = None
for i, (fc, dc) in enumerate(zip(float_str, decimal_str)):
    if fc != dc:
        digit_count = i - float_str.index('.') if '.' in float_str[:i+1] else i
        diff_pos = digit_count
        break

if diff_pos is not None:
    print(f"\n從小數點後第 {diff_pos} 位開始不一樣")
    print(f"  浮點數該位值: {float_str[float_str.index('.') + diff_pos]}")
    print(f"  Decimal該位值: {decimal_str[decimal_str.index('.') + diff_pos]}")
else:
    print("\n兩者在 20 位小數內完全相同")
