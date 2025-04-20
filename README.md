# BioLib

This is a library written for supporting biology computing and data manipulation.

## Installation

### From PyPI (recommended)

bash pip install biolib

### From source

bash git clone [https://github.com/yourusername/biolib.git](https://github.com/yourusername/biolib.git)
cd biolib pip install -e .

## Usage

### As a library

from biolib import BioLib

# Create an instance
bio = BioLib()

# Set a genome sequence
bio.set_genome("ACGTACGT")

# Use functions
pattern_count = bio.count_pattern("ACG") print(f"Pattern count: {pattern_count}")

### Command-line interface

BioLib comes with a command-line interface:

bash biolib-cli

### Available commands:
| Command                     | Alias | Description                                      |
|-----------------------------|-------|--------------------------------------------------|
| `set_genome`                | `sg`  | Set a genome sequence                            |
| `count_pattern`             | `cp`  | Get count of pattern occurrences in a text       |
| `count_approximate_pattern` | `cap` | Get count of approximate pattern occurrences     |
| `match_pattern`             | `mp`  | Get indexes of matches of pattern in a text      |
| `frequency_map`             | `fm`  | Get a map of every pattern occurrence in a text  |
| `frequent_words`            | `fw`  | Get a list of the most frequent words in a text  |
| `complement`                | `c`   | Get a literal complement of a DNA sequence       |
| `reverse_complement`        | `rc`  | Get a reverse complement of a DNA sequence       |
| `get_minimum_skew`          | `gms` | Get minimum skew of a DNA sequence               |
| `calculate_hamming_distance`| `chd` | Calculate hamming distance between two sequences |
| `quit`                      | `q`   | Quit the CLI                                     |

