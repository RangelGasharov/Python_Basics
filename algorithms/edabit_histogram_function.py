def histogram(arr, char):
    result = ""
    for i in range(len(arr)):
        for j in range(int(arr[i])):
            result += str(char)
        result += "\n"
    return result


print(histogram([1, 3, 4], "#"))
print(histogram([6, 2, 15, 3], "="))
print(histogram([1, 10], "+"))
