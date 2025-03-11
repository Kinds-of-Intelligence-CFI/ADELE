#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
import os

# Set up the Jinja2 environment and specify the templates folder
env = Environment(loader=FileSystemLoader('templates'))

# Load the main template
template = env.get_template('index.html')

# Render the template (you can pass variables if needed)
output_html = template.render()

# Define output folder and filename
output_file = os.path.join(".", 'index.html')

# Save the rendered HTML to a file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output_html)

print(f"Rendered HTML saved to {output_file}")
