"""
Dear end-user,
Here is a simple program to extract hex from a file
because sometimes you're on a machine with no hex editor, and
you need to edit some hex. The sister program hex-repack.py
will shove it back together after you are done editing with
any standard text editor like Nano cause you never
figured out how to exit Vim, but you know how to edit hex.
:P all jokes aside, enjoy.

FF D8 FF DB - jpg
EF BB BF - txt
55 AA 00 00 - MBR
"""


def extract_hex(input_file, output_file):
    with open(input_file, 'rb') as f:
        # Read binary data from input file
        binary_data = f.read()

    # Convert binary data to hexadecimal string
    hex_data = binary_data.hex()

    # Write hexadecimal data to output file
    with open(output_file, 'w') as f:
        f.write(hex_data)


if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to save the output text version hex file: ")
    extract_hex(input_file, output_file)
