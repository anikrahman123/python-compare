# Bin files
BIN_FILE_1 = "file1.bin"
BIN_FILE_2 = "file2.bin"

# List to store 6 bit HEX numbers imported from first bin file
hex_1_list = []

# List to store 6 bit HEX numbers imported from second bin file
hex_2_list = []

# 01.
# Open both bin files and import all HEX numbers
with open(BIN_FILE_1) as bin1, open(BIN_FILE_2) as bin2:
    # Iterate through each line of first file
    for line in bin1:
        # And populate the bin_1_list
        hex_1_list.append(line.strip())

    # Iterate through each line of second file
    for line in bin2:
        # And populate the bin_2_list
        hex_2_list.append(line.strip())

# 02.
# Convert all HEX numbers to binary
bin_1_list, bin_2_list = [], []
for hex_num in hex_1_list:  # Before experiment
    # Convert HEX into DECIMAL then DECIMAL into BIN
    bin_num = "{0:06b}".format(int(hex_num, 16))
    # Append the converted hex into binary to the list
    bin_1_list.append(bin_num)
for hex_num in hex_2_list:  # After experiment
    # Convert HEX into DECIMAL then DECIMAL into BIN
    bin_num = "{0:06b}".format(int(hex_num, 16))
    # Append the converted hex into binary to the list
    bin_2_list.append(bin_num)

# List to store count of number of flipped bits
# for each set of before and after experiment
# binary number
flipped_bits_counts = []

# Iterate througfh each set of of before and after
# experiment binary numbers
for bin_before, bin_after in zip(bin_1_list, bin_2_list):
    flipped_bits_count = 0

    # Iterate through each bits
    for bit1, bit2 in zip(bin_before, bin_after):
        # If bit is flipped
        if bit1 != bit2:
            # Then increment the flipped_bits_count
            flipped_bits_count += 1

    # Insert the computed flipped_bits_count to the list
    flipped_bits_counts.append(flipped_bits_count)

# 03.
# Display the total number of flipped bits
for i, flipped_bits_num in enumerate(flipped_bits_counts):
    print(f"For experiment {i + 1}, total number of flipped bits is {flipped_bits_num}.")

# 04.
# Display the input and output addresses that
# contain flipped bits in binary
print("\n\nInput and output addresses that contain flipped bits in binary:")
print("{:15}{}".format("INPUT ADDR", "OUTPUT ADDR"))
for i, (input_add, output_add) in enumerate(zip(hex_1_list, hex_2_list)):
    # If input and output addresses contain
    # flipped bits in binary
    if flipped_bits_counts[i] > 0:
        # Display input and output addresses
        print("{:15}{}".format(input_add, output_add))

# 05.
# Indicate which bits are flipped on the output address
print("\n\nBits that are flipped on the output address:")
# Iterate througfh each set of of before and after
# experiment binary numbers
for bin_before, bin_after in zip(bin_1_list, bin_2_list):
    print("INPUT   BITS: ", bin_before)
    print("OUTPUT  BITS: ", bin_after)
    print("FLIPPED BITS: ", end=" ")

    # Iterate through each bits
    for bit1, bit2 in zip(bin_before, bin_after):
        # If bit is flipped
        if bit1 != bit2:
            # Indicate by ^
            print("^", end="")
        else:
            print(" ", end="")
    print("\n\n")
