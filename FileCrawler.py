#!/usr/bin/env python
# File Name: FileCrawler.py
# Description: This script searches for specified keywords in various file types
#              (text and PDF) within a given directory. It logs the occurrences
#              of the keywords along with their positions in the files.
# Author: Ajay Singh
# Version: 1.0
# Date: 27-10-2024

import os
import fnmatch

# Attempt to import necessary libraries for PDF handling
try:
    import PyPDF2
    PDF_SUPPORTED = True
except ImportError:
    PDF_SUPPORTED = False

# Attempt to import colorama for colored terminal output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    pass

# ========================== Constants ==========================
OUTPUT_HEADER = "Search Results"
OUTPUT_SEPARATOR = "=" * 50 + "\n"
FILE_PATTERNS = [
    '*.txt', '*.csv', '*.log', '*.bat', '*.py', '*.java', '*.cpp', '*.c',
    '*.js', '*.html', '*.xml', '*.json', '*.md', '*.doc', '*.docx', '*.xls',
    '*.xlsx', '*.ppt', '*.pptx', '*.rtf', '*.sql', '*.yaml', '*.yml',
    '*.tsv', '*.ini', '*.config', '*.svg', '*.sh', '*.pl', '*.rb', '*.pdf'
]

# ========================== Error Handling ==========================
def log_error(message):
    """Log error messages in red."""
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")

def write_and_print(out_file, message):
    """Write the message to the output file and print to the console."""
    out_file.write(message + "\n")
    print(message)

# ========================== File Search ==========================
def get_word_positions(words, search_string):
    """Return positions of search_string in a list of words."""
    return [index for index, word in enumerate(words) if word.lower() == search_string.lower()]

def search_text_file(filename, search_string):
    """Search for a string in a text file and return its line and word positions."""
    occurrences = []
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line_num, line in enumerate(file, start=1):
                words = line.split()
                positions = get_word_positions(words, search_string)
                if positions:
                    occurrences.append((line_num, positions))
    except (FileNotFoundError, IOError) as e:
        log_error(f"Could not read text file '{filename}': {e}")
    return occurrences

def search_pdf_file(filename, search_string):
    """Search for a string in a PDF file and return its page and word positions."""
    occurrences = []
    try:
        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    words = text.split()
                    positions = get_word_positions(words, search_string)
                    if positions:
                        occurrences.append((page_num + 1, positions))
    except Exception as e:
        log_error(f"Could not read PDF file '{filename}': {e}")
    return occurrences

def search_files(directory, search_strings, output_file):
    """Search for strings in all readable files in the specified directory."""
    directories_searched = set()
    files_searched = []
    matched_directories = set()

    with open(output_file, 'a') as out_file:
        for dirpath, _, filenames in os.walk(directory):
            directories_searched.add(dirpath)
            directory_match_found = False

            for pattern in FILE_PATTERNS:
                for filename in fnmatch.filter(filenames, pattern):
                    file_path = os.path.join(dirpath, filename)
                    files_searched.append(file_path)

                    for search_string in search_strings:
                        occurrences = search_pdf_file(file_path, search_string) if filename.lower().endswith('.pdf') and PDF_SUPPORTED else search_text_file(file_path, search_string)

                        if occurrences:
                            if not directory_match_found:
                                matched_directories.add(dirpath)
                                directory_match_found = True
                            log_and_print_occurrences(out_file, file_path, occurrences, search_string)

        write_summary(out_file, directories_searched, files_searched, search_strings, matched_directories)

def log_and_print_occurrences(out_file, file_path, occurrences, search_string):
    """Log and print occurrences of the found string in a structured format, with full file path."""
    header = f"Matches found for '{search_string}' in file: {file_path}"
    write_and_print(out_file, header)
    write_and_print(out_file, f"{'LINE/PAGE':<10} | {'WORD POSITIONS'}")
    write_and_print(out_file, "-" * 30)

    for index, positions in occurrences:
        out_line = f"{index:<10} | {positions}"
        write_and_print(out_file, out_line)
    write_and_print(out_file, "\n")

def write_summary(out_file, directories_searched, files_searched, search_strings, matched_directories):
    """Write a summary of directories and files searched, including matched directories."""
    summary = "\n\n" + OUTPUT_SEPARATOR + "SUMMARY OF SEARCH\n" + OUTPUT_SEPARATOR
    summary += f"Total Directories Searched: {len(directories_searched)}\n"
    summary += f"Total Files Searched: {len(files_searched)}\n"
    summary += f"Keywords Searched: {', '.join(search_strings)}\n"
    summary += f"Matched Directories: {len(matched_directories)}\n"
    summary += "Directories with Matches:\n" + "\n".join(matched_directories) + "\n"
    summary += "Directories Searched:\n" + "\n".join(directories_searched) + "\n"
    summary += "Files Searched:\n" + "\n".join(files_searched) + "\n"
    write_and_print(out_file, summary)

# ========================== Input Handling ==========================
def read_input_file(input_file):
    """Read directory and search keywords from an input file."""
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            directory = lines[0].strip()
            keywords = [line.strip() for line in lines[1:] if line.strip()]
            return directory, keywords
    except FileNotFoundError:
        log_error(f"Input file not found: '{input_file}'")
        return None, []
    except Exception as e:
        log_error(f"Could not read input file: {e}")
        return None, []

def update_input_file(input_file, directory, keywords):
    """Update the input file with the latest directory and keywords."""
    with open(input_file, 'w') as file:
        file.write(directory + '\n')
        file.write('\n'.join(keywords) + '\n')

# ========================== Main Function ==========================
def main():
    input_file = 'input.txt'
    output_file = 'output.txt'  # Output file to log results

    # Clear the output file at the start of each run
    with open(output_file, 'w') as f:
        f.write(OUTPUT_HEADER + "\n" + OUTPUT_SEPARATOR)

    while True:
        # Read inputs from the input file
        directory, existing_keywords = read_input_file(input_file)

        # Prompt user for input
        directory_input = input("Please enter the directory to search (leave blank to use existing): ").strip()
        search_keywords_input = input("Please enter keywords to search (separated by '--', leave blank to use existing): ").strip()

        # Use existing inputs if none provided
        if directory_input:
            directory = directory_input

        search_keywords = (
            [keyword.strip() for keyword in search_keywords_input.split('--') if keyword.strip()]
            if search_keywords_input else existing_keywords
        )

        # Keep only the first occurrence of each keyword while preserving order
        unique_keywords = list(dict.fromkeys(search_keywords))

        # Validate directory
        if not os.path.isdir(directory):
            log_error(f"Invalid directory: '{directory}'")
            continue

        # Update the input file only if new inputs were provided
        if directory_input or search_keywords_input:
            update_input_file(input_file, directory, unique_keywords)

        # Perform searches for each unique keyword
        for search_string in unique_keywords:
            print(f"\nSearching for '{search_string}' in directory '{directory}'...")
            search_files(directory, [search_string], output_file)  # Pass the current search string as a list

        # Ask user if they want to perform another search
        if input("Do you want to perform another search? (y/n): ").strip().lower() not in {'y', 'yes', ''}:
            break

# Entry point of the script
if __name__ == "__main__":
    main()
