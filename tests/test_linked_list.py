# imports
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """"Test class initializing"""

    def test_LinkedList_to_list(self):
        """Class LinkedList to_list method testing"""
        test_linked_list_1 = LinkedList()
        test_linked_list_1.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        test_linked_list_1.insert_at_end({'id': 2, 'username': 'mik.roz'})

        self.assertEquals(test_linked_list_1.to_list(), [{'id': 1, 'username': 'lazzy508509'},
                                                         {'id': 2, 'username': 'mik.roz'}])

        test_linked_list_1.insert_at_end({'id': 3, 'username': 'mosh_s'})
        test_linked_list_1.insert_beginning({'id': 0, 'username': 'serebro'})

        self.assertEquals(test_linked_list_1.to_list(), [{'id': 0, 'username': 'serebro'},
                                                         {'id': 1, 'username': 'lazzy508509'},
                                                         {'id': 2, 'username': 'mik.roz'},
                                                         {'id': 3, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        """Class LinkedList get_data_by_id method testing"""
        test_linked_list_2 = LinkedList()
        test_linked_list_2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        test_linked_list_2.insert_at_end('idusername')
        test_linked_list_2.insert_at_end([1, 2, 3])
        test_linked_list_2.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEquals(test_linked_list_2.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})

    def test_type_error(self):
        """TypeError raising testing"""
        test_linked_list_2 = LinkedList()
        test_linked_list_2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        test_linked_list_2.insert_at_end('idusername')
        test_linked_list_2.insert_at_end([1, 2, 3])
        test_linked_list_2.insert_at_end({'id': 2, 'username': 'mosh_s'})
        with self.assertRaises(TypeError):
            test_linked_list_2.get_data_by_id(2)


if __name__ == "__main__":
    unittest.main()
