# imports
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    """"Test class initializing"""

    def test_Node(self):
        """Class Node testing"""
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEquals(n1.data, 5)
        self.assertEquals(n2.next_node, n1)

    def test_Stack_puch(self):
        """Class Stack push testing"""
        test_assert = Stack()
        self.assertEquals(test_assert.top, None)
        self.assertEquals(test_assert.push("Random Inf"), None)
        test_assert.push("Random_Inf_1")
        self.assertEquals(test_assert.top.data, "Random_Inf_1")

    def test_stack_pop(self):
        """Class Stack pop testing"""
        test_assert = Stack()
        test_assert.push("Inf_1")
        test_assert.pop()
        self.assertEquals(test_assert.top, None)
        test_assert.push("Inf_1")
        test_assert.push("Inf_2")
        self.assertEquals(test_assert.top.data, "Inf_2")
        self.assertEquals(test_assert.top.next_node.data, "Inf_1")
        test_assert.pop()
        self.assertEquals(test_assert.top.data, "Inf_1")
        self.assertEquals(test_assert.top.next_node, None)

    def test_str(self):
        """Magic method __str__ testing"""
        test_assert = Stack()
        self.assertEquals(str(test_assert.top), "None")
        test_assert.push("Inf_1")
        self.assertEquals(str(test_assert.top.data), "Inf_1")
        test_assert.push("Inf_2")
        self.assertEquals(str(test_assert.top.next_node.data), "Inf_1")



if __name__ == "__main__":
    unittest.main()
