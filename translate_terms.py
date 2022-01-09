import googletrans
import sys

if len(sys.argv) < 6:
    print("Available languages\n",googletrans.LANGUAGES)
    print("\nAbove is the available languages\n")
    print("To run the script use:\npython3 translate_terms [filename] [column to be translated] [language to translate to] [file name for output] [number of lines before data]")
    exit(1)



input_file = sys.argv[1]
translate_column = int(sys.argv[2]) -1
output_language = sys.argv[3]
output_file = sys.argv[4]
skip_lines = int(sys.argv[5])
input_language = "no"
csv_delimiter = ";"


translator = googletrans.Translator()


with open(input_file, "r") as input_csv:
    with open(output_file, "w") as output_csv:
        line_count = 1
        for line in input_csv:
            
            # skip all lines up to header row and include the non-translated headers
            if line_count < skip_lines:
                if line_count == skip_lines -1:
                    print(line.strip(), file=output_csv)
                    first_line = False
                line_count += 1
                continue

            input_row = line.split(csv_delimiter)
            input_row[translate_column] = translator.translate(input_row[translate_column], src=input_language, dest=output_language).text
            output_row = csv_delimiter.join(input_row)
            print(output_row.strip(), file=output_csv)




