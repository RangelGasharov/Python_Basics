def ulam(n):
    ulam_list = [1, 2]
    if n < 3:
        return ulam_list[n - 1]
    current_number = 3
    while len(ulam_list) < n:
        count = 0
        for i in range(len(ulam_list)):
            for k in range(i, len(ulam_list)):
                if ulam_list[i] + ulam_list[k] == current_number and i != k:
                    count += 1
        if count == 1:
            ulam_list.append(current_number)
        else:
            current_number += 1
            continue
        current_number += 1
    return ulam_list[n - 1]


print(ulam(4))
print(ulam(9))
print(ulam(38))
print(ulam(99))
print(ulam(206))
print(ulam(495))
print(ulam(577))
