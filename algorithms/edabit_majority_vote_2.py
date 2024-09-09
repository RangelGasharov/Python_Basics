def majority_vote(votes):
    if len(votes) == 0:
        return None
    current_majority = votes[0]
    leading_votes = 1
    for vote in votes:
        if vote != current_majority:
            if leading_votes < 1:
                current_majority = vote
            else:
                leading_votes -= 1
        else:
            leading_votes += 1
    return (leading_votes >= 1) * current_majority or None


print(majority_vote([]))
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
print(majority_vote(["A", "B", "C", "A", "C", "C"]))
print(majority_vote(["A", "B", "C", "A", "C", "C", "C"]))
print(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
