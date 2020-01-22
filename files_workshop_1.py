file_path = '/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/text.txt'
file_pdf_path = '/Users/ppuczka/Downloads/Komunikat ws ustalenia kwoty zobowiązania na rok 2020.pdf'
open_file = open(file_path, 'r')
text = open_file.read()

print(len(text))
print(text)

print(open_file)


with open(file_path, 'r') as open_file:
    text = open_file.readlines()

for tx in text:
    print(text)

print(open_file.closed)

with open(file_pdf_path, 'rb') as open_file:
    btext = open_file.read()
print(btext)
