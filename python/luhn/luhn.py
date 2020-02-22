class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        result = 0
        if len(self.card_num) == 1:
            return False

        import re

        if re.search(r'[^0-9]', self.card_num):
            return False

        for x, what in enumerate(self.card_num[::-1]):
            if x % 2 == 0:
                result += int(what)
            else:
                doubled = int(what) * 2
                if doubled > 9:
                    doubled -= 9

                result += doubled

        if int(result) % 10 == 0:
            return True

        return False

