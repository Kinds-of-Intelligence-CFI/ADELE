#!/usr/bin/env python3
import re
import sys

import html


def parse_text(input_text):
    """
    Parse the free form text into a title, introductory text and level blocks.
    Assumes:
      - The first nonempty line is the title.
      - The introduction is given in the lines following the title up until
        a line that starts with 'Level '.
      - Each level block starts with a line matching 'Level <number>:'.
      - Each level block has a description header that ends with an "Examples:" marker,
        then one or more bullet lines starting with '*'.
    """
    lines = input_text.strip().splitlines()
    title = None
    intro_lines = []
    level_blocks = []
    current_block = []
    in_intro = True

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # When we hit a line starting with "Level" we leave the intro section.
        if in_intro and (re.match(r'^Level \d+{:\.}', stripped) or re.match(r'^Level \d+\.', stripped)):
            in_intro = False

        if in_intro:
            # First non-empty line is the title; the rest is intro.
            if title is None:
                title = stripped
            else:
                intro_lines.append(stripped)
        else:
            # Build level blocks. Each new "Level" line signals a new block.
            if (re.match(r'^Level \d+:', stripped) or re.match(r'^Level \d+\.', stripped)) and current_block:
                level_blocks.append("\n".join(current_block))
                current_block = [stripped]
            else:
                current_block.append(stripped)
    if current_block:
        level_blocks.append("\n".join(current_block))

    # Process each level block.
    levels = []
    for block in level_blocks:
        # Split the block into header and examples parts by the marker "Examples:"
        parts = block.split("Examples:")
        header_text = parts[0].strip()
        examples_text = parts[1].strip() if len(parts) > 1 else ""

        # Extract the level number and the rest of the header.
        m = re.match(r'Level (\d+)[:.]\s*(.*)', header_text)
        if not m:
            continue
        level_num = m.group(1)
        rest = m.group(2).strip()
        # Assume that the first sentence (up to a period) is the level name.
        # For example: "None. No attention or scan is required." becomes
        # level_name: "None." and level_desc: "No attention or scan is required."
        if '.' in rest:
            parts_header = rest.split(".", 1)
            level_name = parts_header[0].strip() + "."
            level_desc = parts_header[1].strip()
        else:
            level_name = rest
            level_desc = ""

        # Now extract example bullet points.
        example_lines = []
        for ex_line in examples_text.splitlines():
            ex_line = ex_line.strip()
            if ex_line.startswith("*"):
                # Remove the bullet marker.
                example_lines.append(ex_line.lstrip("*").strip())
            else:
                # If a line continues a bullet point, append it.
                if example_lines:
                    example_lines[-1] += " " + ex_line
        levels.append({
            "level_num": level_num,
            "level_name": level_name,
            "level_desc": level_desc,
            "examples": example_lines,
        })
    return title, "\n".join(intro_lines), levels


def generate_html(title, intro, levels, color="primordial"):
    """
    Generate HTML output with two tcolorbox sections:
      - The first for the title and introduction.
      - The second for the Levels list with bullet examples.
    """
    html_lines = []
    # First tcolorbox: Title and Intro
    tcolorbox_string = f'<div class="tcolorbox" style="border: 1px solid var(--{color});">'
    tcolorbox_title_string = f'    <div class="tcolorbox-title" style="background-color: var(--{color});">'
    html_lines.append(tcolorbox_string)
    html_lines.append(tcolorbox_title_string + f'{html.escape(title)}</div>')
    html_lines.append('    <div class="tcolorbox-body">')
    html_lines.append('      <span style="font-family: sans-serif;">')
    html_lines.append(f'        {html.escape(intro)}')
    html_lines.append('      </span>')
    html_lines.append('    </div>')
    html_lines.append('</div>\n')
    html_lines.append('<!-- Second tcolorbox: Levels -->')
    html_lines.append(tcolorbox_string)
    html_lines.append(tcolorbox_title_string + '    Levels</div>')
    html_lines.append('    <div class="tcolorbox-body">')
    html_lines.append('        <ol class="levels" start="0">')

    # Process each level into an <li> element.
    for level in levels:
        # For level 5, we display it as "Level 5+".
        data_label = f"Level {level['level_num']}" if level['level_num'] != "5" else "Level 5+"
        html_lines.append(f'            <li data-label="{html.escape(data_label)}">')
        html_lines.append(f'          <span style="font-family: sans-serif;">')
        # Build the header line: bold level name, then description, then bold "Examples:".
        header_line = f'<strong>{html.escape(level["level_name"])}</strong> {html.escape(level["level_desc"])} <strong>Examples:</strong>'
        html_lines.append(f'            {header_line}')
        html_lines.append('          </span>')
        # Build the unordered list for examples.
        html_lines.append('                    <ul>')
        for ex in level["examples"]:
            html_lines.append(
                f'                        <li><span style="font-family: sans-serif;">{html.escape(ex)}</span></li>')
        html_lines.append('                    </ul>')
        html_lines.append('                </li>')
    html_lines.append('            </ol>')
    html_lines.append('        </div>')
    html_lines.append('    </div>')
    return "\n".join(html_lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    # handle colors:
    # This assumes the rubric names is the AS, CEc, CEe or similar
    rubric = input_file.split('.')[0].split('/')[1]
    #             --primordial: #d1495b;
    #             --knowledge: #00798c;
    #             --others: #30638e;
    #             --nd: #edae49;
    if 'KN' in rubric:
        color = 'knowledge'
    elif rubric in ['AT', 'VO']:
        color = 'others'
    elif rubric == 'UG':
        color = 'nd'
    else:
        color = 'primordial'

    title, intro, levels = parse_text(input_text)
    html_output = generate_html(title, intro, levels, color=color)
    print(html_output)


if __name__ == "__main__":
    main()
