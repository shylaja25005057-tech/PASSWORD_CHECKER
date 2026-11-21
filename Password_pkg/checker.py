"""Advanced Password Strength Checker."""

from dataclasses import dataclass
import math
import re


COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "letmein",
    "welcome123", "iloveyou", "abc12345",
    "11111111"
}

SEQUENTIAL_PATTERNS = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop"
)


@dataclass
class PasswordReport:
    strength: str
    score: int
    maximum_score: int
    length: int
    character_variety: int
    has_lowercase: bool
    has_uppercase: bool
    has_digit: bool
    has_symbol: bool
    has_minimum_length: bool
    has_recommended_length: bool
    has_long_length: bool
    is_common: bool
    has_repeated_run: bool
    has_sequence: bool
    estimated_entropy_bits: float
    feedback: list

    @property
    def score_percentage(self):
        return round(
            (self.score / self.maximum_score) * 100
        )


def check_length(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    return len(password) >= 8


def character_score(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    score = 0

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    return score


def contains_sequence(password):
    for pattern in SEQUENTIAL_PATTERNS:
        doubled = pattern + pattern

        for i in range(len(pattern)):
            sequence = doubled[i:i + 4]

            if sequence in password:
                return True

    return False


def estimate_character_pool(lower, upper, digit, symbol):
    pool = 0

    if lower:
        pool += 26

    if upper:
        pool += 26

    if digit:
        pool += 10

    if symbol:
        pool += 33

    return pool


def generate_feedback(
    length,
    lower,
    upper,
    digit,
    symbol,
    common,
    repeated,
    sequence
):
    suggestions = []

    if length < 8:
        suggestions.append(
            "Use at least 8 characters."
        )
    elif length < 12:
        suggestions.append(
            "Increase the length to 12 or more characters."
        )
    elif length < 16:
        suggestions.append(
            "Consider using a longer passphrase."
        )

    if not lower:
        suggestions.append(
            "Include lowercase letters."
        )

    if not upper:
        suggestions.append(
            "Include uppercase letters."
        )

    if not digit:
        suggestions.append(
            "Consider including numbers."
        )

    if not symbol:
        suggestions.append(
            "Consider including special characters."
        )

    if common:
        suggestions.append(
            "Avoid common and predictable passwords."
        )

    if repeated:
        suggestions.append(
            "Avoid repeating the same character many times."
        )

    if sequence:
        suggestions.append(
            "Avoid simple sequences such as abcd or 1234."
        )

    if not suggestions:
        suggestions.append(
            "Good password length and character variety."
        )

    suggestions.append(
        "Never reuse passwords. Use a password manager."
    )

    return suggestions


def analyze_password(password):

    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if not password:
        return PasswordReport(
            "No Password", 0, 10, 0, 0,
            False, False, False, False,
            False, False, False,
            False, False, False,
            0.0,
            ["Please enter a password."]
        )

    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(not c.isalnum() for c in password)

    variety = sum([lower, upper, digit, symbol])

    length = len(password)

    minimum = length >= 8
    recommended = length >= 12
    long_length = length >= 16

    common = password.casefold() in COMMON_PASSWORDS

    repeated = bool(
        re.search(r"(.)\1{3,}", password)
    )

    sequence = contains_sequence(
        password.casefold()
    )

    score = 0

    if minimum:
        score += 1

    if recommended:
        score += 1

    if long_length:
        score += 1

    score += variety

    if not common:
        score += 1

    if not repeated:
        score += 1

    if not sequence:
        score += 1

    if common:
        score = min(score, 2)

    pool = estimate_character_pool(
        lower, upper, digit, symbol
    )

    entropy = (
        length * math.log2(pool)
        if pool > 1 else 0
    )

    feedback = generate_feedback(
        length,
        lower,
        upper,
        digit,
        symbol,
        common,
        repeated,
        sequence
    )

    if length < 8 or common:
        strength = "Weak"

    elif score >= 9 and length >= 12:
        strength = "Strong"

    elif score >= 6:
        strength = "Moderate"

    else:
        strength = "Weak"

    return PasswordReport(
        strength,
        score,
        10,
        length,
        variety,
        lower,
        upper,
        digit,
        symbol,
        minimum,
        recommended,
        long_length,
        common,
        repeated,
        sequence,
        round(entropy, 1),
        feedback
    )


def strength_result(password):
    return analyze_password(password).strength