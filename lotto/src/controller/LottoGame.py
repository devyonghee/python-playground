from lotto.src.model.AutoLottoMachine import AutoLottoMachine
from lotto.src.model.Lotto import Lotto
from lotto.src.model.LottoNumber import LottoNumber
from lotto.src.model.LottoStore import LottoStore, LOTTO_PRICE
from lotto.src.model.Money import Money
from lotto.src.model.WinnerLotto import WinnerLotto
from lotto.src.view.InputView import input_purchase_amount, input_winner_numbers, input_bonus_number
from lotto.src.view.OutputView import print_lottos, print_benefit_rate, print_ranks


def start():
    lottos = LottoStore(AutoLottoMachine()) \
        .purchased_lottos(Money(input_purchase_amount()))

    print_lottos(lottos)

    ranks = WinnerLotto(__input_lotto(), __input_bonus()).ranks(lottos)
    print_ranks(ranks)
    print_benefit_rate((len(lottos) * LOTTO_PRICE.value) / ranks.sum_price().value)


def __input_lotto() -> Lotto:
    return Lotto([LottoNumber(int(str_number)) for str_number in input_winner_numbers().split(',')])


def __input_bonus() -> LottoNumber:
    return LottoNumber(input_bonus_number())
