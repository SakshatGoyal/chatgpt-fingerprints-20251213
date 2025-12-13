# Citation Insertion Script

## You (2025-03-30T21:34:14.181000+00:00)

🧭 GOAL
You are a structured file transformation assistant. Your task is to generate a Python script called adding_citations.py that performs the following:

Takes one reference file and multiple execution files as input.
Each file contains multiple structured modules labeled by a shared wrapper: CATEGORICAL MODULE [code] … END OF CATEGORICAL MODULE..
Each module may appear in both the reference and execution files but never more than once per file.
In the reference file, each module contains a citation as the final non-empty line before the closing END OF CATEGORICAL MODULE. tag.
In the execution files, the same modules are present but lack this citation.
Your task is to produce duplicate versions of each execution file, where the matching citation (if found) from the reference file is inserted after the Supporting Context: section and before the END OF CATEGORICAL MODULE. tag.
Preserve the original module structure, whitespace, and formatting exactly.
Save the transformed output files in the same directory as the originals, but with the word "condensed" in the filename replaced with "cited".
📄 RETURN FORMAT
Produce a complete Python 3 script named adding_citations.py with:

Clear function decomposition (e.g., extract_modules, match_and_merge_modules, write_output_files).
Logging to terminal of:
Any modules found in the reference file but missing in all execution files.
Any modules found in execution files with no matching citation in the reference file.
A final summary of:
Number of modules processed.
Number of successful citation insertions.
Number of unmatched modules in either direction.
Inline comments explaining key parts of logic.
⚠️ WARNINGS & GUARDRAILS

Do not modify any content except for inserting the citation.
Ensure that the citation is inserted after the Supporting Context block and before the END tag, with one blank line above END OF CATEGORICAL MODULE..
If a module appears in an execution file but has no matching module in the reference, retain it and log the absence of a citation.
If a module appears in the reference file but in none of the execution files, log that too.
Match modules by exact string match on the CATEGORICAL MODULE [code] line.
Be robust to minor edge cases: occasional extra blank lines, small whitespace inconsistencies.
📚 CONTEXT & ADDITIONAL ELEMENTS

All files are structured text (.txt), encoded in UTF-8.
Filepaths are absolute, and follow a nested RQ-structure by research question (e.g., /RQ-1/, /RQ-2/, etc.).
Categories include: Business Strategy, Corporate Strategy, Functional Strategy, Innovation Strategy, Leadership Strategy, Risk Management Strategy.
Example of file renaming:
Original: Innovation Strategy Insights - condensed - RQ-2.txt
New: Innovation Strategy Insights - cited - RQ-2.txt
The same module code (e.g., C2-I1) may appear in different execution files but should be processed independently.

---

Path to reference file:
/Users/sakshatgoyal/Desktop/Compilation/Massive Dump.txt

Path to execution files:
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Business Strategy Insights - condensed - RQ-1.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Corporate Strategy Insights - condensed - RQ-1.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Functional Strategy Insights - condensed - RQ-1.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Innovation Strategy Insights - condensed - RQ-1.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Leadership Strategy Insights - condensed - RQ-1.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Risk Management Strategy Insights - condensed - RQ-1.txt

/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Business Strategy Insights - condensed - RQ-2.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Corporate Strategy Insights - condensed - RQ-2.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Functional Strategy Insights - condensed - RQ-2.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Innovation Strategy Insights - condensed - RQ-2.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Leadership Strategy Insights - condensed - RQ-2.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Risk Management Strategy Insights - condensed - RQ-2.txt

/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Business Strategy Insights - condensed - RQ-3.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Corporate Strategy Insights - condensed - RQ-3.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Functional Strategy Insights - condensed - RQ-3.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Innovation Strategy Insights - condensed - RQ-3.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Leadership Strategy Insights - condensed - RQ-3.txt
/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Risk Management Strategy Insights - condensed - RQ-3.txt

## ChatGPT (2025-03-30T21:34:14.666264+00:00)

