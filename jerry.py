age = int(input("Enter your age: "))

# nested if statements to determine eligibility for a rollercoaster ride
if age >= 10:
    print("You are old enough to ride the rollercoaster")
    height = int(input("Enter your height in cm: "))
    if height >= 120:
        print("And you meet the height requirement.")
        w = int(input("Enter ur w"))
        if w > 50:
            print("enjoy ur ride")
        else:
            print("increse ur age")
    else:
        print("But you do not meet the height requirement.")
else:
    print("You are not eligible to ride the rollercoaster because you are too young.")
