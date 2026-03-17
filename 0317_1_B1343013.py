# 基本題：輸入兩個整數 a 與 b，完成各種運算
print("=== 基本題 ===")
a = int(input("請輸入整數 a："))
b = int(input("請輸入整數 b："))

print(f"\na + b  = {a + b:10}  （加法）")
print(f"a - b  = {a - b:10}  （減法）")
print(f"a * b  = {a * b:10}  （乘法）")
print(f"a / b  = {a / b:10.4f}  （除法）")
print(f"a // b = {a // b:10}  （整數除法）")
print(f"a % b  = {a % b:10}  （取餘數）")
print(f"a ** b = {a ** b:10}  （次方）")

# 進階題：輸入整數 n，完成位移、位元、邏輯運算
print("\n=== 進階題 ===")
n = int(input("請輸入整數 n："))

print(f"\n(a) 位移運算子：")
print(f"  n << 1 = {n << 1}  （左移 1 位，相當於 n × 2）")
print(f"  n >> 1 = {n >> 1}  （右移 1 位，相當於 n ÷ 2 取整）")

print(f"\n(b) 位元運算子：")
print(f"  n & 3n = {n & (3 * n)}  （AND）")
print(f"  n | 3n = {n | (3 * n)}  （OR）")
print(f"  n ^ 3  = {n ^ 3}  （XOR）")

print(f"\n(c) 邏輯運算式：")
result = (n > 10) and (n % 2 == 0)
print(f"  (n > 10) and (n % 2 == 0) = {result}")