```python
#!/usr/bin/env python3
"""
adding_citations.py

This script processes a reference file and multiple execution files. It extracts modules
from each file (modules are delimited by "CATEGORICAL MODULE ..." and "END OF CATEGORICAL MODULE.")
In the reference file, each module’s final non-empty line before the END tag is a citation.
For each execution file, the script finds matching modules (by an exact match on the module header)
and inserts the corresponding citation immediately after the Supporting Context section and 
before the END tag (ensuring one blank line above the END tag).

It logs:
  - Modules that are in the reference file but missing in all execution files.
  - Modules in execution files with no matching citation in the reference.
  - A final summary with counts of modules processed, citation insertions, and unmatched modules.
  
Usage: Simply run the script. The output files will be saved in the same directory as the originals,
with "condensed" replaced by "cited" in the filename.
"""

import os
import sys

# ----------------------------
# Helper Functions
# ----------------------------

def extract_modules_from_content(content):
    """
    Extracts modules from the given file content.
    Returns a dictionary mapping the module header line (stripped) to the list of lines (module content).
    Assumes that each module starts with a line starting with "CATEGORICAL MODULE" and ends with
    a line that (when stripped) equals "END OF CATEGORICAL MODULE.".
    """
    modules = {}
    lines = content.splitlines()
    current_module = []
    module_header = None
    in_module = False

    for line in lines:
        # Check if this is the start of a module.
        if line.startswith("CATEGORICAL MODULE"):
            # If already in a module, we assume modules do not nest; start a new module.
            in_module = True
            module_header = line.strip()
            current_module = [line]
        elif line.strip() == "END OF CATEGORICAL MODULE." and in_module:
            # End of the current module.
            current_module.append(line)
            if module_header:
                modules[module_header] = current_module
            in_module = False
            module_header = None
            current_module = []
        else:
            if in_module:
                current_module.append(line)
    return modules

def extract_citation(module_lines):
    """
    Given a list of lines representing a module (from the reference file),
    returns the citation line which is defined as the final non-empty line before the
    "END OF CATEGORICAL MODULE." tag.
    """
    # Ensure the module ends with the END tag.
    if not module_lines or module_lines[-1].strip() != "END OF CATEGORICAL MODULE.":
        return None
    # Traverse backwards (excluding the END tag) to find the last non-empty line.
    for line in reversed(module_lines[:-1]):
        if line.strip():
            return line.rstrip("\n")
    return None

def insert_citation(module_lines, citation):
    """
    Inserts the given citation into the execution module.
    The citation is inserted after the Supporting Context block and before the END tag.
    A blank line is ensured immediately above the END tag.
    The original module structure and formatting are preserved.
    """
    # Locate the END tag.
    end_idx = None
    for idx, line in enumerate(module_lines):
        if line.strip() == "END OF CATEGORICAL MODULE.":
            end_idx = idx
            break
    if end_idx is None:
        # No END tag found; return original content.
        return module_lines

    # Try to locate the last occurrence of "Supporting Context:" if it exists.
    support_idx = None
    for idx, line in enumerate(module_lines):
        if "Supporting Context:" in line:
            support_idx = idx

    # Determine the insertion point.
    # We'll insert the citation just before the END tag.
    insertion_idx = end_idx

    # Remove any trailing blank lines immediately before the END tag to ensure exactly one blank line.
    while insertion_idx > 0 and module_lines[insertion_idx - 1].strip() == "":
        insertion_idx -= 1

    # Build new module lines: keep content up to insertion_idx, then add citation, a blank line, then the END tag.
    new_module_lines = module_lines[:insertion_idx]
    new_module_lines.append(citation)
    new_module_lines.append("")  # Ensure one blank line before the END tag.
    new_module_lines.extend(module_lines[end_idx:])  # Append the END tag and any lines after it.
    return new_module_lines

def write_output_file(original_path, new_lines):
    """
    Writes the transformed module content to a new file.
    The new filename is generated by replacing 'condensed' with 'cited' in the original filename.
    The new file is saved in the same directory as the original.
    """
    directory, filename = os.path.split(original_path)
    new_filename = filename.replace("condensed", "cited")
    new_filepath = os.path.join(directory, new_filename)
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
    print(f"Output written to: {new_filepath}")

def process_execution_file(file_path, ref_citations, ref_modules_used, stats):
    """
    Processes a single execution file:
      - Extracts modules from the file.
      - For each module, if a matching citation is found in ref_citations,
        inserts it into the module (after the Supporting Context section).
      - Logs if a module has no matching citation.
      - Writes out the new file with "cited" in the filename.
    Updates stats and ref_modules_used accordingly.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    modules = extract_modules_from_content(content)

    # We'll rebuild the file content by replacing the module blocks.
    new_file_lines = []
    current_idx = 0
    # Process file line-by-line and replace modules when encountered.
    lines = content.splitlines()
    # To know which lines belong to a module, we iterate through modules based on the known module headers.
    # We'll use a simple state machine.
    in_module = False
    module_buffer = []
    module_header = None

    for line in lines:
        if line.startswith("CATEGORICAL MODULE") and not in_module:
            in_module = True
            module_buffer = [line]
            module_header = line.strip()
        elif in_module:
            module_buffer.append(line)
            if line.strip() == "END OF CATEGORICAL MODULE.":
                # Finished a module; process it.
                stats['modules_processed'] += 1
                if module_header in ref_citations:
                    citation = ref_citations[module_header]
                    # Insert the citation into the module content.
                    new_module = insert_citation(module_buffer, citation)
                    stats['citations_inserted'] += 1
                    # Mark that this reference module was used.
                    ref_modules_used.add(module_header)
                else:
                    # Log that no matching citation was found for this module.
                    print(f"[WARNING] No matching citation found in reference for module: {module_header} in file {file_path}")
                    stats['unmatched_execution'] += 1
                    new_module = module_buffer
                # Append the processed module lines.
                new_file_lines.extend(new_module)
                # Reset state.
                in_module = False
                module_buffer = []
                module_header = None
        else:
            # Outside any module; simply add the line.
            new_file_lines.append(line)
    # Write the new file.
    write_output_file(file_path, new_file_lines)

def main():
    # Define the file paths.
    reference_file = "/Users/sakshatgoyal/Desktop/Compilation/Massive Dump.txt"
    execution_files = [
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Business Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Corporate Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Functional Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Innovation Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Leadership Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Risk Management Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Business Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Corporate Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Functional Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Innovation Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Leadership Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Risk Management Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Business Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Corporate Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Functional Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Innovation Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Leadership Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Risk Management Strategy Insights - condensed - RQ-3.txt",
    ]

    # Load and process the reference file.
    try:
        with open(reference_file, 'r', encoding='utf-8') as f:
            ref_content = f.read()
    except Exception as e:
        print(f"Error reading reference file: {e}")
        sys.exit(1)

    ref_modules = extract_modules_from_content(ref_content)
    ref_citations = {}
    for header, module_lines in ref_modules.items():
        citation = extract_citation(module_lines)
        if citation:
            ref_citations[header] = citation
        else:
            print(f"[WARNING] No citation found in reference module: {header}")

    # Counters for summary.
    stats = {
        'modules_processed': 0,
        'citations_inserted': 0,
        'unmatched_execution': 0  # modules in execution files with no matching citation
    }
    # Set to track reference modules that were used in at least one execution file.
    ref_modules_used = set()

    # Process each execution file.
    for exe_file in execution_files:
        if not os.path.exists(exe_file):
            print(f"[ERROR] Execution file not found: {exe_file}")
            continue
        print(f"Processing execution file: {exe_file}")
        process_execution_file(exe_file, ref_citations, ref_modules_used, stats)

    # Log modules that appear in the reference file but were not found in any execution file.
    for ref_header in ref_citations:
        if ref_header not in ref_modules_used:
            print(f"[WARNING] Reference module not found in any execution file: {ref_header}")

    # Final summary.
    total_ref = len(ref_citations)
    total_exe = stats['modules_processed']
    print("\n--- Processing Summary ---")
    print(f"Total modules processed from execution files: {total_exe}")
    print(f"Total successful citation insertions: {stats['citations_inserted']}")
    print(f"Total execution modules with no matching citation: {stats['unmatched_execution']}")
    print(f"Total reference modules with no matching execution module: {total_ref - len(ref_modules_used)}")

if __name__ == "__main__":
    main()
```

