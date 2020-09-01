def test_string_a(self):
    self.assertEqual('m'*4, 'mmmm')

def test_isupper(self):
    self.assertTrue('MER'.isupper())
    self.assertFalse('Mer'.isupper())
