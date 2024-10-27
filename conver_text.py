import pyttsx3
import datetime

tts = pyttsx3.init()

genders = {'man' : 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',
           'woman' : "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
           'rus' : 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'}
gen = 'rus'

#set a setings


class speaker:
    def choose_voise(lang : str,gen = "men"):#choose voise' gender
        global language
        global gender
        language = lang
        if lang == 'en':
            tts.setProperty('voice', genders[gen])
            gender = gen
        elif lang == 'ru':
            gender = 'rus'
            tts.setProperty('voice', genders['rus'])

    def speak(txt : str, save = False, f_name = str(datetime.datetime.now())):#say and save speach
        tts.say(txt)
        if save:
            tts.save_to_file(text=txt, filename=f_name,name=f_name)
        tts.runAndWait()

    def set_parameters(self, volume: float = -1, speed: float = -1, language: str = 'a') -> None:
        if language != 'a':
            tts.setProperty('voice', language)
        if speed != -1:
            tts.setProperty('rate', speed)
        if volume != -1:
            tts.setProperty('volume', volume)
