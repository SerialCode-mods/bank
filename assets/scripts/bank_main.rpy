label bank_main:
    t "Welcome, what can we help you with?"

    menu:
        "Take on credit":
            jump bank_credits_take

        "Repay a credit" if len(bank.variables.credits) > 0:
            jump bank_credits_repay

        "Extend a credit" if len(bank.variables.credits) > 0:
            jump bank_credits_extend

        "Nevermind":
            jump bank_end
