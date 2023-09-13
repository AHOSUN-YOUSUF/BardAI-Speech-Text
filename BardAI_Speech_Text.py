"""
__author__ = Ahosun Yousuf
__name_project __ = BardAI-Speech-Text
__author_email__ = ahosunyousuf128@gamil.com
__author_github__ = https://github.com/AHOSUN-YOUSUF
__author_replit__ = https://replit.com/@AHOSUNULYOUSUF
"""

# Class of all the Colours you will need in the ChatBOT.
class Colours:
    from colorama import (Fore)

    Yellow = Fore.YELLOW
    Green = Fore.GREEN
    Red = Fore.RED
    Cyan = Fore.CYAN
    Blue = Fore.BLUE

# Class of all the Errors you will find in the ChatBOT.
class Errors:
    from speech_recognition import (exceptions as stt)
    from google.api_core import (exceptions as ttt)

    Error_While_Redcording = stt.UnknownValueError
    API_Err = ttt.GoogleAPIError
    Stoped_by_User = KeyboardInterrupt

# This code checkes all the dependencies to run the ChatBOT.
def dependencies():
    from os import system

    system(str("cls"))
    system(str("python.exe -m pip install --upgrade pip"))
    system(str("python.exe -m pip install --upgrade google-generativeai"))
    system(str("python.exe -m pip install --upgrade colorama"))
    system(str("cls"))

dependencies()

def get_os():
    from platform import (system as os)

    return os()

# This code makes the response look like it's writeing in the Console.
def write(text):
    from time import sleep
    for char in text:
        print(
              char,
              end = str(""),
              flush = bool(True)
             )
        sleep(float(0.05))
    print()

"""
 This code  records the user Audio Input for the time that user want to.
 Then takes the Audio Data and Transcribes into a Text Data.
 And returns The Text Data.
"""
def stt():
    from speech_recognition import (Recognizer, Microphone)

    recognizer = Recognizer()

    duration_to_record = int(input(str(Colours.Green + "Enter the duration of time to record (In Seconds) : ")))
    print(Colours.Yellow + str("Please say something (In English): "))

    with Microphone(chunk_size = 1024) as source:
        audio_data = recognizer.record(source, duration = int(duration_to_record))

    print(str(Colours.Yellow + "Recognizing the user's Speech (In English)..........\n"))
    print(Colours.Red + str("_") * 52)

    prompt = str(recognizer.recognize_google(audio_data = audio_data, language= "en-US"))

    return prompt

"""
 This code takes The Text Data sends it over https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001 url.
 And asks it to add Capitalization & Punctation to the Text Data.
 Then it takes The Capitalized & Punctuated Text Data & sends over https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001.
 And asks it to generate a resopnse using The Capitalized & Punctuated Text Data
"""
def complition(prompt: str):
    from google.generativeai import (configure, generate_text)
    from PaLM_AUTH import (PaLM_API_Key)
    from time import (time)

    configure(api_key = PaLM_API_Key)
    print(Colours.Red + str(f"Did you said (Before Correctio n) : {prompt}"))
    prompt_refected = generate_text(
                model = "models/text-bison-001",
                prompt = f"Add '.', ',', '!', '?', '<', '>', '%', '=', '+' & '-' newline & Capitalize this sentences: \n{prompt}",
                temperature = int(1),
                max_output_tokens = int(800),
    )
    print(Colours.Red + str(f"Did you said (After Correction) : {prompt_refected.result}"))

    start_time = float(time())
    answer = generate_text(
                model = "models/text-bison-001",
                prompt = prompt_refected.result,
                temperature = int(1),
                max_output_tokens = int(800),
    )
    end_time = float(time())

    print(Colours.Blue + str("_") * (int(len(prompt_refected.result)) + 37), "\n")
    print(Colours.Cyan
         + str("Response from BardAI ") 
         + str(f"[Response Generated in : {float(end_time - start_time)}]")
         + str(f" :\n{Colours.Blue}"))

    return (answer.result)

# This code is the ChatBOT.
def main_bard_chatbot():
    while (True):
        try:
            prompt = str(stt())
            comp_ans = complition(prompt = prompt)

            write(f"{comp_ans}\n")
            print(Colours.Green + str("_") * 73)

            OS_Name = get_os()

            if OS_Name == str("Windows"):
                print(Colours.Green + str('⟶ Press "Enter" to ask another question & \n⟶ Press "Ctrl + C" to quit :\n'))
                continue_or_discontinue = input()
                if continue_or_discontinue == "":
                    continue
            if OS_Name == str("Mac"):
                print(Colours.Green + str('⟶ Press "Return" to ask another question & \n⟶ Press "Cmd + ." to quit :\n'))
                continue_or_discontinue = input()
                if continue_or_discontinue == "":
                    continue
            
        except (Errors.Stoped_by_User):
            exit(Colours.Red + str("You stopped the chatbot.\n"))

        except (Errors.Error_While_Redcording):
            print(str(Colours.Red + "Sorry, I didn't understand what you said.\n"))
            continue
        
        except (Errors.API_Err):
            exit(str(Colours.Red + "Sorry, I couldn't connect to the API.\n"))