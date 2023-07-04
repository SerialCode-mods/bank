init python:
    # Wallpaper utils
    def get_wallpaper(id):
        filtered_wallpapers = filter(lambda w: w["id"] == id, wallpapers)

        return next(filtered_wallpapers)

    # applications utils
    class Blank:
        idle = "images/stos/blank.png"
        hover = "images/stos/blank.png"

    def pad_applications(length):
        global applications
        applications.extend([Blank] * (length - len(applications)))

    def twatch_check():
        return MariMentionedStream == True

    dock_length = 13
    applications = [
        { "tooltip": "My Computer", "idle": "images/stos/mypc.png", "hover": "images/stos/mypc_hover.png", "label": "MySystem" },
        { "tooltip": "App Store", "idle": "images/stos/appstore.png", "hover": "images/stos/appstore_hover.png", "label": "AppStore" },
        { "tooltip": "AuraLink Settings", "idle": "images/stos/aura.png", "hover": "images/stos/aura_hover.png", "label": "AuraSettings" },
        { "tooltip": "Ultrasploit Terminal", "idle": "images/stos/hack.png", "hover": "images/stos/hack_hover.png", "label": "CompHackingMenu" },
        { "tooltip": "Browser", "idle": "images/stos/search.png", "hover": "images/stos/search_hover.png", "label": "ResearchComputer" },
        { "tooltip": "CGC GOTY Edition", "idle": "images/stos/catbutton.png", "hover": "images/stos/catbutton_hover.png", "label": "Clicker" },
        { "tooltip": "Twatch.tv", "idle": "images/stos/tv.png", "hover": "images/stos/tv_hover.png", "label": "twatch_main", "condition": twatch_check }
    ]
    pad_applications(dock_length)
    applications.append({ "tooltip": "Wait", "idle": "images/stos/wait.png", "hover": "images/stos/wait_hover.png", "label": "waitinSTOS" })

    def find_index_of_application(label: str):
        for index, app in enumerate(applications):
            if app is not Blank and app["label"] == label:
                return index

        return -1

    def swap_applications(_from, to):
        global applications
        from_index = find_index_of_application(_from)
        to_index = find_index_of_application(to)  

        if from_index == -1 or to_index == -1:
            return

        applications[from_index], applications[to_index] = applications[to_index], applications[from_index]

        return


# Wallpapers
default wallpapers = [
    { "id": 1, "path": "images/stos/suwonwall.png" },
    { "id": 2, "path": "images/stos/ceresWALL.png" },
    { "id": 3, "path": "images/stos/armitageWALL.png" },
    { "id": 4, "path": "images/stos/seawall.png" },
    { "id": 5, "path": "images/stos/upskirtwall.png" },
    { "id": 6, "path": "images/stos/bunnywall.png" },
    { "id": 7, "path": "images/stos/felwall.png" },
    { "id": 8, "path": "images/stos/doublewall.png" },
    { "id": 9, "path": "images/stos/doggywall.png" },
    { "id": 10, "path": "images/stos/pinupwall.png" },
    { "id": 11, "path": "images/stos/footwall.png" },
    { "id": 12, "path": "images/stos/neko1wall.png" },
    { "id": 13, "path": "images/stos/neko2wall.png" },
    { "id": 14, "path": "images/stos/teasewall.png" },
    { "id": 15, "path": "images/stos/sakurawall.png" },
    { "id": 96, "path": "images/stos/rileyspotlight.png", "append": ["gui/darken50.png"] },
    { "id": 96, "path": "images/stos/MariSpot.png" },
    { "id": 97, "path": "images/stos/ErikaMain.png" },
    { "id": 98, "path": "anim/empty_menu.png" },
    { "id": 98, "path": "anim/empty_menu.png", "append": ["menu_movie"] },
    { "id": 100, "path": "menu_movie2", "append": ["gui/darken50.png"] },
    { "id": 199, "path": "crackedpc" }
]

screen STOS:
    $ wallpaper = get_wallpaper(WallpaperChoice)
    add wallpaper["path"]

    for append in wallpaper.get("append", []):
        add append

    if DeveloperMode == True:
        textbutton "TestRoom CombatInit" action Jump("CombatInitTestroom") yalign 0.1
        textbutton "DevMenu" action Call("DevMenu") yalign 0.2
        textbutton "InvBackEnd" action ShowMenu("invdisplay") yalign 0.3
        textbutton "HS_NumberMini" action Call("numbers_game") yalign 0.4
        textbutton "HS_NumberMini2" action Call("krix") yalign 0.5

    add "images/stos/top_status_bar.png"
    imagebutton idle "images/stos/shutdown_idle.png" hover "images/stos/shutdown_hover.png" action Jump("LeaveSTOS") xalign 1.0
    text "[dayoftheweek], [Time] {image=cal.png} [day]" font "fonts/Montserrat-SemiBold.ttf" xalign 0.5 yalign 0.01 size 24

    hbox:
        xalign 0.32
        yalign 0.995
        frame:
            padding (15, 0, 15, 5)
            xalign 0.5
            yalign 1.0
            xsize 1200
            background "gui/frame2.png"
            hbox:
                xoffset 4
                spacing 11.2

                for application in applications:
                    if application is Blank:
                        imagebutton idle Blank.idle hover Blank.hover
                    else:
                        $ has_condition = "condition" in application

                        # If the condition doesn't pass, make it blank
                        if has_condition == True and application["condition"]() == False:
                            imagebutton idle Blank.idle hover Blank.hover
                        else:
                            imagebutton:
                                tooltip application["tooltip"]
                                idle application["idle"]
                                hover application["hover"]
                                action Jump(application["label"])

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                background None
                xalign 0.5
                yoffset -10
                text tooltip
