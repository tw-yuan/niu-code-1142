# 基本題：使用 for 搭配 range() 產生等差數列
a = int(input("請輸入首項 a："))
d = int(input("請輸入公差 d："))
n = int(input("請輸入項數 n："))

print(f"\n等差數列（首項={a}, 公差={d}, 項數={n}）：")
for i in range(n):
    term = a + i * d
    print(term, end="  ")
print()

# 進階題：產生費波那契數列前 n 項
fib_n = int(input("\n請輸入費波那契數列的項數 n："))

print(f"\n費波那契數列前 {fib_n} 項：")
fib_a, fib_b = 1, 1
for i in range(fib_n):
    print(fib_a, end="  ")
    fib_a, fib_b = fib_b, fib_a + fib_b
print()
