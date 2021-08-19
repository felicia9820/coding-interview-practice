def sumlists_back(l1, l2):
    a = l1.head
    b = l2.head

    c = LinkedList()

    carry = 0

    head = c.head

    while a or b or carry:
        val1 = a.value if a else 0
        val2 = b.value if b else 0
        carry, out = divmod(val1 + val2 + carry, 10) 

        head.next.value = out
        head = head.next

        a = a.next
        b = b.next

    return c.tail

def sumlists_forward(l1, l2):
    a = l1.head()
    b = l2.head()

    c = LinkedList()
    c.head.value = 0
    prev = c.head
    nexx = prev.next


    carry = 0

    while a or b or carry:
        val1 = a.value if a else 0
        val2 = b.value if b else 0

        carry, out = divmod(val1 + val2 + carry, 10)

        prev += carry
        nexx.value = out
        prev = nexx
        nexx = nexx.next

        a = a.next
        b = b.next
    
    return c
        