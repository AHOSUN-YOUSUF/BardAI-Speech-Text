# This Code runs the ChatBOT
def main():
    from BardAI_Speech_Text import main_bard_chatbot
    from os import path

    filename =  path.basename(__file__)

    if filename == "Main.PY":
        main_bard_chatbot()

main()
