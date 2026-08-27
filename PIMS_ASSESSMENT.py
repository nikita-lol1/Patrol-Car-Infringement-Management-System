#---CONSTANTS---
WANTED_LIST = ["NIKITA SMITH","BOB SMITH","ROB SMITH","COB SMITH","NOB SMITH"]
PASSWORD = "45110"

#---PROGRAM FUNCTIONS WITHIN COMPONENTS---

def check_password():
    """ADRESS PRIVACY - Asks for password with a max of 3 attempts."""
    attempts = 3
    
    while attempts > 0:
        user_input = input("Enter password: ").strip()
        if user_input == PASSWORD:
            print("Access granted.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect password. You have {attempts} attempt(s) left.\n")
            else:
                print("Access denied. Too many incorrect attempts.")
                return False

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

    return driver_name.upper()

def get_drivers_license():
    '''ASKS FOR LICENSE NO. - Ensures only contains 2 letters followed by 4
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

def validate_speed():
    '''CHECK SPPED VIOLATION - Validates posted speed limit (30-110 km/h) 
    checks if recorded speed exceeds it.'''
    posted_limit = 0
    is_limit_valid = False
    
    # Get and validate the posted speed limit
    while not is_limit_valid:
        user_input = input("Enter posted speed limit (30-110 km/h): ").strip()
        
        if user_input.isdigit():
            temp_limit = int(user_input)
            if 30 <= temp_limit <= 110:
                posted_limit = temp_limit
                is_limit_valid = True
            else:
                print("Error: Posted speed limit must be between 30 and 110 km/h.")
        else:
            print("Error: Invalid input. Please enter a whole number.")

    recorded_speed = 0
    is_speed_valid = False
    
    # Get and validate the driver's recorded speed
    while not is_speed_valid:
        user_input = input("Enter recorded driver speed: ").strip()
        
        if user_input.isdigit():
            temp_speed = int(user_input)
            if temp_speed > posted_limit:
                recorded_speed = temp_speed
                is_speed_valid = True
            else:
                print(f'''No offence occurred. Recorded speed ({temp_speed} km/h) 
                does not exceed posted limit ({posted_limit} km/h).''')
                return None  #Takes the user back to the main menu
        else:
            print("Error: Invalid input. Please enter a whole number.")
            
    return posted_limit, recorded_speed


def calculate_fine(speed_over):
    """CALCULATE FINE - based on speed over limit"""
    if 1 <= speed_over <= 10:
        return 30
    elif 11 <= speed_over <= 20:
        return 80
    elif 21 <= speed_over <= 30:
        return 170
    elif 31 <= speed_over <= 40:
        return 400
    else:
        return 630
    
def check_warrant(driver_name):
    """VERIFIES NAME - Checks if driver name is on wanted list. 
    Prints a warning if matched."""
    if driver_name.upper().strip() in WANTED_LIST:
        print(f"  WARNING: {driver_name.upper()} IS ON THE WANTED LIST!")   
    
    return None
    
#------MAIN PAGE FUNCTIONS----------

def record_offence(offences_list):
    """DATA STORAGE - Collects info, validates, checks wanted list, 
    and stores offence."""
    
    print("\n--- Record Speeding Offence ---")
    driver_name = get_driver_name()
    licence_num = get_drivers_license()

    # Warrant check
    check_warrant(driver_name)

    speed_data = validate_speed()
    
    # Returns to main menu if validate_speed returns None (no offence occurred)
    if speed_data is None:
        return None

    posted_limit, recorded_speed = speed_data

    speed_over = recorded_speed - posted_limit
    fine_amount = calculate_fine(speed_over)

    # store offence record as dictionary
    offence_record = {
        "name": driver_name,
        "licence": licence_num,
        "limit": posted_limit,
        "speed": recorded_speed,
        "over": speed_over,
        "fine": fine_amount
    }
    
    offences_list.append(offence_record)

    print("\n--- Offence Recorded Successfully ---")
    print(f"Driver Name : {driver_name}")
    print(f"Licence No  : {licence_num}")
    print(f"Speed Over  : {speed_over} km/h")
    print(f"Fine Amount : ${fine_amount}\n")    

def view_all_offences(offences_list):
    """SHOW DATA - Displays offences that were recorded in table."""
    print("\n--- Recorded Patrol Offences ---")
    if not offences_list:
        print("No offences recorded during this patrol.")
        return None

    # alignment for merit
    header = f"{'Driver':<20} {'Licence':<10} {'Limit':<7} {'Speed':<7} {'Over':<6} {'Fine':<6}"
    print(header)
    print("-" * len(header))

    for rec in offences_list:
        print(f'''{rec['name']:<20} {rec['licence']:<10} {rec['limit']:<7} 
        {rec['speed']:<7} {rec['over']:<6} ${rec['fine']:<6}''')
    print()
    
def search_offence_records(offences_list): 
    """SEARCH OFFENCES - by full name or license no.""" 
    print("\n--- Search Offence Records ---") 
    if not offences_list: 
        print("No offences recorded yet") 
        return None 
        
    search = input("Enter driver full name or licence number to search: ").strip().upper() 
    found_records = [rec for rec in offences_list if search in rec['name'].upper() or search == rec['licence']] 
    
    if not found_records: 
        print(f"No records found matching search: '{search}'") 
        return None 
        
    print(f"\nFound {len(found_records)} matching record(s):") 
    header = f"{'Driver':<20} {'Licence':<10} {'Limit':<7} {'Speed':<7} {'Over':<6} {'Fine':<6}" 
    print(header) 
    print("-" * len(header)) 
    
    for rec in found_records: 
        print(f'''{rec['name']:<20} {rec['licence']:<10} {rec['limit']:<7} 
        {rec['speed']:<7} {rec['over']:<6} ${rec['fine']:<6}''') 
    print() 
    
def display_patrol_summary(offences_list):
    '''COMPLETE LIST - in right format of all offences made on that patrol'''
    print("\n--- Patrol Summary ---")
    if not offences_list:
        print("No offences recorded during this patrol.")
        return None
   
    total_offences = len(offences_list)
    total_fines = sum(rec['fine'] for rec in offences_list)
    avg_speed_over = sum(rec['over'] for rec in offences_list) / total_offences
    
    # Identify highest offence
    highest_offence = max(offences_list, key=lambda x: x['over'])

    print(f"Total offences            : {total_offences}")
    print(f"Total fines issued        : ${total_fines}")
    print(f"Average speed over limit  : {avg_speed_over:.1f} km/h")
    print(f'''Highest offence           : {highest_offence['name']} 
                                  ({highest_offence['over']} km/h over limit)''')
    print()    
    
def main_menu():
    '''MAIN MENU - users will be sent to to start program'''
    # Run password check first
    if not check_password():
        return  # Exits program if password check fails

    offences_list = []
    is_running = True

    while is_running:
        print("-----------------------------")
        print("    POLICE PATROL SYSTEM     ")
        print("-----------------------------")
        print("1. Record a speeding offence")
        print("2. View all recorded offences")
        print("3. Search offence records")
        print("4. Display patrol summary")
        print("5. Exit program")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            record_offence(offences_list)
        elif choice == '2':
            view_all_offences(offences_list)
        elif choice == '3':
            search_offence_records(offences_list)
        elif choice == '4':
            display_patrol_summary(offences_list)
        elif choice == '5':
            print("Thank you for visting Police Patrol System!")
            is_running = False
        else:
            print("ERROR: Please choose a number between 1 and 5.\n")


if __name__ == "__main__":
    main_menu()

