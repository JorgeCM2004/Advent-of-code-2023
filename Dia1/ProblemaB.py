def search_first(string: str) -> int:
    for i in string:
        try: 
            return (int(i) * 10)
        except:
            pass

def search_last(string: str) -> int:
    for i in reversed(string):
        try: 
            return int(i)
        except:
            pass

if __name__ == "__main__":
    input_file_name = 'Dia1/ProblemaB_input.txt'
    output_file_name = 'Dia1/ProblemaB_output.txt'
    str_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_numbers_reversed = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    calibration_values = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line1 = line
            line2 = ''.join(reversed(line))
            limit = 1
            while limit <= len(line1):
                aux_line = line1[0 : limit]
                for number in str_numbers:
                    if number in aux_line: 
                        line1 = line1.replace(number, str(str_numbers.index(number) + 1), 1)
                        limit -= len(number)
                limit += 1
            limit = 1
            while limit <= len(line2):
                aux_line = line2[0 : limit]
                for number in str_numbers_reversed:
                    if number in aux_line:
                        line2 = line2.replace(number, str(str_numbers_reversed.index(number) + 1), 1)
                        limit -= len(number)
                limit += 1
            line2 = ''.join(reversed(line2))
            calibration_values += search_first(line1) + search_last(line2)
    with open(output_file_name, 'w') as file:
        file.write(str(calibration_values))
