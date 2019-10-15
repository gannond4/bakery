# David Gannon
# 10/16/19
# Hartwick Bakery

from statistics import mean


cookie_input = []
for i in range(0, 6):
    ele = int(input())
    cookie_input.append(ele)
print(f"""This is the list of cookie sales: {cookie_input}""")

candy_input = []
for i in range(0, 6):
    sale = int(input())
    candy_input.append(sale)
print(f"""This is the list of candy sales: {candy_input}""")

# cookie max min avg
avgco = mean(cookie_input)
print(f"The averge cookie sales are {avgco}")

maxco = max(cookie_input)
print(f"The Max cookie sales was {maxco}")

minco = min(cookie_input)
print(f"The min cookie sales are {minco}")

cosum = sum(cookie_input)

# candy avg max min sum
avgca = mean(candy_input)
print(f"The averge candy sales are {avgca}")

maxca = max(candy_input)
print(f"The Max candy sales was {maxca}")

minca = min(candy_input)
print(f"The min candy sales are {minca}")

casum = sum(candy_input)



if cosum > casum:
    print("The cookies are most populaur at hartwicks bakery")
if cosum < casum:
    print("The candies are most populaur at hartwicks bakery")

