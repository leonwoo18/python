#交互_语音识别,并做出反应
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say somthing:")
    audio = recognizer.listen(source)#录音成音频

words = recognizer.recognize_google(audio)#将音频audio转成文字-->words
#作出反应
if "hello" in words:
    print("hello to you too!")
elif "how are you" in words:
    print("I am well, thanks!")
elif "goodbye" in words:
    print("goodbye to you too!")
else:
    print("huh?")