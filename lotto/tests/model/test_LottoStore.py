from unittest import TestCase

from lotto.src.model.AutoLottoMachine import AutoLottoMachine
from lotto.src.model.LottoStore import LottoStore
from lotto.src.model.Money import Money
from parameterized import parameterized


class TestLottoStore(TestCase):

    def test_create(self):
        self.assertIsNotNone(LottoStore(AutoLottoMachine()))

    @parameterized.expand([[Money(500), 0], [Money(1000), 1], [Money(3500), 3]])
    def test_purchased_lottos(self, money: Money, expected_count: int):
        # when
        purchased_lottos = LottoStore(AutoLottoMachine()).purchased_lottos(money)
        # then
        self.assertEqual(expected_count, len(purchased_lottos))
