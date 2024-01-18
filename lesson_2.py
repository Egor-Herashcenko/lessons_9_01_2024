number = int(input())
thousandths = number % 10
hundredths = number // 10 % 10
tenths = number // 100 % 10
units = number // 1000

print(units)
print(tenths)
print(hundredths)
print(thousandths)
