from unittest import TestCase, main
'''
Test driven development develops tests before the code is implemented
'''

from custom_list.custom_list import CustomIntList, CUSTOM_DATA_INDEX_ERROR_MESSAGE, CUSTOM_INDEX_ERROR_MESSAGE, \
    NoElementInListError, NoSuchValueError


class TestCustomIntList(TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomIntList()

    def test_append_adds_an_element_at_the_end_of_the_list(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

    def test_add_non_int_raises(self):
        with self.assertRaises(ValueError)as ex:
            self.custom_list.append("5")
        self.assertEqual("Only ints are expected", str(ex.exception))

    def test_remove_element_invalid_index_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as err:
            self.custom_list.remove(0)
        self.assertEqual("Invalid index", str(err.exception))

    def test_pass_invalid_integer_to_remove_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as err:
            self.custom_list.remove("0")
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(err.exception))

    def test_remove_element_removes_and_returns(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)
        returned_element = self.custom_list.remove(0)
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.assertEqual(5, returned_element)

    def test_get_returns_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

        element = self.custom_list.get(0)
        self.assertEqual(5, element)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

    def test_get_element_invalid_index_raises(self):
        self.custom_list = CustomIntList()
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

        # Pass invalid index left border
        with self.assertRaises(IndexError) as ex:
            element = self.custom_list.get(-2)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

        # Pass invalid index right border
        with self.assertRaises(IndexError) as ex:
            element = self.custom_list.get(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_extend_append_new_values(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

        self.custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)

    def test_extend_with_non_iterable_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

        with self.assertRaises(ValueError) as ex:
            self.custom_list.extend([15])
        self.assertEqual("Extend method works only with iterable objects", str(ex.exception))

    def test_extend_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.extend([5, "10"])
        self.assertEqual("Only ints are expected", str(ex.exception))

    def test_extend_returns_new_list(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)
        result_list = self.custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)
        self.assertEqual([5, 2, 3, 4], result_list)
        self.assertNotEqual(id(result_list), id(self.custom_list._CustomIntList__values))

    def test_insert_invalid_index_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(0, 5)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_insert_invalid_index_data_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.insert("0", 5)
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_insert_returns_the_list_with_inserted_element(self):
        self.custom_list.append(5)
        self.custom_list.append(10)
        self.custom_list.append(15)
        my_list = self.custom_list.insert(1, -3)
        self.assertEqual([5, -3, 10, 15], self.custom_list._CustomIntList__values)
        self.assertEqual(id(my_list), id(self.custom_list._CustomIntList__values))

    def test_pop_with_no_elements_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(NoElementInListError) as ex:
            self.custom_list.pop()
        self.assertEqual("No elements in the list", str(ex.exception))

    def test_pop_removes_and_returns_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

        el = self.custom_list.pop()
        self.assertEqual(5, el)
        self.assertEqual([], self.custom_list._CustomIntList__values)

    def test_clear_no_element_returns_empty_list(self):
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomIntList__values)

    def test_clear(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.assertEqual([5, 15], self.custom_list._CustomIntList__values)

        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomIntList__values)

    def test_index_left_returns_left_most_index_of_the_element(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.custom_list.append(5)

        index = self.custom_list.index_left(5)
        self.assertEqual(0, index)

    def test_index_left_returns_right_most_index_of_the_element(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.custom_list.append(5)

        index = self.custom_list.index_right(5)
        self.assertEqual(2, index)

    def test_index_left_invalid_value_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(NoSuchValueError) as ex:
            self.custom_list.index_left(5)
        self.assertEqual("No such value in the list", str(ex.exception))

    def test_index_right_invalid_value_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(NoSuchValueError) as ex:
            self.custom_list.index_right(5)
        self.assertEqual("No such value in the list", str(ex.exception))

    def test_count_no_such_value(self):
        self.custom_list.append(10)
        self.assertEqual([10], self.custom_list._CustomIntList__values)

        count = self.custom_list.count(5)
        self.assertEqual(0, count)

    def test_count(self):
        self.custom_list.append(10)
        self.custom_list.append(5)
        self.custom_list.append(10)
        self.assertEqual([10, 5, 10], self.custom_list._CustomIntList__values)

        count = self.custom_list.count(10)
        self.assertEqual(2, count)

        count = self.custom_list.count(5)
        self.assertEqual(1, count)

    def test_empty_list_returns_list(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.reverse()
        self.assertEqual([], self.custom_list._CustomIntList__values)

    def test_reverse_reverses_values_in_list(self):
        self.custom_list.append(10)
        self.custom_list.append(5)
        self.assertEqual([10, 5], self.custom_list._CustomIntList__values)
        result = self.custom_list.reverse()
        # the original list reamins unchanged
        self.assertEqual([10, 5], self.custom_list._CustomIntList__values)
        # the new list is reversed
        self.assertEqual([5, 10], result)

    def test_copy_returns_the_same_elements_in_different_list(self):
        self.custom_list.append(10)
        self.custom_list.append(5)

        result = self.custom_list.copy()
        self.assertEqual([10, 5], result)
        self.assertNotEqual(id(result), id(self.custom_list._CustomIntList__values))

    def test_size_returns_elements_count(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        count = self.custom_list.size()
        self.assertEqual(0, count)

        self.custom_list.append(10)
        self.custom_list.append(5)
        self.assertEqual([10, 5], self.custom_list._CustomIntList__values)
        count = self.custom_list.size()
        self.assertEqual(2, count)

    def test_add_first_no_element_append(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.add_first(5)
        self.assertEqual([5], self.custom_list._CustomIntList__values)

    def test_add_first_adds_element_in_front(self):
        self.custom_list.append(10)
        self.custom_list.append(5)
        self.assertEqual([10, 5], self.custom_list._CustomIntList__values)
        self.custom_list.add_first(-3)
        self.assertEqual([-3, 10, 5], self.custom_list._CustomIntList__values)

    def test_add_fist_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.add_first("5")
        self.assertEqual("Only ints are expected", str(ex.exception))

    def test_dictionize_odd_count(self):
        self.custom_list.append(10)
        self.custom_list.append(5)
        self.custom_list.append(15)

        result = self.custom_list.dictionize()
        expected_result = {10: 5, 15: " "}
        self.assertEqual(result, expected_result)

    def test_dictionize_even_count(self):
        self.custom_list.append(10)
        self.custom_list.append(5)

        result = self.custom_list.dictionize()
        expected_result = {10: 5}
        self.assertEqual(result, expected_result)

    def test_move_moves_n_values_at_the_end(self):
        self.custom_list.append(5)
        self.custom_list.append(10)
        self.custom_list.append(15)
        self.custom_list.append(20)
        self.assertEqual([5, 10, 15, 20], self.custom_list._CustomIntList__values)

        result = self.custom_list.move(2)
        self.assertEqual([15, 20, 5, 10], self.custom_list._CustomIntList__values)
        self.assertEqual([15, 20, 5, 10], result)

    def test_sum_(self):
        self.custom_list.append(5)
        self.custom_list.append(10)
        self.custom_list.append(15)
        self.custom_list.append(20)
        self.assertEqual([5, 10, 15, 20], self.custom_list._CustomIntList__values)

        result = self.custom_list.sum()
        self.assertEqual(50, result)

    def test_overbound(self):
        self.custom_list.append(5)
        self.custom_list.append(20)
        self.custom_list.append(10)
        self.custom_list.append(15)
        self.assertEqual([5, 20, 10, 15], self.custom_list._CustomIntList__values)

        res = self.custom_list.overbound()
        self.assertEqual(20, res)

    def test_underbound(self):
        self.custom_list.append(5)
        self.custom_list.append(20)
        self.custom_list.append(10)
        self.custom_list.append(15)
        self.assertEqual([5, 20, 10, 15], self.custom_list._CustomIntList__values)

        res = self.custom_list.underbound()
        self.assertEqual(5, res)

if __name__ == '__main__':
    main()
