def replace_unnecesary(string: str) -> str:
    string = string.replace('red', '0')
    string = string.replace('green', '1')
    string = string.replace('blue', '2')
    string = string.replace(',', '')
    string = string.replace(':', '')
    string = string.replace(';', '')
    return string

if __name__ == '__main__':
    input_file_name = 'Dia2/ProblemaA_input.txt'
    output_file_name = 'Dia2/ProblemaA_output.txt'
    colors = [12, 13, 14]
    posible_games = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = replace_unnecesary(line)
            list_line = list(line.split())
            boolean = True
            searcher = 2
            while boolean and searcher < len(list_line):
                if int(list_line[searcher]) > colors[int(list_line[searcher + 1])]:
                    boolean = False
                searcher += 2
            if boolean:
                posible_games += int(list_line[1])
            
    with open(output_file_name, 'w') as file:
        file.write(str(posible_games))
