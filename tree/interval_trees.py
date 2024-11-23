class IntervalNode:

    def __init__(self, interval):
        self.interval = interval
        self.max_end = interval[1]
        self.left = None
        self.right = None


class IntervalTree:

    def __int__(self):
        self.root = None


    def insert(self, root, interval):
        if root is None:
            return IntervalNode(interval)

        elif self.root.interval[0] > interval[0]:
            root.left = self.insert(root.left, interval)
        else:
            root.right = self.insert(root.right, interval)

        root.max_end = max(root.interval, interval[1])

        return root


