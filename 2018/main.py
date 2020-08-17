# Given a list of integers L and a value K,
# return the number of pairs whose elements sum to less than K.

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
