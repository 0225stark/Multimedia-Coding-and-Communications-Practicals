import math

#Fixed Length Encoding Function
def fixed_length_coding(message):
    # Convert the message to an array of characters
    message_chars = list(message)
   
    encoded_msg = ""
   
    # Calculate the minimum number of bits required to represent the message length
    msg_len_bits = math.ceil(math.log2(len(message)))
   
    for char in message_chars:
        # Convert the character to its ASCII code (a number between 0 and 255)
        ascii = ord(char)
        print(ascii)
        # Convert the ASCII code to binary representation with 8 bits
        binary = format(ascii, "08b")
        print(binary)
        #Take the last msg_len_bits bits of the binary code
        binary = binary[-msg_len_bits:]
       
        # Append the binary code to the encoded message
        encoded_msg += binary
   
    return encoded_msg

#main code

fhand = open('input.txt')
message = fhand.read()       
encoded_msg = fixed_length_coding(message)
print('Fixed length encoded string:- ')
print(encoded_msg)             

print("\nLength of string before compression:- ",len(message))
print("Size of string in bit after compression:- ",len(encoded_msg))
print("Compression ratio:- ",len(encoded_msg)/(math.ceil(math.log2(len(message)))*len(message)))