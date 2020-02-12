from ConverterHistory import *
from CurrencyConverter import *
# this is simple unit converter 
# add file writting 
# make it object orienter 

def kilogram_converter(unit, x):
    units = {
    "miligram" : lambda x: x / 0.0001,
    "gram" : lambda x: x / 0.001,
    "kilogram" : lambda x: x,
    "ton" : lambda x: x / 1000,
    "ounce" : lambda x: x / 0.028,
    "pound" : lambda x: x / 0.453,
    "quater" : lambda x: x / 12.70,
    "long ton" : lambda x: x / 1016
    }
    return units.get(unit, "Not found")(x)

def celsius_to_farenheit(c_value):
    return (c_value * 1.8) + 32

def farenheit_to_celsius(f_value):
    return (f_value - 32) * 1.8 
    
def temperature_converter(entered_unit, result_unit, history):
    try:
    
        if (entered_unit == "celsius"):
            entered_value = int(input(f"Type {entered_unit} value: "))
            result_value = celsius_to_farenheit(entered_value)
        else:
            entered_value = int(input(f"Type {entered_unit} value: "))
            result_value = farenheit_to_celsius(entered_value) 
            
        print(f"Result: {result_value} {result_unit}")
        history.append_to_history(str(entered_value), str(result_value), entered_unit, result_unit)
    
    except ValueError:
        print("Could not user convert data to an integer.")

def convert_currency(from_currency_code, to_currency_code, value, converter, history):
    currency_rates = converter.get_latest_currency_rate(from_currency_code.upper())
    rate = currency_rates.get(to_currency_code.upper(), "Not found") 
    converted_currency = round(value * rate, 2)
    print(f"{value} {from_currency_code.upper()} equals {converted_currency} {to_currency_code.upper()}")
    history.append_to_history(str(value), str(converted_currency), from_currency_code.upper(), to_currency_code.upper() )

def simple_converter():
    history_file_path = "converter_history.txt"
    history = ConverterHistory(history_file_path)
    currency_con = CurrencyConverter()

    converter = input("""Choose converter: 
                    1. Celsius to Farenheit
                    2. Farenheit to Celsius
                    3. Kilogram converter
                    4. Currency converter
                    Type 1/2/3/4 or exit to end program: """)    
    
    while converter != "exit":
        if converter == "1":
            temperature_converter("celsius", "farenheit", history)          
        
        elif converter == "2":
            temperature_converter("farenheit", "celsius", history)
        
        elif converter == "3":
            unit = input("Type unit to convert to: ")
            unit_value = int(input("Type number of kilograms: ")) 
            result = kilogram_converter(unit, unit_value)
            print(result)
        
        elif converter == "4":
            currency_from = input("Type currency to convert from USD/EUR/PLN: ")
            currency_to = input("Type currency to convert to USD/EUR/PLN: ")
            currency_value = int(input("Type cash value: ")) 
            convert_currency(currency_from, currency_to, currency_value, currency_con, history)

        elif converter == "exit":
            print("Goodbye :)")
            break
        else:
            print("Wrong choice \n")
            converter = input("""Choose converter: 
                    1. Celsius to Farenheit
                    2. Farenheit to Celsius
                    3. Kilogram converter
                    4. Currency converter
                    Type 1/2/3/4 or exit to end program: """)    
simple_converter()
    