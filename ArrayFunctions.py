lucky_numbers = [5, 2, 17, 7, 99, 54]
friends = ["Maximilian", "George", "Samuel", "Christopher", "Tim"]
print("Array of friends: " + str(friends))
friends.insert(0, "Kevin")
print("Array of friends after adding a person at position 0 with insert: " + str(friends))
friends.append("Charles")
print("Array of friends after adding a person with append" + str(friends))
friends.pop()
print("Array of friends after deleting a person with pop" + str(friends))
print("Position where Kevin is in the Array: " + str(friends.index("Kevin")))
# print(friends.index("Mike"))
