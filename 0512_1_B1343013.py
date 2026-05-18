# 基本題：行程瀏覽器（使用 iter() + next()）
print("=== 基本題：行程瀏覽器 ===")

spots = ["火車站", "早餐店", "博物館", "老街", "夜市"]
spot_iter = iter(spots)
visited_count = 0

print("旅行景點清單：", spots)
print("接下來要拜訪前三個景點：")

for i in range(3):
    spot = next(spot_iter)
    visited_count += 1
    print(f"第 {visited_count} 站：{spot}")

remaining = len(spots) - visited_count
print(f"目前還剩 {remaining} 個景點尚未被拜訪")

# 進階題：任務處理器（序列 + 迭代器 + while + break/continue）
print("\n=== 進階題：任務處理器 ===")

tasks = ["寫報告", "交作業", "回覆 Email", "繳電話費", "準備期中考"]
task_iter = iter(tasks)
finish_count = 0

while True:
    command = input("請按 Enter 顯示下一項任務，輸入 skip 或 s 跳過，輸入 q 結束：")

    if command == "q":
        print("任務流程已提前結束")
        break

    try:
        task = next(task_iter)
    except StopIteration:
        print("所有任務都已處理完畢")
        break

    if command == "skip" or command == "s":
        print(f"已跳過任務：{task}")
        continue

    print(f"目前任務：{task}")
    finish_count += 1

print(f"使用者總共完成了 {finish_count} 項任務")
