### UP TO DATE ###
# class Credit:
#     def __init__(self, balance: int, interests: float, time: int) -> None:
#         # The amount of money you currently owe before interests
#         self._raw_balance = balance

#         # How much the debt increases every day
#         self.interests = interests

#         # You REALLY need to make sure this doesn't reach 0.
#         self.time = time

#     def __str__(self, raw_balance: bool) -> str:
#         return dedent(
#             f"""
#                 Balance: {self._raw_balance if raw_balance else self.balance}
#                 Rate: {self.interests}
#                 Time: {self.time}
#             """
#         ).strip("\n")

#     def get_balance(self) -> int:
#         """Returns your current balance using current interests

#         Example:
#             Balance is 1000 and interests is 0.1 -> `debt.get_balance() -> 100`

#         Returns:
#             int: The current interests value
#         """
#         return int(self.balance + self.balance * self.interests)

#     balance = property(get_balance)

#     def get_interest(self) -> int:
#         """Returns your current interests using current balance

#         Example:
#             Balance is 1000 and interests is 0.1 -> `debt.get_interest() -> 100`

#         Returns:
#             int: The current interest
#         """
#         return int(self.balance * self.interests)
