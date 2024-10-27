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

## Code Breakdown

### Imports

- **os, fnmatch**: For directory traversal and file pattern matching.
- **PyPDF2**: For reading PDF files (if available).
- **colorama**: For colored terminal output (if available).

### Error Handling

```python
def log_error(message):
    """Log error messages in red."""
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")
```
Logs errors in red color for better visibility.

### Searching Functions

- **`get_word_positions(words, search_string)`**: Returns positions of the search string in a list of words.
- **`search_text_file(filename, search_string)`**: Searches for a string in a text file, returning its line and word positions.
- **`search_pdf_file(filename, search_string)`**: Searches for a string in a PDF file, returning its page and word positions.

### Directory and File Search

```python
def search_files(directory, search_strings, output_file):
    """Search for strings in all readable files in the specified directory."""
```
Traverses the directory, searches for specified keywords in each file, and logs the results.

### Logging Functions

- **`log_and_print_directory(out_file, directory)`**: Logs the directory being searched.
- **`log_and_print_occurrences(out_file, filename, occurrences, context_label, search_string)`**: Logs and prints occurrences of found keywords in a structured format.
- **`output_no_results(out_file, directory)`**: Logs a message when no results are found.

### Input Handling

- **`read_input_file(input_file)`**: Reads the input file for directory and keywords.
- **`update_input_file(input_file, directory, keywords)`**: Updates the input file with the latest directory and keywords.

### Main Function

```python
def main():
```
The entry point of the script, which orchestrates reading inputs, executing searches, and prompting for repeated searches.

## Example Usage

1. Place `FileCrawler.py` and `input.txt` in the same directory.
2. Run the script and follow the prompts.
3. Check `output.txt` for search results.

## Notes

- Ensure that the directory you specify in `input.txt` exists and is accessible.
- The script handles multiple file formats as specified in the `file_patterns` list.
- For PDF files, ensure that the `PyPDF2` library is installed; otherwise, PDF search functionality will be disabled.

```
