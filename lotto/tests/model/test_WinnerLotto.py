from unittest import TestCase

from lotto.src.model.LottoNumber import LottoNumber
from lotto.src.model.WinnerLotto import WinnerLotto
from lotto.tests.model.test_Lotto import ONE_TO_SIX_LOTTO


class TestWinnerLotto(TestCase):

    def test_create(self):
        self.assertIsNotNone(WinnerLotto(ONE_TO_SIX_LOTTO, LottoNumber(7)))

    def test_create_invalid_type_raised_type_error(self):
        self.assertRaises(TypeError, lambda: WinnerLotto('lotto', LottoNumber(7)))
        self.assertRaises(TypeError, lambda: WinnerLotto(ONE_TO_SIX_LOTTO, 7))

    def test_create_duplicate_lotto_number_raised_value_error(self):
        self.assertRaises(ValueError, lambda: WinnerLotto(ONE_TO_SIX_LOTTO, LottoNumber(1)))
