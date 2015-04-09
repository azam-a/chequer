from chequer import (
    get_decimals,
    get_digits,
    is_all_zero,
    is_first_digit_zero,
    parse_five_digits,
    parse_four_digits,
    parse_single_digit,
    parse_three_digits,
    parse_two_digits,
    )

import unittest


class GetDigitsGetDecimalsTest(unittest.TestCase):

    def test_get_digits_for_number_with_no_decimals(self):
        self.assertEqual(get_digits('123'), '123')

    def test_get_digits_for_number_with_decimals(self):
        self.assertEqual(get_digits('456.78'), '456')

    def test_get_decimals_for_number_with_decimals(self):
        self.assertEqual(get_decimals('321.45'), '45')

    def test_get_decimals_for_number_with_no_decimals(self):
        self.assertEqual(get_decimals('567'), None)


class DictComparator(unittest.TestCase):

    def compare(self, function):

        for keys in self.expected_results.keys():
            self.assertEqual(function(keys), self.expected_results[keys])


class ZeroTest(DictComparator):

    def test_is_all_zero(self):
        self.expected_results = {
            '0': True, '1': False,
            '00': True, '01': False, '11': False,
            '000': True, '001': False, '010': False}
        self.compare(is_all_zero)

    def test_is_first_digit_zero(self):
        self.expected_results = {
            '0': True, '1': False,
            '00': True, '01': True, '10': False,
            '000': True, '010': True, '100': False}


class ParseSingleDigitTest(DictComparator):

    def test_1_to_9(self):
        self.expected_results = {
            '1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat',
            '5': 'lima', '6': 'enam', '7': 'tujuh', '8': 'lapan',
            '9': 'sembilan', '0': None}
        self.compare(parse_single_digit)


class ParseTwoDigitsTest(DictComparator):

    def test_exact_multiple_of_10s(self):
        self.expected_results = {
            '10': 'sepuluh', '20': 'dua puluh', '30': 'tiga puluh',
            '40': 'empat puluh', '50': 'lima puluh', '60': 'enam puluh',
            '70': 'tujuh puluh', '80': 'lapan puluh', '90': 'sembilan puluh'}
        self.compare(parse_two_digits)

    def test_teens(self):
        self.expected_results = {
            '11': 'sebelas', '12': 'dua belas', '13': 'tiga belas',
            '14': 'empat belas', '15': 'lima belas', '16': 'enam belas',
            '17': 'tujuh belas', '18': 'lapan belas', '19': 'sembilan belas'}
        self.compare(parse_two_digits)

    def test_non_10_multiples_non_teen(self):
        self.expected_results = {
            '00':  None,
            '01': 'satu',
            '53': 'lima puluh tiga', '99': 'sembilan puluh sembilan',
            '87': 'lapan puluh tujuh', '26': 'dua puluh enam'}
        self.compare(parse_two_digits)


class ParseThreeDigitsTest(DictComparator):

    def test_random_three_digits(self):
        self.expected_results = {
            '000':  None,
            '003': 'tiga',
            '010': 'sepuluh',
            '111': 'satu ratus sebelas',
            '153': 'satu ratus lima puluh tiga',
            '400': 'empat ratus',
            '530': 'lima ratus tiga puluh',
            '712': 'tujuh ratus dua belas'}
        self.compare(parse_three_digits)


class ParseFourDigitsTest(DictComparator):

    def test_random_four_digits(self):
        self.expected_results = {
            '0000':  None,
            '0005': 'lima',
            '0020': 'dua puluh',
            '0100': 'satu ratus',
            '1000': 'satu ribu',
            '1111': 'satu ribu satu ratus sebelas',
            '2500': 'dua ribu lima ratus',
            '3470': 'tiga ribu empat ratus tujuh puluh',
            '4313': 'empat ribu tiga ratus tiga belas',
            '9001': 'sembilan ribu satu'}
        self.compare(parse_four_digits)


class ParseFiveDigitsTest(DictComparator):

    def test_random_five_digits(self):
        self.expected_results = {
            '00000':  None,
            '00010': 'sepuluh',
            '00100': 'satu ratus',
            '01000': 'satu ribu',
            '10000': 'sepuluh ribu',
            '11000': 'sebelas ribu',
            '13050': 'tiga belas ribu lima puluh',
            '15001': 'lima belas ribu satu',
            '21567': 'dua puluh satu ribu lima ratus enam puluh tujuh',
            '31702': 'tiga puluh satu ribu tujuh ratus dua'}
        self.compare(parse_five_digits)
