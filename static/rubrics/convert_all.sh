#!/bin/bash

# Ensure the txt directory exists
INPUT_DIR="txt"
OUTPUT_DIR="html"

# Create the output directory if it does not exist
mkdir -p "$OUTPUT_DIR"

# Path to the Python script
PYTHON_SCRIPT="convert_txt_to_html.py"

# Check if the Python script exists
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "Error: Python script '$PYTHON_SCRIPT' not found!"
    exit 1
fi

# Process all .txt files in the txt directory
for txt_file in "$INPUT_DIR"/*.txt; do
    # Check if there are no txt files
    if [[ ! -e "$txt_file" ]]; then
        echo "No .txt files found in $INPUT_DIR."
        exit 1
    fi

    # Extract the base filename without extension
    base_name=$(basename "$txt_file" .txt)

    # Define output HTML file path
    html_file="$OUTPUT_DIR/$base_name.html"

    # Run the Python script and save the output
    echo "Processing $txt_file -> $html_file"
    python3 "$PYTHON_SCRIPT" "$txt_file" > "$html_file"
done

echo "Conversion completed. HTML files are in the '$OUTPUT_DIR' folder."

