arr = [1, 2, 3, 4]

def test(arr):
    it = iter(arr)  # Create an iterator for the list
    while True:
        try:
            val = next(it)  # Get the next value from the iterator
            custom_print(val)
        except StopIteration:
            # StopIteration is raised when the iterator is exhausted
            break

def custom_print(val):
    print("Value is:", val)

test(arr)
