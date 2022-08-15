#Lesson 18: Sets
# collection which is undordered, unindexed. no duplicate values.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)