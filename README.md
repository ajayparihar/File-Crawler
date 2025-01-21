# FileCrawler

A powerful Python utility for searching keywords across multiple file types and directories.

## Overview

**File Name:** `FileCrawler.py`  
**Description:** Searches for keywords in various file types (text and PDF) within a directory structure, providing detailed occurrence logs.  
**Author:** Ajay Singh  
**Version:** 1.0  
**Date:** 27-10-2024

## Key Features

- **Multi-format Search**: Supports various file types including:
  - Documents: `.txt`, `.doc`, `.docx`, `.pdf`, `.rtf`
  - Code Files: `.py`, `.java`, `.cpp`, `.js`, `.html`, `.xml`
  - Data Files: `.csv`, `.json`, `.yaml`, `.yml`, `.tsv`
  - Configuration: `.ini`, `.config`
  - Logs: `.log`
  
- **Search Capabilities**:
  - Case-insensitive keyword matching
  - Multiple keyword search support
  - Recursive directory scanning
  - Line/page number tracking
  - Word position recording

- **Output Features**:
  - Detailed search results
  - Optional search summary
  - Colored error messages
  - Both console and file output

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/FileCrawler.git
   cd FileCrawler
   ```

2. **Install Dependencies**:
   ```bash
   pip install PyPDF2 colorama
   ```

## Configuration

### Input File (`input.txt`)
```
/path/to/search/directory
keyword1--keyword2--keyword3
```

### Display Settings
- Summary display can be configured by changing `DISPLAY_SUMMARY` in the script:
  - `0`: No summary
  - `1`: Show complete summary

## Usage

1. **Basic Usage**:
   ```bash
   python FileCrawler.py
   ```

2. **Interactive Prompts**:
   - Directory prompt: Enter search directory or press Enter to use existing
   - Keywords prompt: Enter keywords separated by '--' or press Enter to use existing
   - Continue prompt: 'y' to perform another search, any other key to exit

3. **Output Location**:
   - Results are saved in `output.txt`
   - Real-time results appear in console

## Example

```bash
$ python FileCrawler.py
Please enter the directory to search (leave blank to use existing): /home/documents
Please enter keywords to search (separated by '--', leave blank to use existing): error--warning
Searching for 'error' in directory '/home/documents'...
[Results appear here]
Searching for 'warning' in directory '/home/documents'...
[Results appear here]
Do you want to perform another search? (y/n):
```

## Troubleshooting

### Common Issues

1. **PDF Search Not Working**
   - Ensure PyPDF2 is installed: `pip install PyPDF2`
   - Check PDF file permissions
   - Verify PDF is not encrypted

2. **No Color Output**
   - Install colorama: `pip install colorama`
   - Check terminal color support

3. **File Access Errors**
   - Verify directory permissions
   - Check file path validity
   - Ensure files aren't locked by other processes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
