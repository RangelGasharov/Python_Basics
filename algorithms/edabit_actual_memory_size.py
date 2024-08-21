def actual_memory_size(string_memory):
    memory_number = int(string_memory[:-2])
    memory_unit = string_memory[-2]
    if memory_unit == "G":
        memory_number *= 1000
    memory_number *= 0.93
    if memory_number < 1000:
        return str(round(memory_number, 2)) + "MB"
    else:
        return str(round(memory_number / 1000, 2)) + "GB"


print(actual_memory_size("23GB"))
print(actual_memory_size("940MB"))
print(actual_memory_size("512MB"))
print(actual_memory_size("256MB"))
