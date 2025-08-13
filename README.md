# CountyFilter

A Python-based data filtering tool for extracting and processing Kenyan administrative data (counties, constituencies, wards, and sub-counties) for specific regions.

## Overview

CountyFilter is designed to filter large datasets of Kenyan administrative boundaries and extract data for specific counties of interest. The project focuses on four counties: **Meru**, **Embu**, **Kirinyaga**, and **Tharaka-Nithi**.

## Features

- **CSV Data Filtering**: Extract specific county data from large CSV files containing all Kenyan administrative units
- **GeoJSON Processing**: Filter large GeoJSON files to create smaller, region-specific map files
- **Sub-county Extraction**: Process and standardize sub-county data with proper formatting
- **Multi-format Output**: Generate filtered data in both CSV and JSON formats

## Project Structure

```
CountyFilter/
├── extract_sub_counties.py    # Extracts and formats sub-county data
├── filter_map.py             # Filters GeoJSON files for specific counties
├── wards_filter.py           # Filters ward-level administrative data
├── sub_counties.csv          # Filtered sub-county data
├── filtered_counties.csv     # Filtered county/ward data
├── filtered_counties.json    # Filtered GeoJSON data
└── README.md                # This file
```

## Scripts

### 1. extract_sub_counties.py
Processes sub-county data from `kenya_subcounty.csv` and creates a filtered output with:
- Uppercase formatting for consistency
- Only specified counties (Meru, Embu, Kirinyaga, Tharaka-Nithi)
- Clean CSV output format

### 2. filter_map.py
Filters large GeoJSON files to create smaller, region-specific map files:
- Loads and processes GeoJSON FeatureCollections
- Case-insensitive county name matching
- Preserves coordinate reference systems
- Configurable county property keys

### 3. wards_filter.py
Extracts ward-level data from comprehensive administrative datasets:
- Filters by county names
- Maintains original data structure
- Fast processing for large CSV files

## Usage

### Prerequisites
- Python 3.x
- Input data files:
  - `kenya_subcounty.csv`
  - `csv-Kenya-Counties-Constituencies-Wards.csv`
  - `kenya_wards.json`

### Running the Scripts

1. **Extract Sub-counties**:
   ```bash
   python extract_sub_counties.py
   ```

2. **Filter GeoJSON Maps**:
   ```bash
   python filter_map.py
   ```

3. **Filter Ward Data**:
   ```bash
   python wards_filter.py
   ```

## Configuration

The target counties are defined in each script:
```python
counties_to_keep = {'Meru', 'Embu', 'Kirinyaga', 'Tharaka-Nithi'}
```

For GeoJSON filtering, ensure the correct property key is set:
```python
county_property_key = 'county'  # Adjust based on your data structure
```

## Output Files

- `sub_counties.csv`: Filtered sub-county data with standardized formatting
- `filtered_counties.csv`: Ward-level data for target counties
- `filtered_counties.json`: GeoJSON file containing only target county boundaries

## Data Format

The project works with Kenyan administrative data structured as:
- **Counties**: Top-level administrative divisions
- **Constituencies**: Electoral divisions within counties
- **Wards**: Smallest administrative units
- **Sub-counties**: Administrative subdivisions of counties

## Error Handling

All scripts include comprehensive error handling for:
- Missing input files
- Malformed CSV/JSON data
- Encoding issues
- Invalid data structures

## License

This project is for educational and administrative data processing purposes.