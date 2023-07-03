label bank:
    label .prepare:
        # Config
        define bank.config.credits.days_between_interests = 3
        define bank.config.credits.interests = 0.1

        # Variables
        default bank.variables.credits = []
        default bank.variables.bank_index = -1
        default bank.variables.twatch_index= -1
        
        define bank_application = {
            "tooltip": "Bank",
            "idle": "mods/bank/images/stos/bank.png",
            "hover": "mods/bank/images/stos/bank_hover.png",
            "label": "bank_main"
        }

        # Applications indexes
        define bank.variables.bank_index = -1
        define bank.variables.twatch_index = -1

        return

    label .load:
        $ config.label_overrides.update({
            "sleep": "bank_sleep",
            "sleep2": "bank_sleep2",
        })

        return

    label .after:
        $ bank.variables.bank_index = find_index_of_application("bank_main")

        $ bank.variables.bank_index = find_index_of_application("bank_main")

        # Check if mod is already loaded (can happen in a case of reload for example)
        if bank.variables.bank_index > -1:
            return

        $ bank.variables.twatch_index = find_index_of_application("twatch_main")
        $ applications[bank.variables.twatch_index + 1] = bank_application
        $ swap_applications("twatch_main", "bank_main")

        return

    label .unload:
        $ print("Unloading bank")

        $ bank.variables.bank_index = find_index_of_application("bank_main")
        $ bank.variables.twatch_index = find_index_of_application("twatch_main")

        if bank.variables.bank_index > -1:
            $ del applications[bank.variables.bank_index]

        if bank.variables.twatch_index > bank.variables.bank_index:
            $ swap_applications("bank_main", "twatch_main")

        return
