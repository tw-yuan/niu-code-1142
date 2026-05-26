# 基本題：遊戲金幣轉換器
print("=== 基本題：遊戲金幣轉換器 ===")

money = input("請輸入遊戲貨幣數值（例如 500g 或 20d）：")
money = money.replace(" ", "").lower()

if "g" in money and "d" not in money:
    try:
        gold = float(money.replace("g", ""))
        diamond = gold / 100
        print(f"{gold:.2f} 金幣 = {diamond:.2f} 鑽石")
    except ValueError:
        print("輸入錯誤，請輸入正確的數字與單位")
elif "d" in money and "g" not in money:
    try:
        diamond = float(money.replace("d", ""))
        gold = diamond * 100
        print(f"{diamond:.2f} 鑽石 = {gold:.2f} 金幣")
    except ValueError:
        print("輸入錯誤，請輸入正確的數字與單位")
else:
    print("輸入錯誤，請輸入包含 g 或 d 的貨幣數值")

# 進階題：連續輸入版本
print("\n=== 進階題：連續輸入版本 ===")

while True:
    user_input = input("請輸入貨幣數值（例如 500 g、20 D，輸入 q 結束）：")
    user_input = user_input.replace(" ", "").lower()

    if user_input == "q":
        print("轉換器結束")
        break

    if "g" in user_input and "d" not in user_input:
        number_text = user_input.replace("g", "")

        try:
            gold = float(number_text)
            diamond = gold / 100
            print(f"{gold:.2f} 金幣 = {diamond:.2f} 鑽石")
        except ValueError:
            print("格式錯誤，請重新輸入")

    elif "d" in user_input and "g" not in user_input:
        number_text = user_input.replace("d", "")

        try:
            diamond = float(number_text)
            gold = diamond * 100
            print(f"{diamond:.2f} 鑽石 = {gold:.2f} 金幣")
        except ValueError:
            print("格式錯誤，請重新輸入")

    else:
        print("格式錯誤，請輸入包含 g 或 d 的貨幣數值")
