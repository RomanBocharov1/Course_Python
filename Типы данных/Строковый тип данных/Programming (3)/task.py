name_city1 = input()
name_city2 = input()
name_city3 = input()
name_city_len1= len(name_city1)
name_city_len2= len(name_city2)
name_city_len3= len(name_city3)
name_city_max = max(name_city_len1, name_city_len2, name_city_len3)
name_city_min = min(name_city_len1, name_city_len2, name_city_len3)
if name_city_min == name_city_len2 and name_city_max == name_city_len1:
    print(name_city2, name_city1, sep = '\n')
elif name_city_min == name_city_len1 and name_city_max == name_city_len2:
    print(name_city1, name_city2, sep = '\n')
elif name_city_min == name_city_len3 and name_city_max == name_city_len1:
    print(name_city3, name_city1, sep = '\n')
elif name_city_min == name_city_len3 and name_city_max == name_city_len2:
    print(name_city3, name_city2, sep = '\n')
elif name_city_min == name_city_len1 and name_city_max == name_city_len3:
    print(name_city1, name_city3, sep = '\n')

