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
        if len(parts) >= 2 and all(part.isalpha() for part in parts):
            driver_name = user_input.title()
            is_valid = True
        else:
            print("Error: Must include at least 2 names with letters only.\n"
                  "Blank or single-word entries are not accepted.\n")

    return driver_name

def get_drivers_license():
    '''ASKS FOR LICENSE NO. - Ensures only contains 2 letters followed by 2
    numbers in capital'''
    
    is_valid = False
    license_no = ""
    
    while not is_valid: # Asks for license no. 
        user_input = input("Enter driver's license number: ").strip().upper()
         
         # Ensures exactly 6 characters: first 2 are letters, last 4 are digits
        if len(user_input) == 6 and user_input[:2].isalpha() and user_input[2:].isdigit():
            license_no = user_input
            is_valid = True
        
        else:
            print("Error: Must be 6 characters long (2 letters followed by 4 numbers).")

    return license_no  

print(get_drivers_license())

    
def speeding_offence():
    '''RECORDING AN OFFENCE AND COLLECTS DRIVERS RELEVANT INFO'''
