import pyttsx3

#Carregando a lib
engine = pyttsx3.init()

#Texto que a engine vai falar
engine.say("olá, como vai?")
engine.say("Você acaba de converter texto em áudio com Python")


#Exec

engine.runAndWait()
