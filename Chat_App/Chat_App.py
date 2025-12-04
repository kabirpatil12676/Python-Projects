class User:
    def __init__(self,name):
        self.name = name

class Message:
    def __init__(self,sender,text):
        self.sender = sender
        self.text = text

    
class ChatRoom:
    def __init__(self,room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self,user):
        self.users.append(user)
        print(f"{user.name} joined {self.room_name}")

    def leave(self,user):
        if user in self.user:
            self.users.remove(user)
            print(f"{user.name} left {self.room_name}")
    
    def send_message(self,sender,text):
        if sender in self.user:
            msg = Message(sender.name,text)
            self.messages.append(msg)

        else:
            print(f"{sender.name} is not in the chat room!")

    def show_chat_history(self):
        print(f"\n--- Chat History in {self.room_name} ---")
        for msg in self.messages:
            print(f"{msg.sender}: {msg.text}")
        print("----------------------------------\n")



u1 = User("Kabir")
u2 = User("Pratiksha")
u3 = User("Alok")

chat = ChatRoom("Friends Chat")

chat.join(u1)
chat.join(u2)

chat.send_message(u1, "Hi everyone!")
chat.send_message(u2, "Hello Kabir! 😄")

chat.join(u3)
chat.send_message(u3, "Hey, I’m here too!")

chat.show_chat_history()

chat.leave(u2)