## You (2025-03-30T21:38:21.451000+00:00)

"--- Processing Summary ---
Total modules processed from execution files: 0
Total successful citation insertions: 0
Total execution modules with no matching citation: 0
Total reference modules with no matching execution module: 0
sakshatgoyal@MacBook-Pro Desktop % "

Could you help debug this issue? should I attach a sample of the reference file and one of the execution files for your reference?

## ChatGPT (2025-03-30T21:38:22.107332+00:00)

Yes, please do! That summary showing all zeroes suggests that the script didn't detect any modules in **either** the reference file or the execution files — likely due to formatting mismatches (e.g., spacing, line endings, or slight deviations in tag lines like `CATEGORICAL MODULE [code]` or `END OF CATEGORICAL MODULE.`).

🔧 To troubleshoot this effectively, please upload:

1. A sample of your **reference file** (`Massive Dump.txt`) that includes at least one complete module.
2. A sample of **one execution file** that includes at least one module expected to match.

Once I see how the modules are actually formatted, I can tweak the parsing logic to ensure it's picking up the content correctly. You can just upload short snippets if full files are too large — a few modules each will do!

## You (2025-03-30T21:39:01.939000+00:00)

Massive Dump.txt is the reference file, and Functional Strategy Insights... is the execution file.

## ChatGPT (2025-03-30T21:39:03.744449+00:00)

