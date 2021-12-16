import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import sys


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga")

def kapan():
    talk('Görüşürüz')
    sys.exit()

def yenilen():
    talk('tamamdır')
    os.system("main.py")

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print("Dinliyorum")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="tr-TR")
            command = command.lower()

            if 'hamza' in command:
                command = command.replace("hamza", "")
                print(command)

            else:
                take_command = False
                return command

        return command
    except:
        return command

def run_hamza():
    command = take_command()
    print(command)
    if "çal" in command:
        song = command.replace("çal", "")
        talk('oynatılıyor' + song)
        pywhatkit.playonyt(song)
    elif "saat" in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("Şu an zaman" + time)
        ##(Normalde bu kütüphane İngilizce desteklediği için konuşmada sıkıntı çıkıyor.)
   ## elif "kim" in command:
        ##     person = command.replace("kim", "")
        ##     info = wikipedia.summary(person)
        ##    print(info)
    ##talk(info)

    elif "buluşalım" in command:
        talk("üzgünüm, başım ağrıyor")
    elif "yalnız mısın" in command:
        talk("İnternetle bir ilişkim var")

        ##
        ##elif "şaka" in command:
        ##print(command)
    elif "teşekkür ederim" in command:
        talk("rica ederim, görevim")
    elif "nasılsın" in command:
        talk("ben bir botum, nasıl olduğumu bilmiyorum")

    elif "kapat kendini" in command:
        kapan()
    elif "yenilen" in command:
        yenilen()

    else:
        print("anlamadım")

while True:
    run_hamza()
