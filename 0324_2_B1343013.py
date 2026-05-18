# 基本題：使用 match/case 判斷月份資訊
month = int(input("請輸入月份 (1~12)："))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        days = 31
    case 4 | 6 | 9 | 11:
        days = 30
    case 2:
        days = "28（平年）或 29（閏年）"
    case _:
        days = None

match month:
    case 3 | 4 | 5:
        season = "春季"
    case 6 | 7 | 8:
        season = "夏季"
    case 9 | 10 | 11:
        season = "秋季"
    case 12 | 1 | 2:
        season = "冬季"
    case _:
        season = None

if days is None:
    print("輸入錯誤，請輸入 1~12 的月份")
else:
    print(f"\n{month} 月有 {days} 天")
    print(f"{month} 月屬於{season}")

# 進階題：查詢當季水果 & 反向查詢盛產月份
seasonal_fruits = {
    1:  ["草莓", "柳丁", "棗子"],
    2:  ["草莓", "蓮霧", "棗子"],
    3:  ["草莓", "蓮霧", "枇杷"],
    4:  ["鳳梨", "枇杷", "桑葚"],
    5:  ["鳳梨", "荔枝", "芒果"],
    6:  ["芒果", "荔枝", "西瓜"],
    7:  ["芒果", "西瓜", "龍眼"],
    8:  ["龍眼", "西瓜", "文旦"],
    9:  ["文旦", "柿子", "百香果"],
    10: ["柿子", "百香果", "柑橘"],
    11: ["柑橘", "柳丁", "釋迦"],
    12: ["柳丁", "釋迦", "草莓"],
}

if days is not None:
    fruits = seasonal_fruits.get(month, [])
    print(f"\n{month} 月的當季水果有：{'、'.join(fruits)}")

    fruit_input = input("\n請輸入水果名稱（查詢盛產月份）：")
    producing_months = [
        str(m) for m, f_list in seasonal_fruits.items()
        if fruit_input in f_list
    ]
    if producing_months:
        print(f"「{fruit_input}」的盛產月份為：{', '.join(producing_months)} 月")
    else:
        print(f"查無「{fruit_input}」的盛產資料")
