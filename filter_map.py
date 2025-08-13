import json


def filter_geojson_by_county(input_path, output_path, counties_to_keep, county_property_key):
    """
    Filters a GeoJSON file to include only features from specified counties.

    Args:
        input_path (str): Path to the large input GeoJSON file.
        output_path (str): Path where the smaller, filtered GeoJSON will be saved.
        counties_to_keep (list): A list of county names (strings) to keep.
        county_property_key (str): The key in the 'properties' object that holds the county name.
    """
    try:
        # Load the entire GeoJSON file into memory.
        # This is necessary because we need to construct a new valid GeoJSON object.
        print(f"Loading {input_path}...")
        with open(input_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)
        print("File loaded successfully.")

        # The structure of a GeoJSON file is a dictionary. The features are in a list
        # under the "features" key.
        if 'features' not in geojson_data or not isinstance(geojson_data['features'], list):
            print("Error: Input file is not a valid GeoJSON FeatureCollection.")
            return

        # Create a list to hold the features we want to keep.
        filtered_features = []
        print(f"Filtering for counties: {', '.join(counties_to_keep)}...")

        # Iterate over each feature in the original file.
        for feature in geojson_data['features']:
            # Each feature has a 'properties' dictionary. We need to check if the
            # county name in the properties matches one of the counties we want to keep.
            # We use .get() to avoid errors if a feature is missing the property key.
            county_name = feature.get(
                'properties', {}).get(county_property_key)

            if county_name and county_name.strip().lower() in [c.lower() for c in counties_to_keep]:
                filtered_features.append(feature)

        print(f"Found {len(filtered_features)} matching features.")

        # If we found features, create a new GeoJSON structure for the output.
        if filtered_features:
            output_geojson = {
                "type": "FeatureCollection",
                # Preserve the Coordinate Reference System
                "crs": geojson_data.get("crs"),
                "features": filtered_features
            }

            # Write the new, smaller GeoJSON data to the output file.
            print(f"Saving filtered data to {output_path}...")
            with open(output_path, 'w', encoding='utf-8') as f:
                # Use indent=2 for readability, or None for the smallest file size.
                json.dump(output_geojson, f, indent=2)
            print("Done! Your new file has been created.")
        else:
            print(
                "No features found for the specified counties. No output file was created.")

    except FileNotFoundError:
        print(f"Error: The file was not found at {input_path}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file. It might be corrupted or not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    # --- CONFIGURATION ---

    # 1. Set the path to your big GeoJSON file.
    input_geojson_path = 'kenya_wards.json'  # Change this to your file's name

    # 2. Set the desired name for your new, smaller file.
    output_geojson_path = 'filtered_counties.json'

    # 3. List the exact names of the counties you want to keep.
    #    The script is case-insensitive, so 'Meru' and 'meru' are treated the same.
    counties_to_keep = [
        # Note: Sometimes names have hyphens! Check your data.
        "THARAKA-NITHI",
        "EMBU",
        "KIRINYAGA",
        "MERU"
    ]

    # 4. **VERY IMPORTANT**: Specify the property key for the county name.
    #    You MUST inspect your GeoJSON file to find the correct key.
    #    Common examples are 'COUNTY_NAM', 'county', 'CountyName', 'COUNTY'.
    county_property_key = 'county'  # <-- UPDATED!

    # --- END OF CONFIGURATION ---

    filter_geojson_by_county(
        input_geojson_path, output_geojson_path, counties_to_keep, county_property_key)
