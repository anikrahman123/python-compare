f1 = open("address.txt","w")
f2 = open("oldtest.txt","w")
f3 = open("newtest.txt","w")
for i in open("outputfromprompt.txt", "r").readlines():
    str1=i.split(" ")
    f1.write(str1[0].replace(":"," ") + "\n")
    f2.write(str1[1]+"\n")
    f3.write(str1[2])
    



f1.close()
f2.close()
f3.close()

# Bin files OUTPUT file is the output of thw command prompt which shows the addresses, original, and motified data
BIN_FILE_1 = "oldtest.txt"
BIN_FILE_2 = "newtest.txt"
ADD_FILE_1 = "address.txt"
#OUTPUT_FILE = "output.bin"
# List to store 6 bit HEX numbers imported from first bin file
hex_1_list = []

# List to store 6 bit HEX numbers imported from second bin file
hex_2_list = []

#list to store address imported from third bin file
add_1_list = []

# 01.
# Open three bin files and import all HEX numbers
with open(BIN_FILE_1) as bin1, open(BIN_FILE_2) as bin2, open(ADD_FILE_1) as add:
    # Iterate through each line of first file
    for line in bin1:
        # And populate the bin_1_list
        hex_1_list.append(line.strip())

    # Iterate through each line of second file
    for line in bin2:
        # And populate the bin_2_list
        hex_2_list.append(line.strip())
    for line in add:
        add_1_list.append(line.strip())

# 02.
# Convert all HEX numbers to binary
bin_1_list, bin_2_list = [], []
for hex_num in hex_1_list:  # Before experiment
    # Convert HEX into DECIMAL then DECIMAL into BIN
    bin_num = "{0:08b}".format(int(hex_num, 16))
    # Append the converted hex into binary to the list
    bin_1_list.append(bin_num)
for hex_num in hex_2_list:  # After experiment
    # Convert HEX into DECIMAL then DECIMAL into BIN
    bin_num = "{0:08b}".format(int(hex_num, 16))
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
compare_data= open('compare.txt','w')
#this compare_data file is the file that contains the output of the script. This will display all the flipped bits in the data
# Display the total number of flipped bits
for i, flipped_bits_num in enumerate(flipped_bits_counts):
    print(f"For address row {i + 1}, total number of flipped bits is {flipped_bits_num}.")
    compare_data.write(f"\nFor address row {i + 1}, total number of flipped bits is {flipped_bits_num}.")
total_bits = sum(flipped_bits_counts)
print(f"The total number of flipped bits in the whole experiment is {total_bits}.")
compare_data.write(f"\nThe total number of flipped bits in the whole experiment is {total_bits}.")

# 04.
# Display the input and output addresses that
# contain flipped bits in binary
print("\n\nInput and output addresses that contain flipped bits in binary:")
compare_data.write("\n\nInput and output addresses that contain flipped bits in binary:\n")
print("{:15}{}".format("INPUT ADDR", "OUTPUT ADDR"))
compare_data.write("{:15}{}".format("\nINPUT ADDR", "OUTPUT ADDR\n"))
for i, (input_add, output_add) in enumerate(zip(hex_1_list, hex_2_list)):
    # If input and output addresses contain
    # flipped bits in binary
    if flipped_bits_counts[i] > 0:
        # Display input and output addresses
        print("{:15}{}".format(input_add, output_add))
        compare_data.write("\n{:15}{}".format(input_add, output_add))

# 05.
count1 = 0
#count1 counts the number of 1's that are flipped to 0 in the data
# Indicate which bits are flipped on the output address
print("\n\nBits that are flipped on the output address:")
compare_data.write("\n\nBits that are flipped on the output address:")
# Iterate througfh each set of of before and after
# experiment binary numbers
for bin_before, bin_after,i in zip(bin_1_list, bin_2_list, add_1_list):
    print(f"ADDRESS: ", str(i))
    compare_data.write(f"ADDRESS:  {i}\n")
    print("INPUT   BITS: ", bin_before)
    compare_data.write(f"INPUT   BITS: {bin_before}\n")
    print("OUTPUT  BITS: ", bin_after)
    compare_data.write(f"OUTPUT  BITS: {bin_after}\n")
    print("FLIPPED BITS: ", end=" ")
    compare_data.write("FLIPPED BITS: ")

    # Iterate through each bits
    for bit1, bit2 in zip(bin_before, bin_after):
        # If bit is flipped
        if bit1 != bit2:
            # Indicate by ^
            print("^", end="")
            compare_data.write("^")
            if bit1 == "1":
                count1 = count1+1
        else:
            print(" ", end="")
            compare_data.write(" ")
    print("\n\n")
    compare_data.write("\n\n")
#prints out the percentage of 1's that are flipped to 0 and 0's that are flipped to 1
print(f"The total percentage of 1's flipped to 0 is: {(count1/total_bits)*100} %")
compare_data.write(f"The total percentage of 1's flipped to 0 is: {(count1/total_bits)*100} %\n")
print(f"The total percentage of 0's flipped to 1 is: {100-((count1/total_bits)*100)} %")
compare_data.write(f"The total percentage of 0's flipped to 1 is: {100-((count1/total_bits)*100)} %\n")

myfile = open("address.txt","r")

file_data = myfile.read()

 

address_list = file_data.split()

same_list=[]
for i in address_list:
    sub =i[:-1]
    for j in address_list:
        if(i!= j and j[:-1] == sub and (i not in same_list)):
            same_list.append(i)
            same_list.append(j)


count = 0
for i in range(0,len(same_list),2):
    print("{} and {} have multiple bit upsets".format(same_list[i],same_list[i+1]))
    compare_data.write("{} and {} have multiple bit upsets".format(same_list[i],same_list[i+1]))
    count = count +1
print("There are " + str(count)+ " number of multible bit errors in this code")
compare_data.write(f"There are " + str(count)+ f" number or multible bit errors in this code %\n")
compare_data.close()
