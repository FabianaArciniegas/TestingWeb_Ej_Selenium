import unittest


class Operations(unittest.TestCase):

    def test_suma(self):
        sum = 1 + 1
        self.assertEqual(sum, 2, msg="El resultado de la suma es correcto = 2")

    def test_resta(self):
        rest = 1 - 1
        self.assertNotEqual(rest, 2)

    def test_isMayus(self):
        self.assertTrue("COURSE".isupper())
        self.assertFalse("course".isupper())


if __name__ == "__main__":
    unittest.main()
