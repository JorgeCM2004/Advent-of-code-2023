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
input_file_name = 'Dia1/ProblemaA_input.txt'
output_file_name = 'Dia1/ProblemaA_output.txt'
calibration_values = 0
with open(input_file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        calibration_values += search_first(line) + search_last(line)
with open(output_file_name, 'w') as file:
    file.write(str(calibration_values))
