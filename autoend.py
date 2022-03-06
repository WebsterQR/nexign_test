def find_ends(start: str, dictionary: dict) -> list:
    ends = [(None, -1)] * 10
    for line in dictionary:
        if line.startswith(start):
            position = pos_to_array_insert(ends, line, dictionary[line])
            for i in range(len(ends) - 1, position, -1):
                ends[i] = ends[i - 1]
            ends[position] = (line, dictionary[line])
    return ends

def pos_to_array_insert(array: list, line: str, count: int) -> int:
    for num, el in enumerate(array):
        if el[1] < count:
            return num

def strip_enters(line: str) -> str:
    while line.endswith("\n"):
        line = line[:-2]
    return line


N = int(input())
dictionary = dict()
for _ in range(N):
    word, count = input().split()
    count = int(count)
    dictionary[word] = count

M = int(input())
output_line = ""
for _ in range(M):
    word_start = input()
    result = find_ends(word_start, dictionary)
    for el in result:
        if el[0] != None:
            output_line = output_line + el[0] + "\n"
    output_line += "\n"
print(strip_enters(output_line))

