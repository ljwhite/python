from decimal import *

sum = Decimal(0)
sum += Decimal("0.0111111111111111")
sum += Decimal("0.0111111111111111")
sum += Decimal("0.0111111111111111")
sum -= Decimal("0.0111111111111111")
sum -= Decimal("0.0111111111111111")
sum -= Decimal("0.0111111111111111")

print("Sum = ", sum)