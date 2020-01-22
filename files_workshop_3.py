import json
from pprint import pprint

with open('/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json', 'r') as opened_file:
    json_example = json.load(opened_file)

pprint(json_example)

json_example['Statement']['Resource'] = 'S3'
pprint(json_example)

with open("/Users/ppuczka/Desktop/Projects_v2/Python_Workshops/jsonexample.json", 'w') as opened_file:
    json_example = json.dump(json_example, opened_file)