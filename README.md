# FileCrawler

## Overview

**File Name:** `FileCrawler.py`  
**Description:** This script searches for specified keywords in various file types (text and PDF) within a given directory. It logs the occurrences of the keywords along with their positions in the files.  
**Author:** Ajay Singh  
**Version:** 1.0  
**Date:** 27-10-2024

## Features

- Search for keywords in multiple file formats, including:
  - Text files (`.txt`, `.csv`, `.log`, etc.)
  - PDF files (`.pdf`)
- Logs the occurrences of keywords along with their line or page and word positions.
- Supports colored terminal output for error messages.
- Ability to read search parameters from an input file.
- Option to update the input file with new search parameters.
- User-friendly command line interface for repeated searches.

## Requirements

- Python 3.x
- `PyPDF2` library for PDF handling
- `colorama` library for colored terminal output

To install the required libraries, you can use pip:
```bash
pip install PyPDF2 colorama
```

## How to Use

1. **Input File Structure:**
   - Create a text file named `input.txt` in the same directory as the script.
   - The first line should contain the directory path to search.
   - The subsequent lines should contain the keywords to search for, one per line.

   **Example of `input.txt`:**
   ```
   /path/to/directory
   keyword1
   keyword2
   ```

2. **Run the Script:**
   - Execute the script in the terminal:
   ```bash
   python FileCrawler.py
   ```

3. **Interactive Inputs:**
   - You will be prompted to enter a directory to search and keywords. You can leave these blank to use the existing inputs from `input.txt`.

4. **Output:**
   - The results will be logged in an `output.txt` file, detailing the occurrences found.

## Example Usage

1. Place `FileCrawler.py` and `input.txt` in the same directory.
2. Run the script and follow the prompts.
3. Check `output.txt` for search results.

## Notes

- Ensure that the directory you specify in `input.txt` exists and is accessible.
- The script handles multiple file formats as specified in the `file_patterns` list.
- For PDF files, ensure that the `PyPDF2` library is installed; otherwise, PDF search functionality will be disabled.

```