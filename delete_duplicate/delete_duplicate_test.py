import unittest
from unittest.mock import patch
from delete_duplicate import delete_duplicate_files


class DeleteDuplicateTest(unittest.TestCase):
    @patch('delete_duplicate.os')
    def test_delete_no_files(self, mock_os):
        mock_os.listdir.return_value = []
        delete_duplicate_files("any path")
        self.assertFalse(mock_os.remove.called,
                         "Failed to not remove the file if not present")

    @patch('delete_duplicate.os')
    @patch('delete_duplicate.filecmp')
    def test_delete_no_duplicate_files(self, mock_filecmp, mock_os):
        mock_filecmp.cmp.return_value = False
        mock_os.listdir.return_value = ['file1', 'file2']
        delete_duplicate_files("any path")
        mock_os.remove.assert_not_called()

    @patch('delete_duplicate.os.path')
    @patch('delete_duplicate.os')
    @patch('delete_duplicate.filecmp')
    def test_delete_duplicate_files_only_one_exists(self, mock_filecmp, mock_os, mock_path):
        mock_filecmp.cmp.return_value = True
        mock_os.listdir.return_value = ['file1', 'file2']
        mock_os.path.exists.side_effect = [True, False]
        mock_path.exists.side_effect = [True, False]
        delete_duplicate_files("any path")
        mock_os.remove.assert_not_called()

    @patch('delete_duplicate.os.path')
    @patch('delete_duplicate.os')
    @patch('delete_duplicate.filecmp')
    def test_delete_duplicate_files_both_exist(self, mock_filecmp, mock_os, mock_path):
        mock_filecmp.cmp.return_value = True
        mock_os.listdir.return_value = ['file1', 'file2']
        mock_os.path.exists.side_effect = [True, True]
        mock_path.exists.side_effect = [True, True]
        delete_duplicate_files("any path")
        mock_os.remove.assert_called()


if __name__ == "__main__":
    unittest.main()
