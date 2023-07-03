label bank_main:
    t "Welcome, what can we help you with?"

    menu:
        "Take on credit":
            jump bank_get_credit

        "Repay a credit" if len(bank.variables.credits) > 0:
            jump bank_repay_credit

        "Extend a credit" if len(bank.variables.credits) > 0:
            jump bank_extend_credit

        "Nevermind":
            jump bank_end
