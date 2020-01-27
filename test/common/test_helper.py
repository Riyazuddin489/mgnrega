import unittest
import mock
import enum
from common.helper import raw_data_to_table, Menu, Key
import sys

class HelperTest(unittest.TestCase):

    @mock.patch('builtins.print')
    @mock.patch('common.helper.PrettyTable')
    @mock.patch('common.connect_db.sqlite3.connect')
    def test_raw_data_to_table(self, mock_cursor, mock_table, mock_print):
        raw_data = [[1, 2], [3, 4]]
        mock_cursor.cursor().description.return_value = ['a', 'b']
        raw_data_to_table(raw_data, mock_cursor.cursor)
        self.assertEqual(mock_table().add_row.call_count, 2)
        mock_print.assert_called_once()

    def test_on_press_up(self):
        mock_press_key = mock.Mock()
        mock_press_key.name = 'up'
        menu = Menu()
        menu.count = 3
        menu.on_press(mock_press_key)
        assert menu.index, 3

    def test_on_press_down(self):
        mock_press_key = mock.Mock()
        mock_press_key.name = 'down'
        menu = Menu()
        menu.count = 3
        menu.on_press(mock_press_key)
        assert menu.index, 0

    @mock.patch('common.helper.Key')
    def test_on_press_enter(self, mock_key):
        mock_press_key = mock_key.enter
        menu = Menu()
        menu.count = 3
        menu.on_press(mock_press_key)
        assert menu.flag, 1

    @mock.patch('common.helper.Listener')
    def test_draw_menu(self, mock_listener):
        menu = Menu()
        items = ['first', 'second', 'EXIT']
        menu.index = 1
        menu.flag = 1
        result = menu.draw_menu(items)
        assert result, items[1]


if __name__ == '__main__':
    unittest.main()
