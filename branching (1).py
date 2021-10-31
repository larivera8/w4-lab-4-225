# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))  # added perentheses removed peroid and apostrophe

if year <= 1900:                                        #adeed semicolon
    print("Woah,that's the past!")                     # changed the apostrophe to quotation mark
elif year > 1900 & year < 2020:                       #removed &
    print("That's totally the present!")                # took of space
'''
else:
    print(Far out, that;s the future!!")
'''
    
elif year > 2022 & year < 2030:                            #added year
    print("Far out, that's the future!!")             # took of space
