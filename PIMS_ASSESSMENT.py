#---CONSTANTS---
MAX_SPEED = 110
WANTED_LIST = ["NIKITA SMITH","BOB SMITH","ROB SMITH","COB SMITH","NOB SMITH"]

#---PROGRAM FUNCTIONS WITHIN COMPONENTS---

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

def validate_speed(): 
    '''CHECKS SPPED - makes sure recorded offending speed is greater than
    posted speed'''
    
    is_valid = False
    recorded_speed = ''
    
    while not is_valid: #Asks for offending speed
        user_input = input("Enter driver's speed: ").strip()
        
        #ensures speed is breaching limit. else, returns no offence
        if user_input.isdigit():
            temp_speed = int(user_input)
            if temp_speed > MAX_SPEED:
                recorded_speed = temp_speed
                is_valid = True
            else: 
                print('''Error: Driver's speed does not exceed posted 30-110km/h speed.
                No offence occurred.''')
        else:
            print("Error: Please enter a whole number.")        
    
    return recorded_speed

def calculate_fine(speed_over):
    """Calculates the fine based on speed over limit"""
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
    """Checks if driver name is on wanted list. Prints a warning if matched."""
    if driver_name.upper().strip() in WANTED_LIST:
        print(f"  WARNING: {driver_name.upper()} IS ON THE WANTED LIST!")   
    
    return None
    
#------MAIN PAGE FUNCTIONS----------

def record_offence(offences_list):
    """Collects info, validates, checks wanted list, and stores offence."""
    
    print("\n--- Record Speeding Offence ---")
    driver_name = get_driver_name()
    licence_num = get_driver_licence()

    # Warrant check
    check_warrant(driver_name)

    posted_limit = validate_speed()

    is_invalid_speed = True
    while is_invalid_speed:
        try:
            recorded_speed = int(input("Enter recorded speed (km/h): "))
            if recorded_speed > 0:
                is_invalid_speed = False
            else:
                print("Recorded speed must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # speed must be over limit for offence
    if recorded_speed <= posted_limit:
        print(f'''\nNo speeding offence has occurred. 
        (Recorded: {recorded_speed} km/h <= Limit: {posted_limit} km/h)''')
        return None

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
    """Displays offences that were recorded in table."""
    print("\n--- Recorded Patrol Offences ---")
    if not offences_list:
        print("No offences recorded during this patrol.")
        return None

    # alignment for merit
    header = f"{'Driver':<20} {'Licence':<10} {'Limit':<7} {'Speed':<7} {'Over':<6} {'Fine':<6}"
    print(header)
    print("-" * len(header))

    for rec in offences_list:
        print(f"{rec['name']:<20} {rec['licence']:<10} {rec['limit']:<7} {rec['speed']:<7} {rec['over']:<6} ${rec['fine']:<6}")
    print()
    
def search_offence_records(offences_list): 
    """searches offence by full name or license no.""" 
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
        print(f"{rec['name']:<20} {rec['licence']:<10} {rec['limit']:<7} {rec['speed']:<7} {rec['over']:<6} ${rec['fine']:<6}") 
    print() 
    
def display_patrol_summary(offences_list):
    '''shows complete list in right format of all offences made on that patrol'''
    print("\n--- Patrol Summary ---")
    if not offences_list:
        print("No offences recorded during this patrol.")
        return None
    