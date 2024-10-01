def string_fret(string_number, fret):
    notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    offset = [+5, -5, -4, -5, -5, -5]
    if string_number > 6 or string_number <= 0 or fret > 24 or fret < 0:
        return "Invalid input"
    current_offset = 0
    for i in range(string_number):
        current_offset += offset[i]
    return notes[(current_offset - 1 + fret) % len(notes)]


print(string_fret(1, 18))
print(string_fret(2, 0))
print(string_fret(2, 10))
print(string_fret(3, 0))
print(string_fret(4, 18))
print(string_fret(5, 0))
print(string_fret(6, 10))
print(string_fret(7, 7))
print(string_fret(0, 16))
print(string_fret(5, 25))
