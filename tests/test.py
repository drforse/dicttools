import unittest
from dicttools import KeyTools


class TestTools(unittest.TestCase):

    d = {
        'name':
            'drforse',
        'language':
            'python',
        'age':
            19,
        'friends':
            {
                'kotlinistas':
                    [
                        {
                            'name':
                                'senderman',
                            'age':
                                None
                        },
                        {
                            'name':
                                'gbball',
                            'age':
                                None
                        }
                    ],
                'pythonistas':
                    [
                        {
                            'name':
                                'p0lunin',
                            'age':
                                None
                        },
                        {
                            'name':
                                'Loshadkin',
                            'age':
                                None
                        }
                    ]
            }
        }

    def test_iter_all_keys(self):
        """
        iter_all_keys test
        """

        awaited_return = ['name', 'language', 'age', 'friends', 'kotlinistas', 'name', 'age', 'name', 'age', 'name',
                          'age', 'name','age', 'pythonistas', 'name', 'age', 'name', 'age', 'name', 'age', 'name', 'age']
        generator = KeyTools.iter_all_keys(dictionary=self.d)
        result = [i for i in generator]
        self.assertListEqual(result, awaited_return)

    def test_edit_all_keys(self):
        """
        edit_all_keys test
        """

        awaited_return = {'nxme': 'drforse', 'lxnguxge': 'python', 'xge': 19, 'friends': {
            'kotlinistxs': [{'nxme': 'senderman', 'xge': None}, {'nxme': 'gbball', 'xge': None}],
            'pythonistxs': [{'nxme': 'p0lunin', 'xge': None}, {'nxme': 'Loshadkin', 'xge': None}]
        }}

        def replace(s, to_replace, replacement):
            return s.replace(to_replace, replacement)

        modified_dict = KeyTools.edit_all_keys(obj=self.d, function=replace, to_replace='a', replacement='x')
        self.assertDictEqual(modified_dict, awaited_return)


if __name__ == '__main__':
    unittest.main()
