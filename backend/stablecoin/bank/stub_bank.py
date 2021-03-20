from bank.bank import Bank


class StubBank(Bank):
    def __str__(self):
        pass

    def get_post_callback_routes(self):
        return {}

    def create_payment_request(self, amount, payment_id):
        return {
            "paymentRequestToken": payment_id,
            "payment_id": payment_id,
            "url": "https://tudelft.nl"
        }

    def payment_request_status(self, identifier):
        return {}

    def attempt_payment_done(self, paymentRequestToken):
        print("Payment done")
        return paymentRequestToken

    def initiate_payment(self, account, amount):
        return None

    def list_transactions(self, account):
        pass

    def get_available_balance(self):
        pass
