def dependencies():
    from colorama import Fore
    from os import system

    print(Fore.BLUE)
    system(str("cls"))
    system(str("python.exe -m pip install --upgrade pip"))
    system(str("python.exe -m pip install --upgrade google-generativeai"))
    system(str("python.exe -m pip install SpeechRecognition"))
    system(str("python.exe -m pip install colorama"))
    system(str("cls"))
dependencies()

def write(text):

    from time import sleep

    for char in text:
        print(
              char,
              end= str(""), 
              flush = bool(True)
             )
        sleep(float(0.05))
    print()

def bard_ai():
    from speech_recognition import (Recognizer, Microphone)
    from google.generativeai import (configure, generate_text)
    from PaLM_AUTH import PaLM_API_Key
    from colorama import Fore
    from time import time

    r = Recognizer()
    configure(api_key = PaLM_API_Key)

    print(str(" "))
    print(Fore.LIGHTGREEN_EX + str("Please say something : "))
    print(str(" "))

    with Microphone() as source:
        audio_data = r.record(source, duration = int(10))
    print(str(Fore.YELLOW + "Recognizing..........\n"))
    print(Fore.RED + str("_") * 23)

    prompt = str(r.recognize_google(audio_data))
    print(Fore.RED + str("Did you said (Before Refactoreing) : "), prompt)
    prompt_refected = generate_text(
                model = "models/text-bison-001",
                prompt = f"Add '.', ',', '!' & '?' newline & Capitalize this sentences: \n{prompt}",
                temperature = int(0),
                max_output_tokens = int(800),
    )

    print(Fore.RED + str("Did you said (After Refactoreing) : "), prompt_refected.result)
    length: int = len(prompt_refected.result) + 37
    print(Fore.LIGHTBLUE_EX + str("_") * length)

    start_time = float(time())

    answer = generate_text(
                model = "models/text-bison-001",
                prompt = prompt_refected.result,
                temperature = int(0),
                max_output_tokens = int(800),
    )

    end_time = float(time())

    print(Fore.LIGHTBLUE_EX
          + str("Response from BardAI ")
          + str("[Regponse Generated in : ")
          + f"{float(end_time - start_time)}"
          + str("]")
          + str(" :"))

    print(str(" "))
    write(Fore.LIGHTBLUE_EX + str(answer.result))

def exit_bard():
    from sys import exit
    print(str(" "))
    exit("Closing BardAI.")

while True:
    from speech_recognition import exceptions
    try:
        bard_ai()

        from colorama import Fore
        print(str(" "))
        continue_or_discontinue = input(Fore.YELLOW + str('Press "Enter" (For Windows)/ "Return" (For Mac) to ask another question or\npress "Ctrl + C" (For Windows)/"Cmd + ." (Fro Mac) to quit :\n'))
        if continue_or_discontinue == str("y"):
           continue
        if continue_or_discontinue == str("n"):
            exit_bard()

    except exceptions.UnknownValueError:
        continue

    except KeyboardInterrupt:
        exit_bard()
