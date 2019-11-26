
lucky_numbers = [7, 77, 777, 77, 7]
friends = ["Kate", "Karney", "Karen", "Jim", "Roy"]
print("Sorted order: ")
friends.sort()
print(friends)

print("Reverse order: ")
friends.reverse()
print(friends)

print("Merge two arrays")
friends.extend(lucky_numbers)
print("Add backward")
friends.append("Credo")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends[1:4])
print(friends[0:])

print("Remove last element :")
friends.pop()
print(friends)
print(friends.count(77))

tempFriends = friends.copy()
friends.clear()
print(tempFriends)
