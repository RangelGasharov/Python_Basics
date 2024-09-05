import heapq


def ulam(n):
    ulam_list = [1, 2]
    if n < 3:
        return ulam_list[n - 1]
    sum_counts = {}
    heap = []

    for i in range(len(ulam_list)):
        for j in range(i + 1, len(ulam_list)):
            s = ulam_list[i] + ulam_list[j]
            if s not in sum_counts:
                sum_counts[s] = 1
                heapq.heappush(heap, s)
            else:
                sum_counts[s] += 1

    while len(ulam_list) < n:
        while heap:
            smallest_sum = heapq.heappop(heap)
            if sum_counts[smallest_sum] == 1:
                ulam_list.append(smallest_sum)
                break

        for ulam_number in ulam_list[:-1]:
            new_sum = ulam_number + smallest_sum
            if new_sum not in sum_counts:
                sum_counts[new_sum] = 1
                heapq.heappush(heap, new_sum)
            else:
                sum_counts[new_sum] += 1

    return ulam_list[-1]


print(ulam(4))
print(ulam(9))
print(ulam(38))
print(ulam(99))
print(ulam(206))
print(ulam(495))
print(ulam(577))
print(ulam(1577))
