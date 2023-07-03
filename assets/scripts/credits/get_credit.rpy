label bank_credits_take:
    if len(bank.variables.credits) > 3:
        t "You already have 3 bank.variables.credits. You can't take any more."
        jump bank_main

    menu:
        "500":
            $ bank.variables.credits.append(Credit(500, 10))
            $ CCOIN += 500
            t "Credit taken. You have 10 days to repay it."
            jump bank_main

        "1000":
            $ bank.variables.credits.append(Credit(1000, 20))
            $ CCOIN += 1000
            t "Credit taken. You have 20 days to repay it."
            jump bank_main

        "10000":
            $ bank.variables.credits.append(Credit(10000, 30))
            $ CCOIN += 10000
            t "Credit taken. You have 30 days to repay it."
            jump bank_main

        "Nevermind":
            jump bank_main

    jump bank_main
