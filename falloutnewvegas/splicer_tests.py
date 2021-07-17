import splicer
import unittest

class TestStringMethods(unittest.TestCase):
    def test_choosetwocombinations_1arg_fail(self):
        en = 'en'
        de = 'de'
        es = 'es'
        tuples = splicer.create_all_choose_two_combinations(en, de, es)
        self.assertCountEqual(tuples, [(en, de), (en, es), (de, en), (de, es), (es,
            en), (es, de)])

    def test_choosetwocombinations_3args_success(self):
        en = 'en'
        de = 'de'
        es = 'es'
        tuples = splicer.create_all_choose_two_combinations(en, de, es)
        self.assertCountEqual(tuples, [(en, de), (en, es), (de, en), (de, es), (es,
            en), (es, de)])

if __name__ == '__main__':
    unittest.main()
