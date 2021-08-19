def delete_middle(lst, n):
    head = lst.head

    while head:
        if head.value == n.value:
            break
        prev = head
        head = head.next

    prev.next = head.next
    head = None
    return lst

def delete_middle_short(node):
    node.value = node.next.value
    node.next = node.next.next