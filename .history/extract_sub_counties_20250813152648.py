import csv

input_file = 'kenya_subcounty.csv'
output_file = 'subcounties_list.csv'
counties_to_keep = {'Mombasa', 'Kwale'}

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header
    header = next(reader)
    # Write the header to the new file, ensuring the order is correct
    writer.writerow(['county', 'subCounty'])

    # Iterate over each row and filter based on the county name
    for row in reader:
        if len(row) > 0 and row[0] in counties_to_keep:
            # Write the row to the new CSV file
            writer.writerow(row)

print(
    f"A new CSV file named '{output_file}' has been created with data for Mombasa and Kwale counties.")
