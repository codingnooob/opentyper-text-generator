import lorem
import os

def generate_paragraphs(num_paragraphs, num_files):
    for i in range(num_files):
        paragraphs = [lorem.paragraph() for _ in range(num_paragraphs)]
        file_name = f"paragraphs_{i+1}.txt"
        with open(file_name, 'w') as file:
            file.write("\n\n".join(paragraphs))
        print(f"Generated {file_name}")

if __name__ == "__main__":
    num_paragraphs = int(input("Enter the number of paragraphs per file: "))
    num_files = int(input("Enter the number of files to generate: "))
    generate_paragraphs(num_paragraphs, num_files)
