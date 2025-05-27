
import unittest
from password_generator import generate_random_password
import string

class TestPasswordGenerator(unittest.TestCase):

    def test_password_default_length(self):
        """Перевірка, що довжина пароля за замовчуванням — 28 символів"""
        password = generate_random_password()
        self.assertEqual(len(password), 28)

    def test_password_custom_length(self):
        """Перевірка, що функція підтримує довільну довжину"""
        length = 50
        password = generate_random_password(length)
        self.assertEqual(len(password), length)

    def test_password_characters_validity(self):
        """Перевірка, що всі символи пароля входять у дозволений набір"""
        password = generate_random_password()
        allowed_chars = string.ascii_letters + string.punctuation + string.digits
        for char in password:
            self.assertIn(char, allowed_chars)

    def test_password_not_empty(self):
        """Пароль не повинен бути порожнім"""
        password = generate_random_password()
        self.assertTrue(len(password) > 0)

if __name__ == '__main__':
    unittest.main()
