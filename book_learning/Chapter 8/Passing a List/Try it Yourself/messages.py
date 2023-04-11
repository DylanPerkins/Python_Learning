# Try it Yourself 8-9

# Task:
# Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def print_messages(texts):
    for text in texts:
        print(text)
    
texts = ['good morning, how did you sleep?', 'how are you feeling today?', 'did you end up going to that party?']
print_messages(texts)

