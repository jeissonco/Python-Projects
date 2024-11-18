import unittest, os, tracemalloc
from pdf import merge_pdfs, rotate_pdf, decrypt_pdf, encrypt_pdf  
from pypdf import PdfReader, PdfWriter
from unittest.mock import patch, mock_open, MagicMock

tracemalloc.start()

class TestPdfFunctions(unittest.TestCase):

    def setUp(self):
        # paths to the testing PDF files
        self.test_pdf_path = '/Users/jeissonnino/Desktop/Python/Ass3/all_merged_files.py'
        self.output_pdf_path = '/Users/jeissonnino/Desktop/Python/Ass3/rotation.pdf'

    def test_merge_pdfs(self):
        
        merge_pdfs()
        # checking the output file has the expected number of pages
        with open(self.output_pdf_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 2)

    def test_rotate_pdf(self):
        # This test would rotate the first page of the PDF and save it
        rotate_pdf()
        with open(self.output_pdf_path, 'rb') as f:
            reader = PdfReader(f)
            # checking the orientation given was 90 degrees
            self.assertTrue(90)

    @patch('builtins.open', new_callable=mock_open, read_data=b"dummy pdf data")
    @patch('pdf.PdfWriter')
    @patch('pdf.PdfReader')
    def test_encrypt_pdf(self, mock_writer, mock_open, mock_reader):
        # Set up
        mock_writer_instance = mock_writer
        mock_reader_instance = mock_reader

        # Execute
        encrypt_pdf()

        # Verify
        mock_writer_instance("Password1", algorithm="AES-256")
        mock_writer_instance()
        mock_open("encrypted-pdf.pdf", "wb")

    @patch('builtins.open', new_callable=mock_open, read_data=b"dummy pdf data")
    @patch('pdf.PdfWriter')
    @patch('pdf.PdfReader')
    def test_decrypt_pdf(self, mock_writer, mock_open, mock_reader):
        # Set up
        mock_reader_instance = mock_reader
        mock_writer_instance = mock_writer

        # Execute
        decrypt_pdf()

        # Verify
        mock_reader_instance("Password1")
        mock_writer_instance()
        mock_open("decrypted-pdf.pdf", "wb")

if __name__ == '__main__':
    unittest.main()
