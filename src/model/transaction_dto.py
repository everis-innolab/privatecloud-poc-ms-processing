class TransactionDTO(object):

    def __init__(self, _id=None, client_country=None, client_id=None,
                 commerce_tpv=None, client_credit_card=None,
                 transaction_amount=None, commerce_id=None,
                 client_country_name=None, commerce_country=None,
                 commerce_country_name=None, commerce_account_iban=None,
                 transaction_datetime=None):
        self.___id = _id
        self.__client_country = client_country
        self.__client_id = client_id
        self.__commerce_tpv = commerce_tpv
        self.__client_credit_card = client_credit_card
        self.__transaction_amount = transaction_amount
        self.__commerce_id = commerce_id
        self.__client_country_name = client_country_name
        self.__commerce_country = commerce_country
        self.__commerce_country_name = commerce_country_name
        self.__commerce_account_iban = commerce_account_iban
        self.__transaction_datetime = transaction_datetime

##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def _id(self):
        return self.___id

    @property
    def client_country(self):
        return self.__client_country

    @property
    def client_id(self):
        return self.__client_id

    @property
    def commerce_tpv(self):
        return self.__commerce_tpv

    @property
    def client_credit_card(self):
        return self.__client_credit_card

    @property
    def transaction_amount(self):
        return self.__transaction_amount

    @property
    def commerce_id(self):
        return self.__commerce_id

    @property
    def client_country_name(self):
        return self.__client_country_name

    @property
    def commerce_country(self):
        return self.__commerce_country

    @property
    def commerce_country_name(self):
        return self.__commerce_country_name

    @property
    def commerce_account_iban(self):
        return self.__commerce_account_iban

    @property
    def transaction_datetime(self):
        return self.__transaction_datetime

##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @client_country.setter
    def client_country(self, client_country):
        self.__client_country = client_country

    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id

    @commerce_tpv.setter
    def commerce_tpv(self, commerce_tpv):
        self.__commerce_tpv = commerce_tpv

    @client_credit_card.setter
    def client_credit_card(self, client_credit_card):
        self.__client_credit_card = client_credit_card

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        self.__transaction_amount = transaction_amount

    @commerce_id.setter
    def commerce_id(self, commerce_id):
        self.__commerce_id = commerce_id

    @client_country_name.setter
    def client_country_name(self, client_country_name):
        self.__client_country_name = client_country_name

    @commerce_country.setter
    def commerce_country(self, commerce_country):
        self.__commerce_country = commerce_country

    @commerce_country_name.setter
    def commerce_country_name(self, commerce_country_name):
        self.__commerce_country_name = commerce_country_name

    @commerce_account_iban.setter
    def commerce_account_iban(self, commerce_account_iban):
        self.__commerce_account_iban = commerce_account_iban

    @transaction_datetime.setter
    def transaction_datetime(self, transaction_datetime):
        self.__transaction_datetime = transaction_datetime

    def __eq__(self, other):
        return (
            self._id == other._id and
            self.client_country == other.client_country and
            self.client_id == other.client_id and
            self.commerce_tpv == other.commerce_tpv and
            self.client_credit_card == other.client_credit_card and
            self.transaction_amount == other.transaction_amount and
            self.commerce_id == other.commerce_id and
            self.client_country_name == other.client_country_name and
            self.commerce_country == other.commerce_country and
            self.commerce_country_name == other.commerce_country_name and
            self.commerce_account_iban == other.commerce_account_iban and
            self.transaction_datetime == other.transaction_datetime
        )

    def __str__(self):
        return (
            '_id: %s\n'%str(self.___id)+
            'client_country: %s\n'%str(self.__client_country)+
            'client_id: %s\n'%str(self.__client_id)+
            'commerce_tpv: %s\n'%str(self.__commerce_tpv)+
            'client_credit_card: %s\n'%str(self.__client_credit_card)+
            'transaction_amount: %s\n'%str(self.__transaction_amount)+
            'commerce_id: %s\n'%str(self.__commerce_id)+
            'client_country_name: %s\n'%str(self.__client_country_name)+
            'commerce_country: %s\n'%str(self.__commerce_country)+
            'commerce_country_name: %s\n'%str(self.__commerce_cuontry_name)+
            'commerce_account_iban: %s\n'%str(self.__commerce_account_iban)+
            'transaction_datetime: %s\n'%str(self.__transaction_datetime)
        )