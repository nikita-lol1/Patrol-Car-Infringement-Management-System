#---CONSTANTS---



#---PROGRAM FUNCTIONS---


def get_driver_name():
    """ASKS FOR FULL NAME - Ensures alpha-only format and title case output."""
    
    is_valid = False
    driver_name = ""

    while not is_valid: # Asks for a full name and splits into 2 words
        user_input = input("Enter driver's full name: ").strip()
        parts = user_input.split()

        # Ensure at least 2 words are entered and all parts contain only letters
        if len(parts) >= 2 and parts.isalpha():
            driver_name = user_input.title()
            is_valid = True
        else:
            print("Error: Must include at least 2 names with letters only.\n"
                  "Blank or single-word entries are not accepted.\n")

    return driver_name
    
print(get_driver_name())
    
def speeding_offence():
    '''RECORDING AN OFFENCE AND COLLECTS DRIVERS RELEVANT INFO'''
    
