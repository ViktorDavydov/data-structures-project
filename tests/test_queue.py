# imports
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):
    """"Test class initializing"""

    def test_Node(self):
        """Class Node testing"""
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEquals(n1.data, 5)
        self.assertEquals(n2.next_node, n1)

    def test_Queue_enqueue(self):
        """Class Queue enqueue testing"""
        test_assert = Queue()
        self.assertEquals(test_assert.enqueue("Random_Inf_1"), None)
        test_assert.enqueue("Random_Inf_2")
        self.assertEquals(test_assert.head.data, "Random_Inf_1")
        self.assertEquals(test_assert.head.next_node.data, "Random_Inf_2")

    def test_Queue_dequeue(self):
        """Class Queue dequeue testing"""
        test_assert = Queue()
        test_assert.enqueue("Inf_1")
        test_assert.enqueue("Inf_2")
        test_assert.enqueue("Inf_3")
        self.assertEquals(test_assert.dequeue(), "Inf_1")
        self.assertEquals(test_assert.dequeue(), "Inf_2")
        self.assertEquals(test_assert.dequeue(), "Inf_3")
        self.assertEquals(test_assert.dequeue(), None)



if __name__ == "__main__":
    unittest.main()
