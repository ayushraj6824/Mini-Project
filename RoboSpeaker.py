import pyttsx3
engine = pyttsx3.init()
while True:
    x=input("Enter what you want me to speak: ")
    if x=="exit":
        engine.say("Bye bye")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()