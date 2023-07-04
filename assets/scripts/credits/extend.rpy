label bank_credits_extend:
    t "What credit do you want to extend?"

    python:
        credits_menu = []

        for i in range(len(bank.variables.credits)):
            credit = bank.variables.credits[i]

            if credit.last_extension == 0:
                credit_str = "{image=main_purple.png} " if credit.time <= 3 else " "
                credit_str += bank.variables.credits[i].str_extend()
                credits_menu.append((credit_str, i))

        credits_menu.append(("Nevermind", -1))
        choice = renpy.display_menu(credits_menu)
        chosen_credit = bank.variables.credits[choice]

        if choice == -1:
            renpy.jump("bank_main")

        chosen_credit = bank.variables.credits[choice]

        if chosen_credit.last_extension != 0:
            renpy.say(t, f"You can't extend this credit until the current extension runs out. You still need to wait {chosen_credit.last_increase}.")
            renpy.jump("bank_credits_extend")
        
        cost = int(chosen_credit.raw_amount * chosen_credit.interests)
        amount_in_weeks = int(renpy.input(f"You currently have {CCOIN} credits. It will cost you {cost} credits for a week. How many weeks do you want to extend?", allow="0123456789"))
        cost *= amount_in_weeks
        amount = cost

        if amount_in_weeks == 0:
            renpy.say(t, "You can't extend your credit for 0 weeks.")
            renpy.jump("bank_credits_extend")
        elif amount_in_weeks > 2:
            renpy.say(t, "You can't extend your credit for more than 2 weeks.")
            renpy.jump("bank_credits_extend")

        if amount > CCOIN:
            renpy.say(t, "You don't have enough money.")
            renpy.jump("bank_credits_extend")
        else:
            confirmation_menu = [
                ("Yes", True),
                ("No", False)
            ]
            renpy.say(t, f"You will have to pay {cost} credits for {amount_in_weeks} week{'s' if amount_in_weeks > 1 else ''}. Are you sure?"),
            confirmation = renpy.display_menu(confirmation_menu)

            if not confirmation:
                renpy.say(t, "Credit not extended.")
                renpy.jump("bank_credits_extend")
            
            days = 7 * amount_in_weeks
            chosen_credit.time += days
            chosen_credit.last_extension = days
            renpy.say(t, "Credit extended.")

        renpy.jump("bank_main")
