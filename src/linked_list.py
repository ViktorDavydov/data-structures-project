class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = self.tail = ""

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head == "":
            self.head = self.tail = Node(data, None)
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data, None)
        if self.tail == "":
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def to_list(self):
        """List of nodes generator initializing"""
        data_list = []
        temp_node = self.head
        while temp_node:
            data_list.append(temp_node.data)
            temp_node = temp_node.next_node
        return data_list

    def get_data_by_id(self, id_index):
        """Node finder by id initializing with exception invalid node type"""
        new_list = LinkedList.to_list(self)
        for item in new_list:
            try:
                isinstance(item["id"], int)
            except TypeError:
                # raise TypeError
                print(f"Данные не являются словарем или в словаре нет id.")
            else:

                if item["id"] == id_index:
                    return item

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
