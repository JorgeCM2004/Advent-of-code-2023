def classifier(card: str) -> str:
    maximum_length = [[0, card[0]]]
    jokers = 0
    generating_card = ''
    for i in card:
        if i == 'J':
            jokers += 1
        elif i in generating_card or generating_card == '':
            for x in range(len(maximum_length)):
                if maximum_length[x][1] == i:
                    maximum_length[x][0] += 1
        else:
            maximum_length.append([1, i])
        generating_card += i
    maximum_length.sort(reverse=True)
    out = maximum_length[0][0]
    out += jokers
    match out:
        case 5:
            return 'five_of_a_kind'
        case 4:
            return 'four_of_a_kind'
        case 3:
            if maximum_length[1][0] == 2:
                return 'full_house'
            else:
                return 'three_of_a_kind'
        case 2:
            if maximum_length[1][0] == 2:
                return 'two_pair'
            else:
                return 'one_pair'
        case 1:
            return 'high_card'

def sort_camel(l: list) -> list:
    replaces = (('A', 'a'), ('K', 'b'), ('Q', 'c'), ('T', 'd'), ('9', 'e'), ('8', 'f'), ('7', 'g'), ('6', 'h'), ('5', 'i'), ('4', 'j'), ('3', 'k'), ('2', 'l'), ('J', 'm'))
    for i in range(len(l)):
        card = l[i][0]
        number = l[i][1]
        for x in replaces:
            card = card.replace(x[0], x[1])
        l[i] = (card, number)
    l.sort()
    return l

if __name__ == '__main__':
    input_file_name = 'Dia7/ProblemaB_input.txt'
    output_file_name = 'Dia7/ProblemaB_output.txt'
    classified = {'five_of_a_kind': [], 'four_of_a_kind': [], 'full_house': [], 'three_of_a_kind': [], 'two_pair': [], 'one_pair': [], 'high_card': []}
    winnings = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        len_lines = len(lines)
        for line in lines:
            aux = tuple(map(str, line.strip().split(' ')))
            classified[classifier(aux[0])].append((aux[0], int(aux[1])))
        for i in list(classified.keys()):
            classified[i] = sort_camel(classified[i])
            for x in classified[i]:
                winnings += x[1] * len_lines
                len_lines -= 1

    with open(output_file_name, 'w') as file:
        file.write(str(winnings))
