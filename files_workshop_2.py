import pathlib

text = '''export STAGE=PROD 
export TBALE_ID=token-storage-1234'''

with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/.envrc', 'w') as opened_file:
    opened_file.write(text)

path = pathlib.Path(
    "/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json"
)

with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json', 'r') as open_file:
    example = open_file.readlines()

print(open_file)