Thanks for uploading both files — this helps a lot!

Here's what I found that's **breaking the module detection in the current script**:

---

### 🔍 ISSUE: Header Parsing is Too Strict

Your modules begin with:
```
### CATEGORICAL MODULE 34 - C2-I1
```

But the script only looks for lines that start with:
```python
if line.startswith("CATEGORICAL MODULE"):
```

This misses headers that begin with `###`, tabs, or spaces.

---

### ✅ FIX: Use a More Flexible Pattern

Let’s adjust the detection logic to **match lines containing `CATEGORICAL MODULE` anywhere**, and then use that as the module header.

Here’s the fix for the `extract_modules_from_content` function:

```python
import re

def extract_modules_from_content(content):
    modules = {}
    lines = content.splitlines()
    current_module = []
    module_header = None
    in_module = False

    for line in lines:
        # Match header line flexibly, e.g., "### CATEGORICAL MODULE 34 - C2-I1"
        if re.search(r'CATEGORICAL MODULE\s+\S+', line):
            if in_module:
                # Previous module didn't close; discard or warn if needed
                pass
            in_module = True
            module_header = line.strip()
            current_module = [line]
        elif line.strip() == "END OF CATEGORICAL MODULE." and in_module:
            current_module.append(line)
            if module_header:
                modules[module_header] = current_module
            in_module = False
            module_header = None
            current_module = []
        else:
            if in_module:
                current_module.append(line)
    return modules
```

This version:
- Finds any line with `"CATEGORICAL MODULE"` in it
- Stores that line (stripped of whitespace) as the module header
- Keeps the module block intact
- Works even if `###` or spaces appear before the tag

---

### 📋 Next Steps

1. Would you like me to regenerate the updated full script (`adding_citations.py`) with this fix and any other refinements?
2. Once it's ready, you can re-run it and it should detect and cite everything as expected.

Let me know — happy to patch it up cleanly.

## You (2025-03-30T21:39:48.642000+00:00)

regenerate the updated full script

## ChatGPT (2025-03-30T21:39:49.020873+00:00)

Below is the updated full Python script. The key change is in the module extraction function: it now uses a regular expression to match any line that contains "CATEGORICAL MODULE" (regardless of any preceding "###" or spaces). This should detect your headers correctly.

