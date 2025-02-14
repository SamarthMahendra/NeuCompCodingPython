
def solution(head):
    if not head:
        return None

    hashmap = {}  # Dictionary to store the mapping from original to copied nodes

    cur = head

    # First pass: Create copies of nodes and store them in hashmap
    while cur:
        hashmap[cur] = Node(cur.val)
        cur = cur.next

    cur = head

    # Second pass: Assign next and random pointers
    while cur:
        if cur.next:
            hashmap[cur].next = hashmap[cur.next]  # Assign next pointer
        if cur.random:
            hashmap[cur].random = hashmap[cur.random]  # Assign random pointer
        cur = cur.next

    return hashmap[head]