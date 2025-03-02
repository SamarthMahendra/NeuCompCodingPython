input = [4, 5, 2, 10, 8]
Output = [5, 10, 10, -1, -1]



from typing import List
def get_next_greater_element(nums: List[int]) -> List[int]:

    m_stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):

        while m_stack and nums[m_stack[-1]] < nums[i]:
            index = m_stack.pop()
            res[index] = nums[i]
        m_stack.append(i)

    return res




print(get_next_greater_element(input))