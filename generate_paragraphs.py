import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import brown

# Ensure the Brown corpus is downloaded
nltk.download('brown')
import os
import language_tool_python
import re

def generate_paragraphs(num_paragraphs, num_files):
    tool = language_tool_python.LanguageTool('en-US')
    for i in range(num_files):
        paragraphs = []
        for _ in range(num_paragraphs):
            sentences = [' '.join(sentence) for sentence in random.sample(list(brown.sents()), 5)]
            paragraph = ' '.join([' '.join(word_tokenize(sentence)) for sentence in sent_tokenize(' '.join(sentences))])
            # Correct grammar and spelling
            paragraph = tool.correct(paragraph)
            paragraphs.append(paragraph)
        file_name = f"paragraphs_{i+1}.txt"
        with open(file_name, 'w') as file:
            file.write("\n\n".join(paragraphs))
        print(f"Generated {file_name}")

if __name__ == "__main__":
    num_paragraphs = int(input("Enter the number of paragraphs per file: "))
    num_files = int(input("Enter the number of files to generate: "))
    generate_paragraphs(num_paragraphs, num_files)
