# File paths (you can change these as needed)
input_file = "input.txt"
output_file = "odd_lines.txt"

# Read from input file and write odd lines to output file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line_number, line in enumerate(infile, start=1):
        if line_number % 2 != 0:  # odd line
            outfile.write(line)

print(f"Odd-numbered lines have been copied from '{input_file}' to '{output_file}'.")
