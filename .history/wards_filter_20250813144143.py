# Assuming your data is in a file named 'counties.csv'
file_path = 'csv-Kenya-Counties-Constituencies-Wards.csv'
output_file_path = 'filtered_counties.csv'

counties_to_keep = {'MERU', 'EMBU', 'KIRINYAGA', 'THARAKA-NITHI'}

with open(file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    # Read the header from the input file
    header = infile.readline()
    # Write the header to the output file
    outfile.write(header)

    for line in infile:
        # Split the line by comma
        columns = line.strip().split(',')
        # The county name is in the second column (index 1)
        # Convert to uppercase for case-insensitive comparison
        county_name = columns[1].upper()

        # Check if the county name is in our set of counties to keep
        if county_name in counties_to_keep:
            # If it is, write the entire line to the output file
            outfile.write(line)

print(
    f"Data for {', '.join(counties_to_keep)} 
    has been saved to
    '{output_file_path}'.")
