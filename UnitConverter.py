from ConverterHistory import *
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

def weight_converter(input_weight, output_weight):
    weight_unit


def simple_converter():
    history_file_path = "converter_history.txt"
    history = ConverterHistory(history_file_path)
    try:
        converter = input("""Choose converter: 
                        1. Celsius to Farenheit
                        2. Farenheit to Celsius
                        3. Kilogram converter
                        Type 1/2/3 or exit() to end program: """)    
        while converter != "exit()":
            if converter == "1":
                c_value = int(input("Type celsius value: "))
                print(celsius_to_farenheit(c_value))
                history.append_to_history(str(c_value))
            elif converter == "2":
                f_value = int(input("Type farenheit value: "))
                print(farenheit_to_celsius(f_value))
            elif converter == "3":
                unit = input("Type unit to convert to: ")
                unit_value = int(input("Type number of kilograms: ")) 
                result = kilogram_converter(unit, unit_value)
                print(result)
            elif converter == "exit()":
                print("Goodbye :)")
                pass
            else:
                print("Wrong choice \n")
                converter = input("""Choose converter: 
                        1. Celsius to Farenheit
                        2. Farenheit to Celsius
                        3. Kilogram converter
                        Type 1/2/3 or exit() to end program: """) 
    except ValueError:
        print("Could not user convert data to an integer.")

    finally:
        _ = input("Do You want to try again ? Y or N: ")
        if (_.lower() == "Y".lower()):
            simple_converter()
        else:
            "Goodbye!" 

simple_converter()
    