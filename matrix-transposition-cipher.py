def ciphertext(string, array):
    string = string.replace(' ', '%')

    columns = max(array)

    cipher_matrix = []
    matrix_row = [''] * columns
    row_count = 0
    col_count = 0

    for i in range(len(string)):
        matrix_row[col_count] = string[i]

        if col_count == columns-1:
            col_count = 0
            row_count += 1
            cipher_matrix.append(matrix_row)
            matrix_row = [''] * columns
        else:
            col_count += 1

        if i == len(string)-1:
            cipher_matrix.append(matrix_row)

    for i in range(len(cipher_matrix)):
        for j in range(len(cipher_matrix[0])):
            if cipher_matrix[i][j] == '':
                cipher_matrix[i][j] = '%'

    final_cipher = ''

    for a in range(len(array)):
        for b in range(len(cipher_matrix[0])):
            final_cipher += cipher_matrix[b][array[a]-1]

    return final_cipher


def plaintext(cipher, key_array):
    columns = max(key_array)
    rows = int(len(cipher) / columns)

    col_counter = 0
    row_counter = 0
    key_matrix = [['' for x in range(columns)] for y in range(rows)]

    #print(key_matrix)

    for i in range(len(cipher)):

        key_matrix[row_counter][key_array[col_counter] - 1] = cipher[i]

        if row_counter == rows-1:
            row_counter = 0
            col_counter += 1

        else:
            row_counter += 1

    final_plain = ''

    for i in range(len(key_matrix)):
        for j in range(len(key_matrix[0])):
            final_plain += key_matrix[i][j]

    final_plain = final_plain.replace('%', ' ')

    return final_plain


if __name__ == '__main__':
    #test = "meet at military house"

    #permutation = [5, 4, 1, 2, 3]

    #confused = 'rsiet%u!rsi%sietcyetcyu!cyu!r%'

    #final = ciphertext(test, permutation)

    #final_two = plaintext(confused, permutation)

    #print('Matrix Transposition Cipher\nPlaintext to Ciphertext')
    #print(test + '  -->  ' + final +'\n')

    #print('Ciphertext to Plaintext')

    #print(confused + '  -->  ' + final_two)

    array_size = int(input('Enter the size of key integer array: '))

    key = []

    for i in range(array_size):
        integer = int(input("Enter number to store in integer array: "))

        key.append(integer)

    option = input('\nEnter 1 to create Ciphertext and 2 to create Plaintext: ')
    option = int(option)
    good_option = False

    while not good_option:
        if option == 1:

            # The input for this cipher text is the file: matrix-ciphertext-input.txt
            ciphertext_file = input('Enter the filename to create ciphertext (including \".txt\"): ')

            open_file = open(ciphertext_file, 'r')

            text = ''
            a = True

            while a:
                line = open_file.readline()

                if line == '':
                    a = False
                else:
                    text += line

            result_cipher = ciphertext(text, key)

            ciphertext_output = open('ciphertext-output.txt', 'w')

            ciphertext_output.write(result_cipher)

            ciphertext_output.close()

            print('\nOutput in is file \"ciphertext-output.txt\"')

            good_option = True

        elif option == 2:

            # The input for this plain text is the file: matrix-plaintext-input.txt
            plaintext_file = input('Enter the filename to create plaintext (including \".txt\"): ')

            open_file = open(plaintext_file, 'r')

            text = ''
            a = True

            while a:
                line = open_file.readline()

                if line == '':
                    a = False
                else:
                    text += line

            result_plain = plaintext(text, key)

            plaintext_output = open('plaintext-output.txt', 'w')

            plaintext_output.write(result_plain)

            plaintext_output.close()

            print('\nOutput in is file \"plaintext-output.txt\"')

            good_option = True

        else:
            print('Incorrect input! Try again!')
            option = input('Enter 1 for Encryption and 2 for Decryption: ')
            option = int(option)