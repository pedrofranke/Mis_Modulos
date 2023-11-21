class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node
        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        self.head_node = new_head
        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node
        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node = new_tail
        if self.head_node == None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node
        if removed_head == None:
            return None
        self.head_node = removed_head.get_next_node()
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        if removed_head == self.tail_node:
            self.remove_tail()
        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail == None:
            return None
        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if removed_tail == self.head_node:
            self.remove_head()
        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node
        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()
        if node_to_remove == None:
            return None
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_node_beginning(self,new_node):
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_node_pos(self,new_node,pos):
        current = self.get_head_node()
        count = 1
        while count < pos-1:
            current = current.get_next_node()
            count +=1
        new_node.set_next_node(current.get_next_node())
        current.set_next_node(new_node)

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_all(self,value_to_remove):
        current_node = self.get_head_node()
        previous = None
        while current_node != None:
            if current_node.get_value() == value_to_remove:
                if previous == None:
                    self.head_node = current_node.get_next_node()
                else:
                    previous.set_next_node(current_node.get_next_node())
            previous = current_node
            current_node = current_node.get_next_node()
    
    def swap_nodes(self,node1,node2):
        current_node = self.get_head_node()
        previous = None
        while current_node != node1 and current_node:
            previous = current_node
            current_node = current_node.get_next_node()
        first_node = current_node
        pre_first_node = previous
        current_node = self.get_head_node()
        previous = None
        while current_node != node2 and current_node:
            previous = current_node
            current_node = current_node.get_next_node()
        if current_node and first_node:
            aux = first_node.get_next_node()
            if previous != None:
                previous.set_next_node(first_node)
            else:
                self.head_node = first_node
            if pre_first_node != None:
                pre_first_node.set_next_node(current_node)
            else:
                self.head_node = current_node
            first_node.set_next_node(current_node.get_next_node())
            current_node.set_next_node(aux)
        else:
            print(f'One node was not found, node1: {first_node}, node2: {current_node}')

    def get_n_last_node(self,index_number):
        lista = []
        current = self.get_head_node()
        while current:
            lista.append(current)
            current = current.get_next_node()
        return lista[len(lista)-index_number]
    
    def get_n_node_wtail(self,index_number):
        current = None
        tail_seeker = self.get_head_node()
        count = 0
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= index_number:
                if current == None:
                    current = self.get_head_node()
                else:
                    current = current.get_next_node()
        return current
    
    def get_fraction_node(self,fraction):
        current = None
        tail_seeker = self.get_head_node()
        count = 1
        while tail_seeker != None:
            tail_seeker = tail_seeker.get_next_node()
            if count%fraction == 0:
                if current == None:
                    current = self.get_head_node()
                else:
                    current = current.get_next_node()
            count += 1
            if tail_seeker == None and fraction == 2 and count%2==0:
                current = current.get_next_node()
        return current
    
