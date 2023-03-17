print("Available options: cm to ft, ft to cm, temperature, kg to lbs, lbs to kg")
print("oz to l, l to oz, gallon to l, l to gallon, kph to mph, mph to kph, mile to km.")
choice = input("What unit do you wanna calculate?: ")

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

if choice == "temperature": ## fixed 2022-11-01
    f_c_choice = input("Do you want to convert F to C or C to F?: ")

    if f_c_choice == "F to C":
        fahreinheit_input = input("Enter fahrenheit temperature: ")
    
        fahreinheit_input = float(fahreinheit_input)
        result_f_to_c = (fahreinheit_input - 32) * 5 / 9
        print(f"{result_f_to_c} celcius degrees")

    if f_c_choice == "C to F":
        celcius_input = input("Enter celcuis temperature: ")

        celcius_input = float(celcius_input)    
        result_c_to_f = (celcius_input * 9 / 5) + 32
        print(f"{result_c_to_f} degrees")

if choice == "kg to lbs":
    kg_to_lbs = float(input("Enter weight in kg to convert into lbs: "))
    pounds = kg_to_lbs * 2.2046
    print(round(kg_to_lbs),' Kilograms =', round(pounds),' lbs')

if choice == "lbs to kg":
    lbs_to_kg = float(input("Enter weight in lbs to convert into kg: "))
    kg = lbs_to_kg * 0.453592
    print(round(lbs_to_kg),' Pounds(lbs) are equal to', round(kg),'Kilogram (kg)')

if choice == "oz to l":
    oz_to_liter_input = float(input("Enter oz to convert into liters: "))
    oz_to_liter = oz_to_liter_input * 0.0295735296
    print(round(oz_to_liter_input),'oz are equal to', round(oz_to_liter),'L(liters)') 

if choice == "l to oz":
    liter_to_oz_input = float(input("Enter liters to convert into oz: "))
    liter_to_oz = liter_to_oz_input / 0.0295735296
    print(round(liter_to_oz_input),'L are equal to', round(liter_to_oz), 'oz')

if choice ==  "gallon to l":
    gallon_to_liter_input = float(input("Enter gallons to convert into liters: "))
    gallon_to_liter = gallon_to_liter_input * 3.785411784
    print(round(gallon_to_liter_input),'gallons are equal to', round(gallon_to_liter), 'L')

if choice == "l to gallon":
    liter_to_gallon_input = float(input("Enter liters to convert into gallons: "))
    gallon_to_liter = gallon_to_liter_input / 0.2641720524
    print(round(liter_to_gallon_input),'L are equal to', round(gallon_to_liter), 'gallons')

if choice == "kph to mph":
    kph_to_mph_input = float(input("Enter km/h to convert into mi/h: "))
    kph_to_mph = 0.6124 * kph_to_mph_input
    print(round(kph_to_mph_input, 1),'km/h is equal to', round(kph_to_mph, 1),'mi/h')

if choice == "mph to kph":
    mph_to_kph_input = float(input("Enter mi/h to convert into kp/h: "))
    mph_to_kph = 1.609344 * mph_to_kph_input
    print(round(mph_to_kph_input, 1),'mi/h is equal to', round(mph_to_kph, 1),'km/h')

if choice == "m to km":
    m_to_km_input = float(input("Enter miles to convert into km: "))
    m_to_km = 1.60935 * m_to_km_input 
    print(round(m_to_km_input, 1), 'miles is equal to', round(m_to_km, 1),'km')