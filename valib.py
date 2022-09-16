import pyttsx3
import msvcrt as m

def wait():
    m.getch()


APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)



def speak(audio):
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()


