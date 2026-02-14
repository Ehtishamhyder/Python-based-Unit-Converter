# unit converter

def show_list():
    print("1. Centimetre to Metre")
    print("2. Metre to Centimetre")
    print("3. Kilometre to Metre")
    print("4. Metre to Kilometre")
    print("5. Kilometre to Miles")
    print("6. Miles to Kilometre")
    print("7. Gram to Kilogram")
    print("8. Kilogram to Gram")
    print("9. Celsius to Fahrenheit")
    print("10. Fahrenheit to Celsius")
    print("11. Litres to Millilitres")
    print("12. Millilitres to Litres")
    print("13. Seconds to Minutes")
    print("14. Minutes to Seconds")
    print("15. Minutes to Hours")
    print("16. Hours to Minutes")
    print("17. Exit")

def main():
    show_list()
    choice = int(input("Enter your choice (1-17): "))
    

    if choice == 1:
        x = float(input("Enter value in centimetres:"))
        print("Result:", x/100, "metres")

    elif choice == 2:
        x = float(input("Enter value in metres:"))
        print("Result:", x*100, "centimetres")

    elif choice == 3:
        x = float(input("Enter value in kilometres:"))
        print("Result:", x*1000, "metres")

    elif choice == 4:
        x = float(input("Enter value in metres:"))
        print("Result:", x/1000, "kilometres")

    elif choice == 5:
        x = float(input("Enter value in kilometres:"))
        print("Result:", x*0.621371, "miles")

    elif choice == 6:
        x = float(input("Enter value in miles:"))
        print("Result:", x/0.621371, "kilometres")

    elif choice == 7:
        x = float(input("Enter value in grams:"))
        print("Result:", x/1000, "kilograms")

    elif choice == 8:
        x = float(input("Enter value in kilograms:"))
        print("Result:", x*1000, "grams")

    elif choice == 9:
        x = float(input("Enter value in Celsius:"))
        print("Result:", (x*9/5)+32, "Fahrenheit")

    elif choice == 10:
        x = float(input("Enter value in Fahrenheit:"))
        print("Result:", (x-32)*5/9, "Celsius")

    elif choice == 11:                                    
        x = float(input("Enter value in litres:"))
        print("Result:", x*1000, "millilitres")

    elif choice == 12:
        x = float(input("Enter value in millilitres:"))
        print("Result:", x/1000, "litres")

    elif choice == 13:
        x = float(input("Enter value in seconds:"))
        print("Result:", x/60, "minutes")

    elif choice == 14:
        x = float(input("Enter value in minutes:"))
        print("Result:", x*60, "seconds")

    elif choice == 15:
        x = float(input("Enter value in minutes:"))
        print("Result:", x/60, "hours") 

    elif choice == 16:
        x = float(input("Enter value in hours:"))
        print("Result:", x*60, "minutes")
                   
    elif choice == 17:
        print("You are exiting the unit converter. Goodbye!")
    
main()    
        