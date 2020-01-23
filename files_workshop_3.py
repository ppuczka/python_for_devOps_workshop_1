import json
import yaml
import csv
from pprint import pprint


with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json', 'r') as opened_file:
    json_example = json.load(opened_file)

pprint(json_example)

json_example['Statement']['Resource'] = 'S3'
pprint(json_example)

with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json', 'w') as opened_file:
    json_example = json.dump(json_example, opened_file)

with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/example.yml', 'r') as opened_file:
    yml_example = yaml.safe_load(opened_file)

pprint(yml_example)

# with open ('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/example.csv', newline='') as csv_file:
#     csv_example = csv.reader(csv_file, delimiter = ',')

# for _ in range(5):
#     print(next(csv_example))