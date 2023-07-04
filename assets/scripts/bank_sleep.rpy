label bank_sleep:
    if timevar == 3:
        scene home3 with fade

        t "Time to sleep..."

        python:
            if len(bank.variables.credits) > 0:
                for credit in bank.variables.credits:
                    credit.time -= 1

                    if credit.last_extension > 0:
                        credit.last_extension -= 1

                    credit.check_interests()

                has_any_urgent_credit = any(credit.time == 1 for credit in bank.variables.credits)
                has_failed_to_repay_any_credit = any(credit.time <= 0 for credit in bank.variables.credits)

                if has_failed_to_repay_any_credit:
                    renpy.say(t, "I failed to repay some credits... I'm in trouble now.")
                    # TODO: Add an actual scene. Maybe Mariko being kidnapped, giving you one more week to repay or game over?
                    renpy.call_screen("CS_Death")
                elif has_any_urgent_credit:
                    renpy.say(t, "It's the last day for some credits, I really need to repay them quickly!")
                else:
                    renpy.say(t, "I have some credits to pay off... I should probably work a bit more.")

        scene ren_evening with dissolve
        call night_event_check
        scene black with slowdiz

    $ timevar = 1
    $ day += 1
    $ times_slept += 1

    call day_change

    if day == 3 and timevar == 1:
        jump KuroInvasion1

    if times_slept == 1:
        jump dream1
    elif times_slept == 7:
        jump dream2
