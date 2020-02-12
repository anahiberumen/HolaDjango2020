from django.test import TestCase

class TestSmoke(TestCase):
    def test_smoke_Test(self):
        self.assertEqual(2+2,4)
