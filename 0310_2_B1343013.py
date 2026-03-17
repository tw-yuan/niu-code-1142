from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP
from decimal import ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_05UP, ROUND_CEILING, ROUND_FLOOR

numbers = [Decimal("3.265"), Decimal("1.32"), Decimal("5.305")]

# 基本題
print("=== 基本題 ===")
for num in numbers:
    print(f"\n數值: {num}")
    print(f"  (1) ROUND_DOWN    (無條件捨去): {num.quantize(Decimal('0.01'), rounding=ROUND_DOWN)}")
    print(f"  (2) ROUND_UP      (無條件進入): {num.quantize(Decimal('0.01'), rounding=ROUND_UP)}")
    print(f"  (3) ROUND_HALF_UP (四捨五入):   {num.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")

# 進階題
print("\n=== 進階題 ===")
advanced_modes = [
    ("ROUND_HALF_DOWN", ROUND_HALF_DOWN),
    ("ROUND_HALF_EVEN", ROUND_HALF_EVEN),
    ("ROUND_05UP",      ROUND_05UP),
    ("ROUND_CEILING",   ROUND_CEILING),
    ("ROUND_FLOOR",     ROUND_FLOOR),
]

for num in numbers:
    print(f"\n數值: {num}")
    for name, mode in advanced_modes:
        result = num.quantize(Decimal('0.01'), rounding=mode)
        print(f"  {name:20s}: {result}")
