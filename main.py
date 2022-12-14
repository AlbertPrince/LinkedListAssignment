class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def reverse_linkedList(self):
        current_node = self.head
        prev_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def is_infinite(self):
        address_set = set()
        temp = self.head

        while temp:
            if temp in address_set:
                return True
            address_set.add(temp)
            temp = temp.next
        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    linked_list = LinkedList()
    node_1 = Node('a')
    linked_list.head = node_1
    node_2 = Node('b')
    node_3 = Node('c')
    node_1.next = node_2
    node_2.next = node_3
    head = linked_list.head
    # node_3.next = node_2
    # linked_list.reverse_linkedList()
    # linked_list.printList()

    # print(linked_list.is_infinite())
    # linked_list2 = LinkedList()
    # print(linked_list)
    # linked_list.reverse_linkedList()
    print(linked_list.head)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
