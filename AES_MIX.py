#since we are using hex in python we need a way to print hex values

def dec_to_hex(dec_num):
    return "{:02x}".format(dec_num)

#AES uses galois multiplication with 2 bytes

def galois_multiplication(byte_a, byte_b):
    if byte_b == 1:
        return byte_a
    bitwise_operation = (byte_a << 1) & 0xff

    if byte_b == 2:
        return bitwise_operation if byte_a < 128 else bitwise_operation ^ 0x1b

    if byte_b == 3:
        return galois_multiplication(byte_a, 2) ^ byte_a

#next we need to do the mix tabel

def mix_table(val_1, val_2, val_3, val_4): 
    row_1 = galois_multiplication(val_1, 2) ^  galois_multiplication(val_2, 3) ^ galois_multiplication(val_3, 1) ^ galois_multiplication(val_4, 1) 
    row_2 = galois_multiplication(val_1, 1) ^  galois_multiplication(val_2, 2) ^ galois_multiplication(val_3, 3) ^ galois_multiplication(val_4, 1)
    row_3 = galois_multiplication(val_1, 1) ^  galois_multiplication(val_2, 1) ^ galois_multiplication(val_3, 2) ^ galois_multiplication(val_4, 3)
    row_4 = galois_multiplication(val_1, 3) ^  galois_multiplication(val_2, 1) ^ galois_multiplication(val_3, 1) ^ galois_multiplication(val_4, 2)

    print (dec_to_hex(row_1),
           dec_to_hex(row_2),
           dec_to_hex(row_3),
           dec_to_hex(row_4))

#now we got to run the tabel with all the 88's

    mix_table(0x88, 0x88, 0x88, 0x88)