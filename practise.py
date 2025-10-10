class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):

    while head is not None:
        print(head.data)
        head = head.next


def traverseList(head):
    if head is None:
        return
    print(head.data, end=' ')
    traverseList(head.next)


def add_data_in_first(head):
    current = head

    head = Node(10)
    head.next = current

    return head


def main():

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    head = add_data_in_first(head)
    print(traverseList(head))

    

if __name__ == '__main__':
    main()
