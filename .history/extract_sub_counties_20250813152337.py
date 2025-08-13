import csv


def extract_counties(input_file, output_file):
    """
    Extracts unique county names from a CSV file and saves them to a new file.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output text file.
    """
    counties = set()  # Using a set to store unique county names

    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader, None)

        for row in reader:
            if len(row) > 0:
                counties.add(row[0])

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for county in sorted(list(counties)):
            output_file.write(f"{county}\n")


# Example usage:
input_csv = 'kenya_subcounty.csv'
output_txt = 'sub_counties_list.txt'
extract_counties(input_csv, output_txt)

print(f"Unique sub-county names have been saved to '{output_txt}'.")
