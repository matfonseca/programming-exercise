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