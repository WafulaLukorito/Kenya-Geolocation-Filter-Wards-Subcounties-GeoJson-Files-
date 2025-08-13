import csv

input_file_path = 'kenya_subcounty.csv'
output_file_path = 'sub_counties.csv'
counties_to_keep = {'Meru', 'Embu', 'Kirinyaga', 'Tharaka-Nithi'}

try:
    with open(input_file_path, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read and write the header row
        header = next(reader)
        writer.writerow(header)

        # Iterate over each row in the input file
        for row in reader:
            # Assuming 'COUNTY NAME' is the second column (index 1)
            if row[0] in counties_to_keep:
                # Modify first both columns to be uppercase
                row[0] = row[0].upper()
                row[1] = row[1].upper()
                writer.writerow(row)

    print(
        f"A new file named '{output_file_path}' has been created with the specified counties.")

except FileNotFoundError:
    print(f"Error: The input file '{input_file_path}' was not found.")
except IndexError:
    print("Error: The CSV file might be malformed or the 'COUNTY NAME' column is not where expected.")
