import unittest
from unittest.mock import patch, MagicMock
from Word import create_doc, add_picture, get_text_doc

class TestDocumentManager(unittest.TestCase):

    @patch('builtins.input', side_effect=['TestDoc', 'Heading 1', 'Paragraph 1', 'Heading 2', 'Paragraph 2'])
    @patch('document_manager.Document')
    def test_create_doc(self, mock_document, mock_input):
        create_doc()
        mock_document.return_value.add_heading.assert_any_call('Heading 1', level=0)
        mock_document.return_value.add_paragraph.assert_any_call('Paragraph 1')
        self.assertTrue(mock_document.return_value.save.called)

    @patch('builtins.input', side_effect=[None, None])  # Simulate entering and exiting dialogs
    @patch('document_manager.select_file', side_effect=['/path/to/picture.jpg', '/path/to/document.docx'])
    @patch('document_manager.Document')
    def test_add_picture(self, mock_document, mock_select_file, mock_input):
        add_picture()
        mock_document.return_value.add_picture.assert_called_once_with('/path/to/picture.jpg', width=1.5, height=1.5)
        self.assertTrue(mock_document.return_value.save.called)

    @patch('builtins.input', return_value=None)
    @patch('document_manager.select_file', return_value='/path/to/document.docx')
    @patch('document_manager.Document')
    def test_get_text_doc(self, mock_document, mock_select_file, mock_input):
        mock_document.return_value.paragraphs = [MagicMock(text='Line 1'), MagicMock(text='Line 2')]
        text = get_text_doc()
        self.assertIn('Line 1', text)
        self.assertIn('Line 2', text)

if __name__ == '__main__':
    unittest.main()
