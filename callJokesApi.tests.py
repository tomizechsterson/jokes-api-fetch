from unittest import TestCase
from callJokesApi import JokesApiCaller


class TestJokesApiCalls(TestCase):

    def test_caller_default(self):
        j = JokesApiCaller()
