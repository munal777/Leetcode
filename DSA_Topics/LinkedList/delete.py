class Node:
    def __init__(self, data):
        # Each node has two parts: data and a pointer to the next node
        self.data = data
        self.next = None

def deletionInFirst(head):
    if head.next is None:
        return
    
    head = head.next
    return head

def deletionInLast(head):
    head = head
    curr = head

    while curr.data is not None:
        if curr.next is None:
            curr.data = None
            return head
        
        curr = curr.next

    

def print_list(head):

    while head is not None:
        print(head.data)

        head = head.next

def main():
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(15)
    head.next.next.next = Node(20)

    # head = deletionInFirst(head)
    head = deletionInLast(head)
    print_list(head)



if __name__ == "__main__":
    main()
