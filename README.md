# Text Generator

This project generates paragraphs of text using the NLTK Brown corpus. It includes grammar, spelling, and punctuation correction using the `language_tool_python` library.

## Requirements

- Python 3.12 or later
- NLTK
- language-tool-python

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure NLTK data is downloaded:

   The script will automatically download necessary NLTK data packages if they are not already present.

## Usage

Run the script to generate text files with paragraphs:

```bash
python generate_paragraphs.py
```

You will be prompted to enter the number of paragraphs per file and the number of files to generate.

## Features

- Generates grammatically coherent paragraphs using the NLTK Brown corpus.
- Corrects grammar, spelling, and punctuation using LanguageTool.
- Handles punctuation spacing and removes double punctuation marks.

## License

This project is licensed under the MIT License.