```python
#!/usr/bin/env python3
"""
adding_citations.py

This script processes a reference file and multiple execution files.
It extracts modules (delimited by module header lines and an "END OF CATEGORICAL MODULE." line).
In the reference file, each module’s final non-empty line (before the END tag) is the citation.
For each execution file, if a module with the same header exists in the reference, the corresponding citation
is inserted after the Supporting Context section and before the END tag (with a blank line before the END tag).

The script logs:
  - Modules that are in the reference file but missing in all execution files.
  - Modules in execution files with no matching citation in the reference.
  - A final summary with counts of modules processed, citation insertions, and unmatched modules.
  
Usage: Run the script. Output files are saved in the same directory as the originals,
with "condensed" replaced by "cited" in the filename.
"""

import os
import sys
import re

# ----------------------------
# Helper Functions
# ----------------------------

def extract_modules_from_content(content):
    """
    Extracts modules from the given file content.
    A module starts at any line that contains "CATEGORICAL MODULE" (using a regex search)
    and ends with a line that exactly equals "END OF CATEGORICAL MODULE.".
    Returns a dictionary mapping the module header (stripped) to a list of lines (module content).
    """
    modules = {}
    lines = content.splitlines()
    current_module = []
    module_header = None
    in_module = False

    for line in lines:
        # Use regex to flexibly match any header line containing "CATEGORICAL MODULE"
        if re.search(r'CATEGORICAL MODULE\s+\S+', line):
            # Start a new module
            in_module = True
            module_header = line.strip()
            current_module = [line]
        elif line.strip() == "END OF CATEGORICAL MODULE." and in_module:
            current_module.append(line)
            if module_header:
                modules[module_header] = current_module
            in_module = False
            module_header = None
            current_module = []
        else:
            if in_module:
                current_module.append(line)
    return modules

def extract_citation(module_lines):
    """
    Given a list of lines representing a module (from the reference file),
    returns the citation line which is defined as the final non-empty line before the
    "END OF CATEGORICAL MODULE." tag.
    """
    if not module_lines or module_lines[-1].strip() != "END OF CATEGORICAL MODULE.":
        return None
    # Walk backwards (excluding the END tag) to find the last non-empty line.
    for line in reversed(module_lines[:-1]):
        if line.strip():
            return line.rstrip("\n")
    return None

def insert_citation(module_lines, citation):
    """
    Inserts the given citation into the execution module.
    The citation is inserted after the Supporting Context section and before the END tag.
    Ensures one blank line immediately before the END tag.
    """
    # Find the index of the END tag.
    end_idx = None
    for idx, line in enumerate(module_lines):
        if line.strip() == "END OF CATEGORICAL MODULE.":
            end_idx = idx
            break
    if end_idx is None:
        return module_lines

    # Determine the insertion index.
    insertion_idx = end_idx

    # Remove any trailing blank lines immediately before the END tag.
    while insertion_idx > 0 and module_lines[insertion_idx - 1].strip() == "":
        insertion_idx -= 1

    # Rebuild module lines: original lines up to insertion_idx, then the citation,
    # then a blank line, and finally the END tag (and any trailing lines).
    new_module_lines = module_lines[:insertion_idx]
    new_module_lines.append(citation)
    new_module_lines.append("")  # one blank line before END tag
    new_module_lines.extend(module_lines[end_idx:])
    return new_module_lines

def write_output_file(original_path, new_lines):
    """
    Writes the transformed file content to a new file.
    The new filename is created by replacing "condensed" with "cited" in the original filename.
    """
    directory, filename = os.path.split(original_path)
    new_filename = filename.replace("condensed", "cited")
    new_filepath = os.path.join(directory, new_filename)
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
    print(f"Output written to: {new_filepath}")

def process_execution_file(file_path, ref_citations, ref_modules_used, stats):
    """
    Processes a single execution file:
      - Extracts modules from the file.
      - For each module, if a matching citation is found in ref_citations,
        inserts it into the module.
      - Logs if a module has no matching citation.
      - Writes out the new file with "cited" in the filename.
    Updates stats and marks reference modules that were used.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract modules from execution file
    modules = extract_modules_from_content(content)
    new_file_lines = []
    lines = content.splitlines()

    in_module = False
    module_buffer = []
    module_header = None

    for line in lines:
        if re.search(r'CATEGORICAL MODULE\s+\S+', line) and not in_module:
            in_module = True
            module_buffer = [line]
            module_header = line.strip()
        elif in_module:
            module_buffer.append(line)
            if line.strip() == "END OF CATEGORICAL MODULE.":
                stats['modules_processed'] += 1
                if module_header in ref_citations:
                    citation = ref_citations[module_header]
                    new_module = insert_citation(module_buffer, citation)
                    stats['citations_inserted'] += 1
                    ref_modules_used.add(module_header)
                else:
                    print(f"[WARNING] No matching citation found for module: {module_header} in file {file_path}")
                    stats['unmatched_execution'] += 1
                    new_module = module_buffer
                new_file_lines.extend(new_module)
                in_module = False
                module_buffer = []
                module_header = None
        else:
            new_file_lines.append(line)
    write_output_file(file_path, new_file_lines)

def main():
    # Define file paths.
    reference_file = "/Users/sakshatgoyal/Desktop/Compilation/Massive Dump.txt"
    execution_files = [
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Business Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Corporate Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Functional Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Innovation Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Leadership Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Risk Management Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Business Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Corporate Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Functional Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Innovation Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Leadership Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Risk Management Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Business Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Corporate Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Functional Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Innovation Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Leadership Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Risk Management Strategy Insights - condensed - RQ-3.txt",
    ]

    # Process the reference file.
    try:
        with open(reference_file, 'r', encoding='utf-8') as f:
            ref_content = f.read()
    except Exception as e:
        print(f"Error reading reference file: {e}")
        sys.exit(1)

    ref_modules = extract_modules_from_content(ref_content)
    ref_citations = {}
    for header, module_lines in ref_modules.items():
        citation = extract_citation(module_lines)
        if citation:
            ref_citations[header] = citation
        else:
            print(f"[WARNING] No citation found in reference module: {header}")

    # Counters for summary.
    stats = {
        'modules_processed': 0,
        'citations_inserted': 0,
        'unmatched_execution': 0  # modules in execution files with no matching citation
    }
    # Track reference modules used.
    ref_modules_used = set()

    # Process each execution file.
    for exe_file in execution_files:
        if not os.path.exists(exe_file):
            print(f"[ERROR] Execution file not found: {exe_file}")
            continue
        print(f"Processing execution file: {exe_file}")
        process_execution_file(exe_file, ref_citations, ref_modules_used, stats)

    # Log any reference modules not used.
    for ref_header in ref_citations:
        if ref_header not in ref_modules_used:
            print(f"[WARNING] Reference module not found in any execution file: {ref_header}")

    # Final summary.
    total_ref = len(ref_citations)
    total_exe = stats['modules_processed']
    print("\n--- Processing Summary ---")
    print(f"Total modules processed from execution files: {total_exe}")
    print(f"Total successful citation insertions: {stats['citations_inserted']}")
    print(f"Total execution modules with no matching citation: {stats['unmatched_execution']}")
    print(f"Total reference modules with no matching execution module: {total_ref - len(ref_modules_used)}")

if __name__ == "__main__":
    main()
```

