from googletrans import Translator
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='te', show_all=True)

    except:
        return ''

    if 'alternative' in query:
        transcript = query['alternative'][0]['transcript'].lower()
    return transcript.lower()


def translate(Text):
    line = str(Text)
    translator = Translator()
    res = translator.translate(line)
    return res.text

if __name__ == '__main__':
    rs = listen()
    print(translate(rs))





