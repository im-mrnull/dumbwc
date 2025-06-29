# dumbwc

A simple Python implementation of the Unix `wc` (word count) command-line tool.

## Description

`dumbwc` is a command-line utility that mimics the functionality of the Unix `wc` command. It can count lines, words, characters, and bytes in text files. This project was created as a coding challenge to implement a basic version of the classic Unix text processing tool.

## Features

- **Line counting** (`-l`, `--lines`): Count the number of lines in a file
- **Word counting** (`-w`, `--words`): Count the number of words in a file  
- **Character counting** (`-m`, `--characters`): Count the number of characters in a file
- **Byte counting** (`-c`, `--bytes`): Count the number of bytes in a file
- **Default mode**: When no flags are specified, displays lines, words, and characters
- **Standard input support**: Read from stdin when no filename is provided

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/im-mrnull/dumbwc.git
cd dumbwc
```

2. Install the package:
```bash
pip install .
```

Or for development:
```bash
pip install -e .
```

## Usage

### Basic Usage

```bash
# Count lines, words, and characters (default behavior)
dumbwc filename.txt

# Count only lines
dumbwc -l filename.txt
dumbwc --lines filename.txt

# Count only words
dumbwc -w filename.txt
dumbwc --words filename.txt

# Count only characters
dumbwc -m filename.txt
dumbwc --characters filename.txt

# Count only bytes
dumbwc -c filename.txt
dumbwc --bytes filename.txt
```

### Reading from Standard Input

```bash

# Count words from stdin (temp.txt contains the file name)
cat temp.txt | dumbwc -c
```

### Examples

```bash
# Example with test file
$ dumbwc test.txt
7146 58164 342762 test.txt

# Count only lines
$ dumbwc -l test.txt
7146 test.txt

# Count only words
$ dumbwc -w test.txt
58164 test.txt

# Count only characters
$ dumbwc -m test.txt
342762 test.txt

# Count only bytes
$ dumbwc -c test.txt
342762 test.txt
```

## Command Line Options

| Option | Long Form | Description |
|--------|-----------|-------------|
| `-l` | `--lines` | Display the number of lines |
| `-w` | `--words` | Display the number of words |
| `-m` | `--characters` | Display the number of characters |
| `-c` | `--bytes` | Display the number of bytes |
| `-h` | `--help` | Show help message and exit |

## Project Structure

```
dumbwc/
├── src/
│   └── dumbwccli/
│       └── __init__.py          # Main implementation
├── scripts/
│   └── dumbwc                   # Executable script
├── setup.py                     # Package configuration
├── test.txt                     # Test file
├── temp.txt                     # Temporary test file
└── README.md                    # This file
```

## Implementation Details

The tool implements the following functions:

- `calculate_lines()`: Counts newlines in the file
- `calculate_words()`: Splits text and counts individual words (alphanumeric)
- `calculate_characters()`: Counts total characters including whitespace
- `calculate_bytes()`: Gets file size in bytes using `os.path.getsize()`

## Differences from Unix `wc`

This is a simplified implementation and may have some differences from the standard Unix `wc` command:

- Word counting logic may differ slightly in edge cases
- Error handling and reporting may be different
- Performance characteristics may vary
- Some advanced options of Unix `wc` are not implemented

## Requirements

- Python 3.x
- No external dependencies required

## Development

### Running Tests

You can test the tool with the included test files:

```bash
# Test with the included test file
dumbwc test.txt

# Compare with system wc (if available)
wc test.txt
dumbwc test.txt
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Shourya Rai**
- Email: reachshourya3010@gmail.com
- GitHub: [@im-mrnull](https://github.com/im-mrnull)

## Acknowledgments

- Inspired by the Unix `wc` command
- Created as part of a coding challenge series
- Thanks to the Project Gutenberg for providing test text files
