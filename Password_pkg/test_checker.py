
"""Unit tests for Password Strength Checker."""

import unittest

from password_pkg import (
    analyze_password,
    check_length,
    character_score,
    strength_result
)


class PasswordCheckerTests(unittest.TestCase):

    def test_password_length(self):
        self.assertTrue(check_length("Example123!"))
        self.assertFalse(check_length("abc"))

    def test_character_score(self):
        self.assertEqual(
            character_score("Example123!"), 4
        )

    def test_empty_password(self):
        report = analyze_password("")
        self.assertEqual(report.strength, "No Password")

    def test_weak_password(self):
        self.assertEqual(
            strength_result("abc"), "Weak"
        )

    def test_common_password(self):
        self.assertEqual(
            strength_result("password123"), "Weak"
        )

    def test_password_report(self):
        report = analyze_password("Violet-River-82!Cloud")

        self.assertEqual(report.character_variety, 4)
        self.assertTrue(report.has_minimum_length)

    def test_repeated_characters(self):
        report = analyze_password("Aaaaaaaa1!")
        self.assertTrue(report.has_repeated_run)

    def test_sequence_detection(self):
        report = analyze_password("Abcd1234!xyZ")
        self.assertTrue(report.has_sequence)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            analyze_password(None)


if __name__ == "__main__":
    unittest.main()