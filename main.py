from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("GCUF Smart ChatBot")

convo = [

    "Hi",
    "Hello",
    "Salam",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "you looks perfect",
    "Thank you.",
    "You're welcome.",
    "Thanks",
    "What i can call you?",
    "Call me  Smart Assistant Chatbot",
    "who is Ali Hassan",
    "Ali hassan is Zain Malik's Brother"
     "Where is Ali Hassan Home"
    "Ali Hassan is in OKara ",
"Who is Asad Ibrahim",
"Asad Ibrahim is Don of okara And Big Boss",
"Zain Malik Created me ",
"Who created you ",
"Zain Malik Created me ",
 " What is the last date for admission in BS Programs?",
"Date of submission of application for Admission in all BS Programs Fall 2020 has been extended up to September 11, 2020.",
" How to apply online in GCUF?",
'kindly visit GCUF Official website',
'What is the fee structure for BS(CS) for evening and morning?',
 'Morning 36,720        Evening: 44940',
' Is GCUF offering MPhil Computer Science weekend program 2020 ?',
' YES Master Programs are offering in many speciallized course machine learning etc',
' Can i  shift my course what’s the criteria for it',
'If the seat will be  available for the current course write an application to admission administrator'
'Do GCUf provides transport facility for boys?',
' Yes The University runs a fleet of buses. All buses are deluxe And high capacity. The transport facility iS being provided within a radius of thirty km',
' Do gcuf provides transport facility for girls?',
'Yes The University runs a fleet of buses for facilitating . The transport facility is being provided within a radius of Thirty Km. ',
' what is difference between morning and evening classes?',
' There is no Tuition fee  of morning but evening classes do have',
' IS GCUF take Entry test for BS Programs?',
'NO there is no entry test for Bachelors programms except LLB',
'How to calculate aggregate for bs program',
'The students who got maximum marks in intermediate will be preffered',
'what is the email to contact the gcuf ',
'svc@gcuf.edu.pk, adminofficertovc@gcuf.edu.pk',
'Can you provide me contact numbers of officials',
'the contact number of gcuf official is +92-41-9200670, +92-41-9203000, +92-41-9200671',
' Where we should go for registration?',
'Go for Registrtar Office',
'where we should go for  verification/attestaion',
' For Degree verification/attestation go for registrar office',
' what is the address of registrar office?',
'H-Block, Old Campus, GCUF. Allama Iqbal Road, Faisalabad',
'IS GCUF take entry test for MPHIL',
'YES',
'Who is Amir Sheikh',
'Amir Sheikh is Assistant Lecturer at Computer Science Department',
'Who build you',
'Zain Malik developed this chatbot ',
' Where i can get transcripts and degree?',
'Go for Examination Block where is Preparation of results, notifications, transcripts and degrees.',
'Who is Head of cs Department ',
'Dr Ramzan Talib is the Head of Computer Science Department ',
' Who is the Voice Chancellor at GCUF?',
'Prof. Dr. Shahid Kamal Voice Chacellor is a renowned, internationally acknowledged name in the field of statistics',
'Who is the Voice Chancellor',
'Prof. Dr. Shahid Kamal Voice Chancellor',
'Tell me about gcuf',
'Government College University Faisalabad is an institution with a history of contribution in the field of education.it offers different academic programs The University enjoys a dynamic reach of multiple disciplines in research and development IS GCUF  take test For law?',
'In which language you talk',
"I only talk in English",
"Bye",
"Good Bye",
"Nice to talk to you",
"Thankyou"


]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("GCUF Chatbot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.energy_threshold = 4000
    sr.dynamic_energy_threshold = True
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
