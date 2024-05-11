def convert_hex_to_binary(input_file, output_file):
    with open(input_file, 'r') as f:
        # Read hexadecimal data from input file
        hex_data = f.read().strip()

    # Convert hexadecimal string to binary data
    binary_data = bytes.fromhex(hex_data)

    # Write binary data to output file
    with open(output_file, 'wb') as f:
        f.write(binary_data)

if __name__ == "__main__":
    input_file = input("Enter the path to the text file containing hex data: ")
    output_file = input("Enter the path to save the output binary file with extension: ")
    convert_hex_to_binary(input_file, output_file)
