import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Source(1, "bbc","author")
    
    def test_instance(self):
        self.assertEquals(self.new_source, Source)
