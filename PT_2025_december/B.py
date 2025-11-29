n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(input())

answer = float('inf')

index = 0
while index + m <= len(data) - 1:
    string = data[index][::-1]
    second_string = data[index + m][::-1]
    counter = 0
    for i in range(min(len(string), len(second_string))):
        if string[i] == second_string[i]:
            counter += 1
        else:
            break
    answer = min(answer, counter)
    index += 1 

print(answer)