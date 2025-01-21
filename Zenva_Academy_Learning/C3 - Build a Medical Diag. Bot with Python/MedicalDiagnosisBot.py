# Prompts
welcome_prompt = """
\nWelcome Doctor, what would you like to do today?
\n1. List all patients
\n2. Run a new diagnosis
\n3. Exit selection menu
\n"""

name_prompt = "Please enter the patient's name:\n"

appearance_prompt = """Please select the patient's appearance:
\n1. Normal
\n2. Irriatble or lethargic
\n"""

eye_prompt = """Please select the patient's eye condition:
\n1. Normal or slightly sunken
\n2. Very sunken
\n"""

skin_prompt = """Please select the patient's skin condition after pinching:
\n 1. Normal
\n 2. Slow to return to normal
\n"""

invalid_option = "~~Invalid option selected. Please try again.~~"

# Dehydration levels
severe_dehydration = "Severe Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"

patients_and_diagnosis = [
    "John - Severe Dehydration",
    "Mary - Some Dehydration",
    "Bob - No Dehydration"
]

def main():
    flag = True
    while flag:
        selected_option = input(welcome_prompt)
        if selected_option == "1":
            # List all patients
            list_patients()
        elif selected_option == "2":
            # Start a new diagnosis
            run_diagnosis()
        elif selected_option == "3":
            # Exit the program
            flag = False
            return
        else:
            print(invalid_option)
            main()


# List all patients
def list_patients():
    for patient in patients_and_diagnosis:
        print(patient)

# Save a new diagnosis
def save_diagnosis(name, diagnosis):
    final_diagnosis = name + " - " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print("Final Diagnosis: " + final_diagnosis + "\n")



# Functions for running a new diagnosis
def run_diagnosis():
    # Run a new diagnosis
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_diagnosis(name, diagnosis)

# Assess the appearance of their skin or eyes
def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        # Normal
       eyes = input(eye_prompt)
       return assess_eyes(eyes)
    elif appearance == "2":
        # Irriatble or lethargic
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        print(invalid_option)
        assess_appearance()

# Assess the skin
def assess_skin(skin):
    if skin == "1":
        # Normal
        return some_dehydration
    elif skin == "2":
        # Slow to return to normal
        return severe_dehydration
    else:
        print(invalid_option)
        assess_skin(skin)

# Assess the eyes
def assess_eyes(eyes):
    if eyes == "1":
        # Normal or slightly sunken
        return no_dehydration
    elif eyes == "2":
        # Very sunken
        return severe_dehydration
    else:
        print(invalid_option)
        assess_eyes(eyes)


main()
