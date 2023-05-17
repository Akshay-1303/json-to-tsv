import json
import csv

# Open the JSON file for reading
with open('company_data.json', 'r') as json_file:
    data = json.load(json_file)['data']

# Open the TSV file for writing
with open('output.tsv', 'w', newline='') as tsv_file:
    writer = csv.writer(tsv_file, delimiter='\t')

    # Write the header
    header = data[0].keys()
    writer.writerow(header)

    # Write the data
    for row in data:
        writer.writerow(row.values())
