#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from lib.snowball_stemmer_sentence import SnowballStemmerSentence

class TestSnowballStemmerSentence(TestCase):
    def setUp(self):
        self.test_data = ["Szeretném"]
        self.subject = SnowballStemmerSentence(self.test_data)

    def test_sentence(self):
        self.assertEqual(self.subject.sentence, self.test_data)

    def test_result(self):
        self.assertEqual(self.subject.result(), [u'szeretne'])