from unittest import TestCase

from lotto.src.model.AutoLottoGenerator import AutoLottoGenerator


class TestAutoLottoGenerator(TestCase):

    def test_create(self):
        self.assertIsNotNone(AutoLottoGenerator())

    def test_lottos(self):
        # given
        count = 3
        # when
        lottos = AutoLottoGenerator().lottos(count)
        # then
        self.assertEquals(count, len(lottos))
