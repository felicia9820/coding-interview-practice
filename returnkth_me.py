def kth_tolast(lst, k):
    runner = current = lst.head

    while current:
        runner = current
        count = 0

        while runner:
            count += 1
            runner = runner.next

        if count == k:
            return current
        else:
            current = current.next
    

def kth_to_last(lst):
    runner = current = lst.head

    for n in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current