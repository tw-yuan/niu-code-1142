# 基本題：統計數字資料與組合訊息
print("=== 基本題：統計數字資料與組合訊息 ===")

data = input("請輸入一串用逗號隔開的數字（例如 5,3,9,1,3）：")
parts = data.split(",")
numbers = []

for item in parts:
    numbers.append(int(item))

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

result = "輸入的數字列表：" + str(numbers) + "\n"
result = result + "這串數字的總數：" + str(len(numbers)) + "\n"
result = result + "所有數字的總和：" + str(sum(numbers)) + "\n"
result = result + "最小值：" + str(min(numbers)) + "\n"
result = result + "最大值：" + str(max(numbers)) + "\n"

for number in unique_numbers:
    result = result + "數字 " + str(number) + " 出現了 " + str(numbers.count(number)) + " 次\n"
    result = result + "數字 " + str(number) + " 第一次出現的位置：" + str(numbers.index(number)) + "\n"

print(result)

# 進階題：支援空白與混合文字
print("=== 進階題：支援空白與混合文字 ===")

advanced_data = input("請輸入資料（例如 5, hello, 9, world, 1,3）：")
advanced_parts = advanced_data.split(",")
advanced_numbers = []

for item in advanced_parts:
    item = item.strip()

    if item.isdigit():
        advanced_numbers.append(int(item))

if len(advanced_numbers) == 0:
    advanced_result = "沒有可分析的數字；分析完成！"
else:
    advanced_unique_numbers = []
    for number in advanced_numbers:
        if number not in advanced_unique_numbers:
            advanced_unique_numbers.append(number)

    advanced_result = "輸入的數字列表：" + str(advanced_numbers)
    advanced_result = advanced_result + "；這串數字的總數：" + str(len(advanced_numbers))
    advanced_result = advanced_result + "；所有數字的總和：" + str(sum(advanced_numbers))
    advanced_result = advanced_result + "；最小值：" + str(min(advanced_numbers))
    advanced_result = advanced_result + "；最大值：" + str(max(advanced_numbers))

    for number in advanced_unique_numbers:
        advanced_result = advanced_result + "；數字 " + str(number) + " 出現了 " + str(advanced_numbers.count(number)) + " 次"
        advanced_result = advanced_result + "；數字 " + str(number) + " 第一次出現的位置：" + str(advanced_numbers.index(number))

    advanced_result = advanced_result + "；分析完成！"

print(advanced_result)
