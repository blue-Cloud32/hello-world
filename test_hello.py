#! /usr/bin/env python3
import unittest
from hello import hello_world


class Test_(unittest.TestCase):

    def test_1(self) -> None:
        """_summary_
        """
        result = hello_world()
        answer = "Hello World!"
        self.assertEqual(result, answer)

    def test_2(self) -> None:
        """_summary_
        """
        result = hello_world()+" My name is bob!"
        answer = "Hello World! My name is bob!"
        self.assertEqual(result, answer)

    def test_3(self) -> None:
        """_summary_
        """
        result = hello_world()+hello_world()
        answer = "Hello World!Hello World!"
        self.assertEqual(result, answer)

    def test_4(self) -> None:
        """_summary_
        """
        result = hello_world()
        answer = "Hello World!"
        self.assertEqual(result, answer)

    def test_5(self) -> None:
        """_summary_
        """
        result = hello_world()
        answer = "Hello World!"
        self.assertEqual(result, answer)
