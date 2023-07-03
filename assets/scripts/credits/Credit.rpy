init python:
    class Credit:
        def __init__(self, amount, time, interests = bank.config.credits.interests):
            self.raw_amount = amount
            self.amount_with_interests = amount + amount * interests
            self.time = time
            self._interests = interests
            self.last_increase = bank.config.credits.days_between_interests
            self.last_extension = 0

        def get_interests(self):
            return self._interests

        def set_interests(self, interests):
            self._interests = interests
            self.amount = self.amount_with_interests

        interests = property(get_interests, set_interests)

        def __str__(self):
            return f"{self.time} days remaining\nAmount: {int(self.amount)}\nInterest: {round(self.interests * 100, 2)}%"

        def str_extend(self):
            return f"{self.time} days remaining\nPrice per week: {int(self.raw_amount * self.interests)}\nInterest: {round(self.interests * 100, 2)}%"

        def get_amount(self):
            return self.amount_with_interests

        def set_amount(self, raw_amount):
            raw = int(raw_amount)
            self.raw_amount = raw
            self.amount_with_interests = int(raw + raw * self.interests)

        amount = property(get_amount, set_amount)

        def check_interests(self):
            self.last_increase -= 1

            if self.last_increase == 0:
                self.increase_interests()

        # Formula for the interests to go up
        def increase_interests(self):
            self.interests *= 2
            self.last_increase = days_between_interests

        def extend(self, weeks):
            self.time += 7 * weeks
