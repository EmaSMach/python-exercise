def ask_for_details():
    details = {}
    user_id = raw_input("User id : ")
    while True:
        first_name = raw_input("First Name: ")
        if first_name.isspace() or len(first_name) != 0:
            details["first_name"] = first_name
            break
        else:
            print "Name should not be empty, try again\n"
    while True:
        last_name = raw_input("Last Name: ")
        if first_name.isspace() or len(last_name) != 0:
            details["last_name"] = last_name
            break
        else:
            print "Name should not be empty, try again\n"
    while True:
        email = raw_input("Email: ")
        if email.isspace() or len(email) != 0:
            details["email"] = email
            break
        else:
            print "Name should not be empty, try again\n"
    while True:
        ACTIVE_OPTIONS = ("yes", "no", "YES", "NO", 1, 0)
        active = raw_input("Active: ")
        if active in ACTIVE_OPTIONS:
            details["active"] = True
            break
        else:
            print "Active shoul be 'yes', 'YES', 'no', 1, 0, try again\n"  # TODO
    while True:
        address = raw_input("Address: ")
        if address.isspace() or len(address) != 0:
            details["address"] = address
            break
        else:
            print "Address should not be empty, try again\n"

    city = raw_input("City: ")
    state = raw_input("State: ")
    country = raw_input("Country: ")
    zip_code = raw_input("Zip Code: ")
    while True:
        phone_number = raw_input("Phone Number: ")
        if phone_number.isdigit():
            details["phone_number"] = phone_number
            break
        else:
            print "Phone Number should not be empty, try again\n"

    time_zone = raw_input("Time Zone: ")

    while True:
        GENDER_OPTIONS = ("F", "M", "f", "m")
        gender = raw_input("Gender (valid options: 'm', 'M', 'f', 'F'): ")
        if gender in GENDER_OPTIONS:
            details['gender'] = gender
            break
        else:
            print "Gender should be 'f', 'F', 'm', 'M', try again:\n"

    details['city'] = city
    details['state'] = state
    details['country'] = country
    details['zip_code'] = zip_code
    details['time_zone'] = time_zone
    return details

if __name__ == "__main__":
    detalles = ask_for_details()
    print(detalles)
    

