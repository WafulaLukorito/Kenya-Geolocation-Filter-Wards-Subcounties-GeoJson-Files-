import json


def extract_locations_from_geojson(file_path):
    """
    Reads a GeoJSON file, iterates through its features, and extracts
    county, subcounty, and ward information into a hierarchical JSON object.

    Args:
        file_path (str): The path to the GeoJSON file.

    Returns:
        A dictionary with a nested structure (county -> subcounty -> wards),
        or None if an error occurs.
    """
    try:
        # Open and load the GeoJSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        structured_locations = {}

        # Iterate through each feature in the GeoJSON data
        for feature in geojson_data['features']:
            # Access the properties of the feature
            properties = feature.get('properties', {})

            # Extract the desired information
            county = properties.get('county')
            subcounty = properties.get('subcounty')
            ward = properties.get('ward')

            # Check if all required properties exist
            if all([county, subcounty, ward]):
                # Add county if it doesn't exist
                if county not in structured_locations:
                    structured_locations[county] = {}

                # Add subcounty if it doesn't exist within the county
                if subcounty not in structured_locations[county]:
                    structured_locations[county][subcounty] = []

                # Add the ward to the subcounty's list
                structured_locations[county][subcounty].append(ward)

        return structured_locations

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# The user's uploaded file is accessible in this environment via the
# `offlinemap.geojson` filename.
structured_data = extract_locations_from_geojson('offlinemap.geojson')

if structured_data:
    # Write the new structured data to a JSON file
    output_file = 'locations.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2)
    print(f"Successfully wrote the hierarchical JSON data to '{output_file}'.")
else:
    print("Failed to extract the hierarchical JSON data.")
