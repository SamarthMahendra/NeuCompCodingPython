def solution(A):
    # Initialize moves with the first element of the array
    moves = A[0]

    # Traverse through the array
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            moves += A[i] - A[i - 1]

    return moves


# Test cases
a = [2, 2, 0, 0, 1]
print(solution(a))  # Output: 5