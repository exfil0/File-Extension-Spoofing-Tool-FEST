# File Extension Spoofing Tool (FEST V1)

## Description
This tool is designed for file extension spoofing. It allows users to create a copy of a file with a spoofed extension. This can be useful in various testing scenarios, including security testing and penetration testing exercises. The tool uses a special Unicode character to reverse the order of characters in the spoofed extension.

**IMPORTANT:** This tool is intended for educational purposes and legal ethical testing only. Misuse of this tool for deceptive or malicious purposes is strictly prohibited.

## Requirements
- Python 3.x
- Basic knowledge of command line operations

## Installation
No specific installation is required other than having Python installed on your system. Simply download the script and run it using Python.

## Usage
To use the tool, run the script from the command line, providing the path to the file and the extension you want to spoof.

### Syntax
```bash
python fest.py [path_to_file] [extension_to_spoof]
```

### Example
```bash
python fest.py /path/to/file.txt jpg
```

This command will create a spoofed version of 'file.txt' with a reversed 'jpg' extension appended, maintaining the original '.txt' extension.

### CAUTION
- Always ensure you have authorization before using this tool in a pentest environment.
- Do not use this tool on any systems where you do not have explicit permission to do so.
- The creators of this tool are not responsible for any misuse or damage caused by this tool.
