def div_finder(div):
    div_list = []
    for i in range(1, div):
        if div % i == 0:
            div_list.append(i)
    if sum(div_list) == div:
        print (div, div_list)
    return div_list

print ("A perfect number is is a number whose divisors, not including itself, add up to that number.\nIt is unknown if there are any odd numbers and is also unknown if there an infinite amount." )
for j in range(1, 1000000000000):
    div_finder(j)
