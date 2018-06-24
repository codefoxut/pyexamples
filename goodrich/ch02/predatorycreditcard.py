from creditcard import CreditCard


class PredatoryCreditCard(CreditCard):
    __slots__ = '_apr'
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new credit card instance.

        The initial balance is zero.

        :param customer: the name of the customer (e.g. 'John Bawman')
        :param bank: The name of the bank (e.g. 'California Savings')
        :param acnt: the account identifier (e.g. '5678 9012 1234 5678')
        :param limit: credit limit (measured in dollars)
        :param apr: annual percentage rate(e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)   # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge was denied.
        """
        success = super().charge(price)    # call inherited method
        if not success:
            self._balance += 5                                      # assess penalty
        return success                                              # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == '__main__':
    print("Here!!!!")
