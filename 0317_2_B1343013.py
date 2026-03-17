# 基本題：判斷閏年
year = int(input("請輸入西元年份："))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"{year} 年是閏年")
else:
    print(f"{year} 年不是閏年")

# 進階題：輸出該年 2 月有幾天，並說明為何需要閏年
feb_days = 29 if is_leap else 28
print(f"{year} 年的 2 月有 {feb_days} 天")

print("\n【為何需要閏年？】")
print("地球繞太陽公轉一圈約為 365.2422 天，")
print("若每年都只算 365 天，每年會少約 0.2422 天，")
print("大約每 4 年就會累積少將近 1 天。")
print("因此設置閏年，在該年的 2 月多加 1 天（29 天），")
print("以修正曆法與實際天文週期之間的誤差。")
print("而每 100 年跳過一次閏年、每 400 年再補回一次，")
print("是為了更精確地校正這個差距。")
