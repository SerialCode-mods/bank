label bank_credits_repay:
    t "What credit do you want to repay?"

    python:
        credits_list = []

        for i in range(len(bank.variables.credits)):
            credit = bank.variables.credits[i]
            credit_str = "{image=main_purple.png} " if credit.time <= 3 else " "
            credit_str += str(bank.variables.credits[i])
            credits_list.append((credit_str, i))

        credits_list.append(("Nevermind", -1))
        choice = renpy.display_menu(credits_list)
        chosen_credit = bank.variables.credits[choice]

        if choice == -1:
            renpy.jump("bank_main")

    menu:
        "All at once":
            if CCOIN < chosen_credit.amount:
                t "You don't have enough money."
                jump bank_credits_repay

            $ bank.variables.credits.remove(chosen_credit)

            t "Credit repaid."
            jump bank_main

        "Variable amount":
            t "How much do you want to repay?"

            $ amount = int(renpy.input(f"You currently have [CCOIN] money. You need to repay {int(chosen_credit.amount)} credits", allow="0123456789"))

            if amount > CCOIN:
                t "You don't have enough money."
                jump bank_credits_repay
            elif amount > credit.amount:
                t "You can't repay more than you owe."
                jump bank_credits_repay
            elif amount < credit.amount:
                $ credit.amount -= amount
                t "Credit partially repaid."
            else:
                $ bank.variables.credits.remove(chosen_credit)
                t "Credit repaid."

        "Nevermind":
            jump bank_end
