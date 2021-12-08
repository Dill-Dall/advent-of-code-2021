# part 1
with open('3.txt') as inputFile:
    list_of_binaries = inputFile.read().splitlines()


def doit(binary_list):
    sum_array = [0 for i in range(len(binary_list[0]))]
    sum = 0
    binary_list_div = len(binary_list)/2
    gamma_binary = ''
    epsilon_binary = ''
    for binary in binary_list:
        for bit_index in range(len(binary)):
            sum_array[bit_index] += int(binary[bit_index])
    for val in range(len(sum_array)):
        if(sum_array[val] > binary_list_div):
            gamma_binary += '1'
            epsilon_binary += '0'
        else:
            gamma_binary += '0'
            epsilon_binary += '1'

    print(gamma_binary)
    print(int(gamma_binary, 2))
    print(epsilon_binary)

    print(int(epsilon_binary, 2))
    print(int(gamma_binary, 2)*int(epsilon_binary, 2))


# part 2
def doit2(list_of_binaries2):
    binary_2d_Array = binary_list_to_2d_array(list_of_binaries2)
    oxyval = getDiagnostic(binary_2d_Array, "oxy")
    co2 = getDiagnostic(binary_2d_Array, "")

    print(oxyval)
    print(co2)
    print(int(oxyval, 2)*int(co2, 2))


def getDiagnostic(binary_list, type):
    active_table = binary_list

    for col in range(len(active_table[0])):
        binary_list_div = len(active_table)/2
        col_sum = 0
        temp_table = []

        for row in range(len(active_table)):
            col_sum += active_table[row][col]

        for row in range(len(active_table)):
            bit_val = active_table[row][col]

            if(type == "oxy"):
                if(col_sum > binary_list_div and bit_val == 1) or (col_sum < binary_list_div and bit_val == 0) or (col_sum == binary_list_div and bit_val == 1):
                    temp_table.append(active_table[row])
                    binary_list_div = len(active_table)/2
            else:
                if(col_sum < binary_list_div and bit_val == 1) or (col_sum > binary_list_div and bit_val == 0) or (col_sum == binary_list_div and bit_val == 0):
                    temp_table.append(active_table[row])
                    binary_list_div = len(active_table)/2

        if(len(temp_table) == 0):
            return list_bit_array_to_string(active_table)

        active_table = temp_table
    return list_bit_array_to_string(active_table)


def list_bit_array_to_string(lista_array):
    return "".join([str(int) for int in lista_array[0]])


def binary_list_to_2d_array(list_of_binaries):
    binary_2d_array = []
    for binary in list_of_binaries:
        string_list = list(binary)
        int_list = []
        for bit in string_list:
            int_list.append(int(bit))
        binary_2d_array.append(int_list)
    return binary_2d_array


with open('3.txt') as inputFile:
    list_of_binaries2 = inputFile.read().splitlines()

doit2(list_of_binaries2)
