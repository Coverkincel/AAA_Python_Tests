
from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b)
                        for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


if __name__ == '__main__':
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities


class TestFitTransform(unittest.TestCase):
    """Тестовые случаи для функции fit_transform."""

    def test_empty_input(self):
        # Проверка, что при отсутствии аргументов возникает TypeError.
        with self.assertRaises(TypeError):
            fit_transform()

    def test_single_item(self):
        # Проверка, что одиночный элемент корректно трансформируется.
        self.assertEqual(fit_transform('Москва'), [('Москва', [1])])

    def test_identical_items(self):
        """Проверка, что одинаковые элементы получают одинаковую кодировку."""
        input_data = ['Москва', 'Москва']
        expected = [
            ('Москва', [1]),
            ('Москва', [1]),
        ]
        self.assertEqual(fit_transform(*input_data), expected)

    def test_different_items(self):
        # Проверка, что разные элементы получают различную кодировку.
        input_data = ['Москва', 'Нью-Йорк']
        expected = [('Москва', [0, 1]), ('Нью-Йорк', [1, 0])]
        self.assertEqual(fit_transform(*input_data), expected)

    def test_not_in_output(self):
        # Проверка, что 'Нью-Йорк' не появляется в выходных
        # Данных для других элементов.
        input_data = ['Москва', 'Лондон']
        transformed_data = fit_transform(*input_data)
        for item in transformed_data:
            self.assertNotIn('Нью-Йорк', item[0])


if __name__ == '__main__':
    unittest.main()
