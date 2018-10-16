
from easygui import *
import sys
while 1:
    msgbox("Hello, coustomer!")

    msg ="from which site do you want to purchase?"
    title = "shopping"
    choices = ["amazon", "flipkart"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "Survey Result")
    if choice=="amazon":
        msg1 ="choose your preferrance"
        title1 = "shopping"
        choices1 = ["electronics"]
        choice1 = choicebox(msg, title, choices)
        msgbox("You chose: " + str(choice1), "Survey Result")
        if choice1=="electronics":
            msg ="choose your preferrance"
            title2 = "shopping"
            choices2 = ["mobiles"]
            choice2 = choicebox(msg, title, choices)
            msgbox("You chose: " + str(choice2), "Survey Result")
            if choice2=="mobiles":
                msg ="choose your preferrance"
                title3 = "shopping"
                choices3 = ["samsung"]
                choice3 = choicebox(msg, title, choices)
                msgbox("You chose: " + str(choice3), "Survey Result")
                if choice3=="samsung":
                    msg ="choose your preferrance"
                    title4 = "shopping"
                    choices4 = ["j6"]
                    choice4 = choicebox(msg, title, choices)
                    msgbox("You chose: " + str(choice4), "Survey Result")
                    if choice4=="j6":
                        msg ="choose your preferrance"
                        title5 = "shopping"
                        choices5 = ["N ELEC", "A ELEC"]
                        choice5 = choicebox(msg, title, choices)
                        msgbox("You chose: " + str(choice5), "Survey Result")
                        if choice5=="N ELEC":
                           msgbox("You chose: " + str(choice5), "rs.17000")
                        else:
                           msgbox("You chose: " + str(choice5),"rs.17500")
 if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
 else:
        sys.exit(0)

