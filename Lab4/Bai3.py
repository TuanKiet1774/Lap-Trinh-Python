def So_Nguyen(ds):
  temp = [i for i in set(ds) if ds.count(i) == 1]
  return temp

def Max(ds):
    max_count = 0
    pt_max = ''
    
    for i in set(ds):
        count = ds.count(i)
        if count > max_count:
            pt_max = i
            max_count = count 
    return pt_max, max_count


a = [1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 0]
print("Các số xuất hiện 1 lần:",So_Nguyen(a),"\nCác số xuất hiện nhiều lần:",list(set(a) - set(So_Nguyen(a))))

print("Số xuất hiện nhiều nhất:", Max(a)[0], "-", Max(a)[1], "lần")
    
    