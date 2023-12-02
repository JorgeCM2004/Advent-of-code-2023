def replace_unnecesary(string: str) -> str:
    string = string.replace('red', '0')
    string = string.replace('green', '1')
    string = string.replace('blue', '2')
    string = string.replace(',', '')
    string = string.replace(':', '')
    string = string.replace(';', '')
    return string

if __name__ == '__main__':
    input_file_name = 'Dia2/ProblemaB_input.txt'
    output_file_name = 'Dia2/ProblemaB_output.txt'
    posible_games = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            colors = [0, 0, 0]
            line = replace_unnecesary(line)
            list_line = list(line.split())
            searcher = 2
            while searcher < len(list_line):
                if int(list_line[searcher]) > colors[int(list_line[searcher + 1])]:
                    colors[int(list_line[searcher + 1])] = int(list_line[searcher])
                searcher += 2
            posible_games += colors[0] * colors[1] * colors[2]
            
    with open(output_file_name, 'w') as file:
        file.write(str(posible_games))

