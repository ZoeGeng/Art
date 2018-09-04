import logging

from django.test import TestCase

# Create your tests here.
from utils import log

class TestLog(TestCase):
    def testLog(self):
        self.assertEquals(1, 1)
        logging.warning('1=1是ok的')

    def testUser(self):
        self.assertEquals('disen','disen')
        logging.getLogger('info').warning('haha')
