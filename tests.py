import unittest
from logics import get_empty_list, get_number_from_index, get_index_from_number, is_zero_in_mas, move_left, \
    move_up, move_down, can_move

class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_number_from_index(1,2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3,3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
           ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
           ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        a = []
        mas = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
           ]
        self.assertEqual(get_empty_list(mas), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(7), (1,2))

    def test_7(self):
        self.assertEqual(get_index_from_number(16), (3,3))

    def test_8(self):
        self.assertEqual(get_index_from_number(1), (0,0))

    def test_9(self):
        a = []
        mas = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
           ]
        self.assertEqual(is_zero_in_mas(mas), False)
    
    def test_10(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
           ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11(self):
        a = []
        mas = [
            [1, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 0]
           ]
        self.assertEqual(is_zero_in_mas(mas), True)


    def test_12(self):
        a = []
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
           ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 12))

    def test_13(self):
        a = []
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
           ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]

        self.assertEqual(move_left(mas), (rez, 32))

    def test_14(self):
        a = []
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
           ]
        rez = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.assertEqual(move_up(mas), (rez, 24))

    def test_15(self):
        a = []
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
           ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4]
        ]

        self.assertEqual(move_down(mas), (rez, 24))

    def test_16(self):
        a = []
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
           ]

        self.assertEqual(can_move(mas), True)

    def test_17(self):
        a = []
        mas = [
            [2, 4, 0, 3],
            [6, 7, 8, 9],
            [5, 4, 1, 10],
            [11, 12, 13, 14]
           ]

        self.assertEqual(can_move(mas), False)


if __name__== '__main__':
    unittest.main()