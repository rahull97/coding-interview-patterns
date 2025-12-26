def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot = pivot - 1
    if pivot == -1:
        return "".join(reversed(letters))
    else:
        right_most_successor = len(letters) - 1
        while letters[pivot] >= letters[right_most_successor]:
            right_most_successor = right_most_successor - 1
        letters[pivot], letters[right_most_successor] = letters[right_most_successor], letters[pivot]
        letters[pivot+1:] = reversed(letters[pivot+1:])
        return "".join(letters)
