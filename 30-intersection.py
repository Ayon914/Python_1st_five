def find_intersection(set1, sset2):
    myIntersection = set1.intersection(set2)
    return myIntersection

set1_in = input("Enter numbers of the first set, separated by spaces: ")
set2_in = input("Enter numbers of the second set, separated by spaces: ")



set1 = set(map(int,set1_in.split()))
set2 = set(map(int,set2_in.split()))

result = find_intersection(set1, set2)
print("Intersection of set1 and set2 : ",result)