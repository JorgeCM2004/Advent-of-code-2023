def match(search: int, l: list) -> int:
    out = 1
    copy_search = search
    for i in l[search][0]:
        if i in l[search][1]:
            copy_search += 1
            out += match(copy_search, l)
    return out

if __name__ == '__main__':
    input_file_name = 'Dia4/ProblemaB_input.txt'
    output_file_name = 'Dia4/ProblemaB_output.txt'
    scratchcards = []
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
            scratchcards.append((wins, game))
        for i in range(len(scratchcards)):
            points += match(i, scratchcards)
            
    with open(output_file_name, 'w') as file:
        file.write(str(points))