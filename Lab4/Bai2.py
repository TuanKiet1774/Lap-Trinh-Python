def dem_ky_tu(s):
    #dic = dict()
    dic = {}
    for x in set(s):
        dic[x] = s.count(x)     
    return dic

s = "Ana has apples."
print(dem_ky_tu(s))
