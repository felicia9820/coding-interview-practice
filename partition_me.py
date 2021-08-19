def partition(lst, p):
    head = lst.tail = lst.head

    while head is not None:
        next_node = head.next
        head.next = None
        if head.value < p:
            head.next = lst.head
            lst.head = head
        else:
            lst.tail.next = head
            lst.tail = head
        head = next_node

    if lst.tail.next is not None:
        lst.tail.next = None

    return lst
