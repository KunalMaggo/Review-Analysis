from datetime import datetime as dt

helloIntent = ["hello","hi","hey","hey there","hi there","hello there"]
dateIntent = ["date today","today's date","date please","tell me date","date"]
queryIntent = ["queries","i need queries","query","1","1."]
timeIntent = ["tell me time","current time","please tell me time","time"]
aboutIntent = ["about","about you","about us","what about"]
contactIntent = ["contact","contact us","contact you","contact number"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hello User! How can i help you?   \n1.Query")
    elif msg in queryIntent:
        print("What do you need to know? \n1.Yojanas \n2.About Us \n3.Contact")
    elif msg in timeIntent:
        c_time = dt.now().time()
        print(c_time.strftime("%H:%M:%S,%p"))
    elif msg in aboutIntent:
        print("We are a non-profiting antity working in acknoledging people about Government Yojanas and providing special features for people with Special needs. ")
    elif msg in contactIntent:
        print("Contact Number:  \nEmail:")
    elif msg in dateIntent:
        date = dt.now().date()
        print(date.strftime("%d/%m/%y,%a"))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
