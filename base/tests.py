from django.test import TestCase

# Create your tests here.

class ExampleMethodTests(TestCase):

    def test_basic_example_addition(self):
        self.assertIs(1+1, 2)
    
    def test_basic_example_strings(self):
        self.assertIs("this is a test", "this is a test")
