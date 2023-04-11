# Try it Yourself 8-11

# Task:
# Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.

def send_messages(texts, sent_messages):
    for text in texts:
        print(text)
        sent_messages.append(text)


texts = ['good morning, how did you sleep?', 'how are you feeling today?', 'did you end up going to that party?']
sent_messages = []
send_messages(texts[:], sent_messages)
print(texts) # Retains values of it's original instancing