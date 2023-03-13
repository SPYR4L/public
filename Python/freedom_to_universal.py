print("Do you want to convert cm to ft or ft to cm?")
choice = input("")

if choice == "ft to cm":

    print("Input your height: ")
    h_ft = int(input("Feet: "))
    h_inch = int(input("Inches: "))

    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)

    print("Your height is: %d cm." % h_cm)

if choice == "cm to ft":
    
    cm=int(input("Input your height: "))
    feet=0.0328*cm

    print("Your height is:", round(feet,2))