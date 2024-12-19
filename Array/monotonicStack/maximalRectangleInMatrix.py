class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def area_of_rectange(nums):
            stack = []
            nums.append(0)

            max_area = 0

            for i in range(len(nums)):

                while stack and nums[stack[-1]] > nums[i]:
                    index = stack.pop()
                    height = nums[index]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, w * height)
                stack.append(i)
            return max_area

        if not matrix or not matrix[0]:
            return 0
        m_area = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols

        for row in range(rows):

            for col in range(cols):

                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            m_area = max(m_area, area_of_rectange(heights))

        return m_area


