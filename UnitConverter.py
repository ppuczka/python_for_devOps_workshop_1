# this is simple unit converter 

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
    
    
unit = input("Podaj jednostkę: ")
unit_value = int(input("Podaj ilość kilogramów: ")) 
   
result = kilogram_converter(unit, unit_value)
print(result)
    