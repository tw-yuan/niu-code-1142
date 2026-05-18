import random

# 基本題：角色打怪升級模擬
print("=== 基本題：角色打怪升級模擬 ===")

exp = 0
monster_count = 0

while exp < 200:
    monster = random.randint(1, 3)
    monster_count += 1

    if monster == 1:
        monster_name = "小怪"
        gain_exp = 10
    elif monster == 2:
        monster_name = "中怪"
        gain_exp = 20
    else:
        monster_name = "大怪"
        gain_exp = 30

    exp += gain_exp

    print(f"第 {monster_count} 輪：遇到 {monster_name}（{monster}）")
    print(f"本輪獲得經驗值：{gain_exp}")
    print(f"目前總經驗值：{exp}")
    print()

if exp == 200:
    final_status = "剛好升級"
else:
    final_status = "超過升級門檻"

print(f"總共打了 {monster_count} 隻怪")
print(f"最後結果：{final_status}")

# 進階題：血量與戰鬥結果機制
print("\n=== 進階題：血量與戰鬥結果機制 ===")

exp = 0
hp = 100
battle_count = 0

while exp < 200 and hp > 0:
    monster = random.randint(1, 3)
    battle_count += 1

    if monster == 1:
        monster_name = "小怪"
        gain_exp = 10
    elif monster == 2:
        monster_name = "中怪"
        gain_exp = 20
    else:
        monster_name = "大怪"
        gain_exp = 30

    old_exp = exp
    old_hp = hp

    if random.random() < 0.8:
        battle_result = "勝利"
        exp += gain_exp
        exp_change = exp - old_exp
        hp_change = hp - old_hp
    else:
        battle_result = "失敗"
        damage = random.randint(5, 20)
        hp = hp - damage
        if hp < 0:
            hp = 0
        exp_change = exp - old_exp
        hp_change = hp - old_hp

    print(f"第 {battle_count} 場戰鬥：遇到 {monster_name}（{monster}）")
    print(f"戰鬥結果：{battle_result}")
    print(f"經驗值變化：{exp_change:+d}，目前經驗值：{exp}")
    print(f"血量變化：{hp_change:+d}，剩餘血量：{hp}")
    print()

if exp >= 200:
    advanced_result = "成功升級"
else:
    advanced_result = "血量歸零，遊戲失敗"

print(f"最後結果：{advanced_result}")
print(f"總共打了 {battle_count} 場戰鬥")
print(f"剩餘血量：{hp}")
print(f"最後經驗值：{exp}")
