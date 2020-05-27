#交互_语音识别,用正则表达式对语音进行搜索
import speech_recognition
import re
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say somthing:")
    audio = recognizer.listen(source)#录音成音频

words = recognizer.recognize_google(audio)#将音频audio转成文字-->words

#用正则表达式对语音进行搜索
matches = re.search("my name is (.*)", words)#提取is后面的若干个char
if matches:
    print(f"hello, {matches[1]}.")#只要is后面第一个string单词
else:
    print("hey, you.")