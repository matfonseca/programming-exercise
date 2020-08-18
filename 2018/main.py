# Given a list of integers L and a value K,
# return the number of pairs whose elements sum to less than K.
print("--Pair Sum--")

array = [3, 7, 2, 8]
k = 10


def sumsLessThan(list_numbers, k):
    result = 0
    amount_numbers = len(list_numbers)
    for i in range(0, amount_numbers):
        for j in range(i, amount_numbers):
            if i != j and list_numbers[i] + list_numbers[j] < k:
                result += 1
    return result


print(sumsLessThan(array, k))


print("--Man in the Middle--")

message = []

with open('exercise_3.txt', 'r') as f:
    index_line = 0
    for line in f:
        if index_line != 0:
           message.append(line.strip())
        index_line += 1

encode_label_message = "It Is Up To You#####"

def encodeMessage(message):
    for line in message:
        print(encode_label_message + line)


encodeMessage(message)


print("--The Context Switching Problem--")

import functools

def numberOfChunks(start_meetings, end_meetings):
    max = functools.reduce(lambda x, y: x if x > y else y, end_meetings)
    min = functools.reduce(lambda x, y: x if x < y else y, start_meetings)
    time = [min, max]
    times = [time]
    size = len(start_meetings)

    for i in range(0, size):
        meeting_i = [start_meetings[i], end_meetings[i]]
        new_times = []
        for time in times:
            if meeting_i[0] < time[1] and meeting_i[1] < time[1]:
                new_times.append([time[0],meeting_i[0]])
                new_times.append([meeting_i[1], time[1]])
            elif time[0] < meeting_i[1] and meeting_i[0] <= time[0] and meeting_i[1] < time[1]:
                new_times.append([time[1],meeting_i[1]])
            elif time[0] < meeting_i[0] and meeting_i[0] < time[1] and meeting_i[1] >= time[1]:
                new_times.append([time[0], meeting_i[0]])
            else:
                pass
        times = new_times

    return len(new_times)

print(numberOfChunks([1,6,2], [3, 7, 9]))

print(numberOfChunks([1, 6], [3, 7]))