# 基本題：購物折扣計算
amount = int(input("請輸入購物金額（元）："))

if amount >= 5000:
    discount = 0.7
    level = "7 折"
elif amount >= 4000:
    discount = 0.75
    level = "75 折"
elif amount >= 3000:
    discount = 0.8
    level = "8 折"
elif amount >= 2000:
    discount = 0.85
    level = "85 折"
elif amount >= 1000:
    discount = 0.9
    level = "9 折"
elif amount >= 500:
    discount = 0.95
    level = "95 折"
else:
    discount = 1.0
    level = "不打折（100%）"

final = amount * discount
print(f"\n購物金額：{amount} 元")
print(f"折扣等級：{level}")
print(f"折扣後金額：{final:.0f} 元")

# 進階題：還差多少金額可進入下一個更好的折扣
tiers = [
    (500,  "95 折"),
    (1000, "9 折"),
    (2000, "85 折"),
    (3000, "8 折"),
    (4000, "75 折"),
    (5000, "7 折"),
]

next_tier = None
for threshold, name in tiers:
    if amount < threshold:
        next_tier = (threshold, name)
        break

if next_tier:
    diff = next_tier[0] - amount
    print(f"\n再多消費 {diff} 元（達到 {next_tier[0]} 元），即可享有 {next_tier[1]} 優惠！")
else:
    print("\n您已達到最高折扣等級（7 折）！")
