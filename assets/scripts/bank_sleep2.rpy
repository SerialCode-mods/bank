label bank_sleep2:
    call time_keeper

    centered "{size=+30}{color=#ea3c61}[dayoftheweek]{/color}, [Time] {color=#ea3c61}[day]{/color}{/size}"

    if dayoftheweek == "Monday":
        centered "{size=+30}{color=#ea3c61}New week begins.{/color}{/size}"
        if Erika_codex_unlock == True:
            call CO_BountyWeekInit

        if CryptoMiners >= 1:
            centered "Your Crypto miners have made [CrytoMinersIncomeTotal] {image=creds.png}"

        if "BookMeet" in LockedWeek:
            $LockedWeek.remove("BookMeet")

    if day == 2:
        centered "Chapter 1: {b}{i}Star stuff{/i}{/b}"

    call event_resets
    call cinit_protagonist

    if day >= 8 and timevar == 1 and "HelpHex" in BlueDreamsInd and "StarIntroSeen" not in BlueDreamsInd:
        jump StarIntroApp

    jump morning_event_action
