# 基本題：計算字串中母音字母的總數
text = input("請輸入一個字串：")
vowels = "aeiouAEIOU"

count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"\n字串：「{text}」")
print(f"母音字母（a, e, i, o, u，不分大小寫）的總數為：{count}")

# 進階題：字串分析與統計
# (a) 將所有母音字母逐一列出
print("\n所有母音字母（依序）：")
for char in text:
    if char in vowels:
        print(f"  {char}")

# (b) 印出母音 e 與 i 的總數
count_e = 0
count_i = 0
for char in text:
    if char in "eE":
        count_e += 1
    elif char in "iI":
        count_i += 1

print(f"\n母音 e 的總數：{count_e}")
print(f"母音 i 的總數：{count_i}")