### Explanation of Key Changes:
- **Module Extraction:** The function now uses a regex search (`re.search(r'CATEGORICAL MODULE\s+\S+', line)`) to match any header line containing "CATEGORICAL MODULE" even if it is preceded by "###" or extra whitespace.
- **Citation Insertion:** The citation is inserted just before the "END OF CATEGORICAL MODULE." line with exactly one blank line before the END tag.
- **Logging:** Warnings are printed when a module in an execution file lacks a matching citation, and at the end a summary is provided.

Feel free to run the updated script and let me know if you encounter any further issues!

## You (2025-03-30T21:43:13.514000+00:00)

could you rewrite the code with just one tiny change?

the citation in the detination files should have one blank line before, and one blank line after it. So, instead of

[categorical module code]
...
...
[Supporting Context]
[Citation]
[blank line]
END OF CATEGORICAL MODULE.

it should be


[categorical module code]
...
...
[Supporting Context]
[blank line]
[Citation]
[blank line]
END OF CATEGORICAL MODULE.

## ChatGPT (2025-03-30T21:43:14.241865+00:00)

Below is the updated full script. The only change is in the citation insertion logic: now, the citation is inserted with one blank line before it and one blank line after it, so that the module structure becomes:

```
...
[Supporting Context]
[blank line]
[Citation]
[blank line]
END OF CATEGORICAL MODULE.
```

