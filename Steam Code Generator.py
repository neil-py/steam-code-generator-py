## Import random module
## Thank you for checking out my code!! you can reach me via email (provided in README.md)
import random

## Character for generation
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def steam_codeGen():
    format = input("What format do you prefer?:\n(1) for XXXXX-XXXXX-XXXXX,\n(2) for XXXXX-XXXXX-XXXXX-XXXXX-XXXXX\n")
    amount_codes = int(input("How many codes do you want to generate?: \n"))

    ## If user input = "1", format XXXXX-XXXXX-XXXXX will be generated
    if format == "1":
        while True:
            print("Here's your code: ")
            for i in range(0, amount_codes):

                ## String arranged based on the format
                code = f"{random.choices(char, k=5)}-{random.choices(char, k=5)}-{random.choices(char, k=5)}"

                ## Removes unnecessary elements
                st = code.replace("'", "")
                com = st.replace(",", "")
                spc = com.replace(" ", "")
                closing = spc.replace("[", "")
                opening = closing.replace("]", "")
                print(opening)
            return

    ## If user input = "2", format XXXXX-XXXXX-XXXXX-XXXXX-XXXXX will be generated
    else:
        while True:
            print("Here's your code: ")
            for i in range(0, amount_codes):

                ## String arranged based on the format
                code = f"{random.choices(char, k=5)}-{random.choices(char, k=5)}-{random.choices(char, k=5)}-" \
                       f"{random.choices(char, k=5)}-{random.choices(char, k=5)}"

                ## Removes unnecessary elements
                st = code.replace("'", "")
                com = st.replace(",", "")
                spc = com.replace(" ", "")
                closing = spc.replace("[", "")
                opening = closing.replace("]", "")
                print(opening)
            return

steam_codeGen() #Execute
