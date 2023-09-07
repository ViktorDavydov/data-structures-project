import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def test_Node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEquals(n1.data, 5)
        self.assertEquals(n2.next_node, n1)

    def test_Stack(self):
        test_assert = Stack()
        self.assertEquals(test_assert.top, None)
        self.assertEquals(test_assert.push("Random Inf"), None)
        test_assert.push("Random_Inf_1")
        self.assertEquals(test_assert.top.data, "Random_Inf_1")


if __name__ == "__main__":
    unittest.main()
