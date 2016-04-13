import unittest

from working_jsons import add_new_entry

__author__ = 'josebermudez'


class TestWorkingJSONs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestWorkingJSONs, self).__init__(*args, **kwargs)

        self.month = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender":
                {
                    "F":
                        {
                            "count": 5,
                            "amount": 225,
                            "num_items": 7
                        },
                    "M":
                        {
                            "count": 10,
                            "amount": 200,
                            "num_items": 5
                        }
                },
            "currency":
                {
                    "EUR":
                        {
                            "count": 13,
                            "amount": 175,
                            "num_items": 6
                        },
                    "USD":
                        {
                            "count": 2,
                            "amount": 250,
                            "num_items": 6
                        }
                }
        }

        self.entry = {
            "gender": "M",
            "amount": 17.0,
            "num_items": 2,
            "currency": "EUR"
        }

    def test_month_none(self):
        month = None
        self.assertRaises(ValueError, add_new_entry, month=month, entry=self.entry)

    def test_entry_none(self):
        entry = None
        self.assertRaises(ValueError, add_new_entry, month=self.month, entry=entry)

    def test_example(self):
        expected_response = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender":
                {
                    "F":
                        {
                            "count": 5,
                            "amount": 225,
                            "num_items": 7
                        },
                    "M":
                        {
                            "count": 11,
                            "amount": 217,
                            "num_items": 7
                        }
                },
            "currency":
                {
                    "EUR":
                        {
                            "count": 14,
                            "amount": 192,
                            "num_items": 8
                        },
                    "USD":
                        {
                            "count": 2,
                            "amount": 250,
                            "num_items": 6
                        }
                }
        }
        self.assertEqual(add_new_entry(month=self.month, entry=self.entry), expected_response)

    def test_new_currency(self):
        entry = {
            "gender": "M",
            "amount": 17.0,
            "num_items": 2,
            "currency": "GBP"
        }
        expected_response = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender":
                {
                    "F":
                        {
                            "count": 5,
                            "amount": 225,
                            "num_items": 7
                        },
                    "M":
                        {
                            "count": 11,
                            "amount": 217,
                            "num_items": 7
                        }
                },
            "currency":
                {
                    "EUR":
                        {
                            "count": 13,
                            "amount": 175,
                            "num_items": 6
                        },
                    "USD":
                        {
                            "count": 2,
                            "amount": 250,
                            "num_items": 6
                        },
                    "GBP":
                        {
                            "count": 1,
                            "amount": 17,
                            "num_items": 2
                        }
                }
        }
        self.assertEqual(add_new_entry(month=self.month, entry=entry), expected_response)
