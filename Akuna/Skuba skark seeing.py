# big money for anyone who sees exact number of sharks
# divers who can see too many sharks  are not eligible for the prize but they may still recieve less money
# each dive requires - 1 tank and number of sharks seen  ( dependding on magnitute of factors) is 0 - 5
# divers can dive at any location - can see same location multiple times


# he knows the exact probability of seeing each of the 6 possible number of sharks at each location

# assume he takes an optmizal startegy to get big money
# each of his dives is independent of the others
# implement a function to determine the probability of him getting big money
def calculate_big_money_recursive(locations, target_sharks, max_dives):
    """
    Recursively calculate the probability of the diver seeing exactly the target number of sharks.

    :param locations: A list of lists, where each sublist contains 6 probabilities representing
                      the probabilities of seeing 0, 1, 2, 3, 4, and 5 sharks at that location.
    :param target_sharks: The exact number of sharks the diver needs to see to get big money.
    :param max_dives: The number of dives the diver can make.

    :return: The probability of the diver seeing exactly the target number of sharks.
    """

    def helper(dive, seen_sharks, prob_accumulated):
        # Base case: If we have finished all dives, check if we have seen the target number of sharks
        if dive == max_dives:
            if seen_sharks == target_sharks:
                return prob_accumulated  # We've reached the target, return the accumulated probability
            else:
                return 0  # Didn't reach the target number of sharks, return 0

        # Get the probabilities for the current location
        location_probs = locations[dive % len(locations)]

        # Recursively explore all possible outcomes for the current dive (0-5 sharks)
        total_probability = 0
        for sharks_seen in range(6):
            if seen_sharks + sharks_seen <= target_sharks:  # Only consider valid cases
                total_probability += helper(
                    dive + 1,  # Move to the next dive
                    seen_sharks + sharks_seen,  # Update the number of sharks seen so far
                    prob_accumulated * location_probs[sharks_seen]  # Accumulate the probability
                )

        return total_probability

    # Start the recursion with the first dive, 0 sharks seen, and probability 1
    return helper(0, 0, 1)


# Example usage
locations = [
    [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],  # Probabilities for location 1
    [0.15, 0.25, 0.2, 0.1, 0.15, 0.15],  # Probabilities for location 2
    [0.05, 0.1, 0.35, 0.1, 0.25, 0.15]  # Probabilities for location 3
]
target_sharks = 7  # The exact number of sharks to see
max_dives = 5  # Number of dives allowed

probability = calculate_big_money_recursive

# Test case:
locations = [
    [0.1, 0.1, 0.2, 0.2, 0.3, 0.1],  # Probabilities for L1
    [0.0, 0.3, 0.15, 0.45, 0.1, 0.0],  # Probabilities for L2
    [0.4, 0.1, 0.1, 0.1, 0.1, 0.2]  # Probabilities for L3
]
target_sharks = 8  # The exact number of sharks to see
max_dives = 2  # Maximum number of dives
# Run the function with the test case
result = calculate_big_money_recursive(locations, target_sharks, max_dives)
print(f"Probability of success: {result}")


