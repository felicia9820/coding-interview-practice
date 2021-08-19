from linked_list import LinkedList

def remove_dups(lst):
    unique = set()

    head = lst.head
    prev = None

    while head is not None:
        if head.value in unique:
            prev.next = head.next
        else:
            unique.add(head.value)
            prev = head
        
        head = head.next

    lst.tail = prev
    return lst

def remove_dups_runner(lst):
    runner = current = lst.head

    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    lst.tail = runner
    return lst

        
        