```python
#!/usr/bin/env python3
"""
adding_citations.py

This script processes a reference file and multiple execution files.
It extracts modules (delimited by module header lines and an "END OF CATEGORICAL MODULE." line).
In the reference file, each module’s final non-empty line (before the END tag) is the citation.
For each execution file, if a module with the same header exists in the reference, the corresponding citation
is inserted after the Supporting Context section and before the END tag.
The citation is now inserted with one blank line before and one blank line after it.

The script logs:
  - Modules that are in the reference file but missing in all execution files.
  - Modules in execution files with no matching citation in the reference.
  - A final summary with counts of modules processed, citation insertions, and unmatched modules.
  
Usage: Run the script. Output files are saved in the same directory as the originals,
with "condensed" replaced by "cited" in the filename.
"""

import os
import sys
import re

# ----------------------------
# Helper Functions
# ----------------------------

def extract_modules_from_content(content):
    """
    Extracts modules from the given file content.
    A module starts at any line that contains "CATEGORICAL MODULE" (using a regex search)
    and ends with a line that exactly equals "END OF CATEGORICAL MODULE.".
    Returns a dictionary mapping the module header (stripped) to a list of lines (module content).
    """
    modules = {}
    lines = content.splitlines()
    current_module = []
    module_header = None
    in_module = False

    for line in lines:
        # Use regex to flexibly match any header line containing "CATEGORICAL MODULE"
        if re.search(r'CATEGORICAL MODULE\s+\S+', line):
            # Start a new module
            in_module = True
            module_header = line.strip()
            current_module = [line]
        elif line.strip() == "END OF CATEGORICAL MODULE." and in_module:
            current_module.append(line)
            if module_header:
                modules[module_header] = current_module
            in_module = False
            module_header = None
            current_module = []
        else:
            if in_module:
                current_module.append(line)
    return modules

def extract_citation(module_lines):
    """
    Given a list of lines representing a module (from the reference file),
    returns the citation line which is defined as the final non-empty line before the
    "END OF CATEGORICAL MODULE." tag.
    """
    if not module_lines or module_lines[-1].strip() != "END OF CATEGORICAL MODULE.":
        return None
    # Walk backwards (excluding the END tag) to find the last non-empty line.
    for line in reversed(module_lines[:-1]):
        if line.strip():
            return line.rstrip("\n")
    return None

def insert_citation(module_lines, citation):
    """
    Inserts the given citation into the execution module.
    The citation is inserted with one blank line before and one blank line after it,
    immediately before the END tag.
    """
    # Find the index of the END tag.
    end_idx = None
    for idx, line in enumerate(module_lines):
        if line.strip() == "END OF CATEGORICAL MODULE.":
            end_idx = idx
            break
    if end_idx is None:
        return module_lines

    # Determine the insertion index.
    insertion_idx = end_idx

    # Remove any trailing blank lines immediately before the END tag.
    while insertion_idx > 0 and module_lines[insertion_idx - 1].strip() == "":
        insertion_idx -= 1

    # Rebuild module lines: original lines up to insertion_idx,
    # then a blank line, the citation, another blank line,
    # and finally the END tag (and any trailing lines).
    new_module_lines = module_lines[:insertion_idx]
    new_module_lines.append("")            # Blank line before citation
    new_module_lines.append(citation)        # Citation line
    new_module_lines.append("")            # Blank line after citation
    new_module_lines.extend(module_lines[end_idx:])
    return new_module_lines

def write_output_file(original_path, new_lines):
    """
    Writes the transformed file content to a new file.
    The new filename is created by replacing "condensed" with "cited" in the original filename.
    """
    directory, filename = os.path.split(original_path)
    new_filename = filename.replace("condensed", "cited")
    new_filepath = os.path.join(directory, new_filename)
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
    print(f"Output written to: {new_filepath}")

def process_execution_file(file_path, ref_citations, ref_modules_used, stats):
    """
    Processes a single execution file:
      - Extracts modules from the file.
      - For each module, if a matching citation is found in ref_citations,
        inserts it into the module.
      - Logs if a module has no matching citation.
      - Writes out the new file with "cited" in the filename.
    Updates stats and marks reference modules that were used.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract modules from execution file
    modules = extract_modules_from_content(content)
    new_file_lines = []
    lines = content.splitlines()

    in_module = False
    module_buffer = []
    module_header = None

    for line in lines:
        if re.search(r'CATEGORICAL MODULE\s+\S+', line) and not in_module:
            in_module = True
            module_buffer = [line]
            module_header = line.strip()
        elif in_module:
            module_buffer.append(line)
            if line.strip() == "END OF CATEGORICAL MODULE.":
                stats['modules_processed'] += 1
                if module_header in ref_citations:
                    citation = ref_citations[module_header]
                    new_module = insert_citation(module_buffer, citation)
                    stats['citations_inserted'] += 1
                    ref_modules_used.add(module_header)
                else:
                    print(f"[WARNING] No matching citation found for module: {module_header} in file {file_path}")
                    stats['unmatched_execution'] += 1
                    new_module = module_buffer
                new_file_lines.extend(new_module)
                in_module = False
                module_buffer = []
                module_header = None
        else:
            new_file_lines.append(line)
    write_output_file(file_path, new_file_lines)

def main():
    # Define file paths.
    reference_file = "/Users/sakshatgoyal/Desktop/Compilation/Massive Dump.txt"
    execution_files = [
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Business Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Corporate Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Functional Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Innovation Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Leadership Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-1/Risk Management Strategy Insights - condensed - RQ-1.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Business Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Corporate Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Functional Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Innovation Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Leadership Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-2/Risk Management Strategy Insights - condensed - RQ-2.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Business Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Corporate Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Functional Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Innovation Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Leadership Strategy Insights - condensed - RQ-3.txt",
        "/Users/sakshatgoyal/Desktop/Strategy Insights Data Pipeline/RQ-3/Risk Management Strategy Insights - condensed - RQ-3.txt",
    ]

    # Process the reference file.
    try:
        with open(reference_file, 'r', encoding='utf-8') as f:
            ref_content = f.read()
    except Exception as e:
        print(f"Error reading reference file: {e}")
        sys.exit(1)

    ref_modules = extract_modules_from_content(ref_content)
    ref_citations = {}
    for header, module_lines in ref_modules.items():
        citation = extract_citation(module_lines)
        if citation:
            ref_citations[header] = citation
        else:
            print(f"[WARNING] No citation found in reference module: {header}")

    # Counters for summary.
    stats = {
        'modules_processed': 0,
        'citations_inserted': 0,
        'unmatched_execution': 0  # modules in execution files with no matching citation
    }
    # Track reference modules used.
    ref_modules_used = set()

    # Process each execution file.
    for exe_file in execution_files:
        if not os.path.exists(exe_file):
            print(f"[ERROR] Execution file not found: {exe_file}")
            continue
        print(f"Processing execution file: {exe_file}")
        process_execution_file(exe_file, ref_citations, ref_modules_used, stats)

    # Log any reference modules not used.
    for ref_header in ref_citations:
        if ref_header not in ref_modules_used:
            print(f"[WARNING] Reference module not found in any execution file: {ref_header}")

    # Final summary.
    total_ref = len(ref_citations)
    total_exe = stats['modules_processed']
    print("\n--- Processing Summary ---")
    print(f"Total modules processed from execution files: {total_exe}")
    print(f"Total successful citation insertions: {stats['citations_inserted']}")
    print(f"Total execution modules with no matching citation: {stats['unmatched_execution']}")
    print(f"Total reference modules with no matching execution module: {total_ref - len(ref_modules_used)}")

if __name__ == "__main__":
    main()
```

### Explanation of the Change:
- In the `insert_citation` function, the code now appends:
  - A blank line before the citation,
  - The citation itself,
  - And a blank line after the citation,
  ensuring the desired output format.

Feel free to run this updated version and let me know if you need any further changes!

