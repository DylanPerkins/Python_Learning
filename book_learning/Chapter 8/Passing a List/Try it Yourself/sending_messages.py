# Try it Yourself 8-10

# Task:
# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_messages(texts, sent_messages):
    for text in texts:
        print(text)
        sent_messages.append(text)


texts = ['good morning, how did you sleep?', 'how are you feeling today?', 'did you end up going to that party?']
sent_messages = []
send_messages(texts, sent_messages)
print(sent_messages)