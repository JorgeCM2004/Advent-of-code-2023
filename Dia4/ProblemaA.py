def match(search: int, l: list) -> int:
    matches = 0
    for i in l:
        if search == i:
            matches += 1
    return matches

if __name__ == '__main__':
    input_file_name = 'Dia4/ProblemaA_input.txt'
    output_file_name = 'Dia4/ProblemaA_output.txt'
    points = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            exponent = -1
            a, b = line.split(': ')
            line = b
            a, b = line.split(' | ')
            wins = list(map(int, a.strip().split()))
            game = list(map(int, b.strip().split()))
            for i in wins:
                exponent += match(i, game)
            if exponent > -1:
                points += 2 ** exponent
            
    with open(output_file_name, 'w') as file:
        file.write(str(points))
