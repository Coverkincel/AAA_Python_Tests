import urllib.request
import json
import unittest
from unittest.mock import patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 2
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock
    и извлекает из поля 'currentDateTime' год.
    Формат даты может быть 'YYYY-MM-DD' или 'DD.MM.YYYY'.
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


# Тесты для функции what_is_year_now
class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_format_ymd(self, mock_urlopen):
        # Проверка работы с форматом YYYY-MM-DD
        # (PEP8 ignored для улучшения читаемости)
        mock_urlopen.return_value.__enter__.return_value.read.return_value = '{"currentDateTime": "2023-11-13"}'
        self.assertEqual(what_is_year_now(), 2023)

    @patch('urllib.request.urlopen')
    def test_format_dmy(self, mock_urlopen):
        # Проверка работы с форматом DD.MM.YYYY
        # (PEP8 ignored для улучшения читаемости)
        mock_urlopen.return_value.__enter__.return_value.read.return_value = '{"currentDateTime": "13.11.2023"}'
        self.assertEqual(what_is_year_now(), 2023)

    @patch('urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        # Проверка обработки невалидного формата
        # (PEP8 ignored для улучшения читаемости)
        mock_urlopen.return_value.__enter__.return_value.read.return_value = '{"currentDateTime": "2023/11/13"}'
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
