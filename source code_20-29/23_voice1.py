#交互_语音识别
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say somthing:")
    audio = recognizer.listen(source)#录音成音频

print("google speech recognition thinks you said:")
print(recognizer.recognize_google(audio))#将音频audio转成文字