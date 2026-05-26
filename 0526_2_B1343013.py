# 基本題：咖啡店菜單查詢與異動操作
print("=== 基本題：咖啡店菜單查詢與異動操作 ===")

menu = {
    "拿鐵": 10,
    "美式咖啡": 6,
    "摩卡": 0,
    "卡布奇諾": 4,
    "焦糖瑪奇朵": 2
}

if "冰滴咖啡" not in menu:
    menu["冰滴咖啡"] = 7
    print("冰滴咖啡不在菜單中，已新增冰滴咖啡：7 份")

if "摩卡" in menu and menu["摩卡"] == 0:
    del menu["摩卡"]
    print("摩卡庫存為 0，已從菜單中刪除")

if "拿鐵" in menu:
    menu["拿鐵"] = menu["拿鐵"] + 5
    print("拿鐵已補貨 5 份")

print("\n目前菜單與剩餘數量：")
for coffee in menu:
    print(f"{coffee}：{menu[coffee]} 份")

# 進階題：咖啡店庫存清理與更新操作
print("\n=== 進階題：咖啡店庫存清理與更新操作 ===")

menu = {
    "拿鐵": 12,
    "美式咖啡": 3,
    "焦糖瑪奇朵": 0,
    "卡布奇諾": 1,
    "冰滴咖啡": 0
}

print("原始菜單：")
for coffee in menu:
    print(f"{coffee}：{menu[coffee]} 份")

for coffee in list(menu.keys()):
    if menu[coffee] == 0:
        menu.pop(coffee)

print("\n清除庫存為 0 的品項後：")
for coffee in menu:
    print(f"{coffee}：{menu[coffee]} 份")

removed_item = menu.popitem()
print(f"\n刪除最後一筆品項：{removed_item[0]}，數量：{removed_item[1]} 份")

wrong_order = menu.pop("濃縮咖啡", "查無此項目")
print(f"安全刪除濃縮咖啡：{wrong_order}")

print("\n剩餘菜單：")
for coffee in menu:
    print(f"{coffee}：{menu[coffee]} 份")

menu.clear()
print(f"\n清空菜單後：{menu}")
