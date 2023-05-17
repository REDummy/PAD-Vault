def searchCountry(state="America"):
    with open("exchrate.txt", "r") as inFile:
        for line in inFile:
            temp = line.strip() # Remove newline character
            if temp.startswith(state + ","): # Check if line starts with state name
                parts = temp.split(',')
                print("Currency : ", parts[1])
                print("Exchange Rate : ", float(parts[2]))
                break # Stop searching after finding first match
                
def ascCountry() :
    rate=list()
    # Open the file for reading
    with open('exchrate.txt', 'r') as file:
        # Read the lines and split them by comma
        for line in file.readlines() :
            lines = line.strip().split(',')
            rate.append(lines)
            

    # Sort the lines based on the exchange rate (third column)
    
    rate.sort(key=lambda x:float(x[2]))

    # Print the countries in ascending order of exchange rate
    for line in rate:
        print(line[0])

def convert() :
        # Open the file for reading
    with open('exchrate.txt', 'r') as file:
        # Read the lines and split them by comma
        lines = [line.strip().split(',') for line in file.readlines()]

    # Create a dictionary to map the country name to the exchange rate
    exchange_rates = {line[0]: (float(line[2]), line[1]) for line in lines}

    # Get the input amount and the two countries
    from_country = (input("Enter the name of the country you want to convert from: ")).title()
    to_country = (input("Enter the name of the country you want to convert to: ")).title()
    amount = float(input("Enter the amount of money: "))

    from_rate, from_currency = exchange_rates[from_country]
    to_rate, to_currency = exchange_rates[to_country]

    # Convert the amount from one currency to another 
    converted_amount = amount / from_rate * to_rate

    # Print the result
    print(f"{amount:.2f} {from_currency} ({from_country}) is equal to {converted_amount:.2f} {to_currency} ({to_country})")


       
#temp = input("Insert the name of Country: ")
#searchCountry(temp)
#ascCountry()
convert()