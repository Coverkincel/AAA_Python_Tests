import pytest
from morse import encode, decode

# Тесты для функции decode


@pytest.mark.parametrize("test_input,expected", [
    (".... . .-.. .-.. ---", "HELLO"),
    ("-- --- .-. ... .  -.-. --- -.. .", "MORSE CODE"),
    ("-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.",
     "MAI-PYTHON-2019")
])
def test_decode(test_input, expected):
    assert decode(test_input) == expected

# Тесты для функции encode


@pytest.mark.parametrize("test_input,expected", [
    ("HELLO", ".... . .-.. .-.. ---"),
    ("MORSE CODE", "-- --- .-. ... .  -.-. --- -.. ."),
    ("MAI-PYTHON-2019",
     "-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.")
])
def test_encode(test_input, expected):
    assert encode(test_input) == expected
