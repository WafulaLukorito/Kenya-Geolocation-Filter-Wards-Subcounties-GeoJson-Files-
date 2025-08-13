import json


def extract_locations_from_geojson(file_path):
    """
    Reads a GeoJSON file, iterates through its features, and extracts
    county, subcounty, and ward information into a new JSON object.

    Args:
        file_path (str): The path to the GeoJSON file.

    Returns:
        A JSON formatted string containing a list of dictionaries,
        or None if an error occurs.
    """
    try:
        # Open and load the GeoJSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        locations = []

        # Iterate through each feature in the GeoJSON data
        for feature in geojson_data['features']:
            # Access the properties of the feature
            properties = feature.get('properties', {})

            # Extract the desired information
            county = properties.get('county')
            subcounty = properties.get('subcounty')
            ward = properties.get('ward')

            # Check if all required properties exist and add to the list
            if all([county, subcounty, ward]):
                locations.append({
                    'county': county,
                    'subcounty': subcounty,
                    'ward': ward
                })

        # Return the list of locations as a formatted JSON string
        return json.dumps(locations, indent=2)

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
json_output = extract_locations_from_geojson('offlinemap.geojson')

if json_output:
    # save to file
    with open('locations.json', 'w') as f:
        f.write(json_output)
else:
    print("No valid locations found or an error occurred.")
