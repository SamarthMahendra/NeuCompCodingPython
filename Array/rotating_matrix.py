# Given a constant matrix that represents tables in a restaurant
seating_chart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304]
]

# Function to transpose the seating chart (Matrix) for new arrangement
def transpose(chart):
    return [[chart[i][j] for i in range(len(chart))] for j in range(len(chart[0]))]

# Example usage:
transposed_seating = transpose(seating_chart)
print(transposed_seating)  # Output will be the transposed matrix
# The expected output - [[104, 204, 304], [103, 203, 303], [102, 202, 302], [101, 201, 301]]