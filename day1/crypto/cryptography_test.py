import unittest
from cryptography import rot13


class CryptographyTest(unittest.TestCase):
    def test_can_encrypt_single_letter(self):
        self.assertEqual(rot13("a"), "n")

    def test_can_encrypt_single_uppercase_letter(self):
        self.assertEqual(rot13("A"), "N")

    def test_raises_error_non_letter_input(self):
        with self.assertRaises(TypeError):
            rot13(1)

    def test_raises_error_alphanumeric_input(self):
        with self.assertRaises(TypeError):
            rot13("a1")

    def test_can_encrypt_two_letter_input(self):
        self.assertEqual(rot13("aa"), "nn")

    def test_can_encrypt_two_letter_uppercase_input(self):
        self.assertEqual(rot13("AA"), "NN")

    def test_can_encrypt_two_words(self):
        self.assertEqual(rot13("a b"), "n o")

    def test_can_encrypt_sentence(self):
        self.assertEqual(rot13("This is a SeNtEnCe"), "Guvf vf n FrAgRaPr")


if __name__ == "__main__":
    unittest.main()
