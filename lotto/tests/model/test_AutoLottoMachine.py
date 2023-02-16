from unittest import TestCase

from lotto.src.model.AutoLottoMachine import AutoLottoMachine


class TestAutoLottoMachine(TestCase):

    def test_create(self):
        self.assertIsNotNone(AutoLottoMachine())

    def test_lottos(self):
        # given
        count = 3
        # when
        lottos = AutoLottoMachine().lottos(count)
        # then
        self.assertEqual(count, len(lottos))
