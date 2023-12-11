def how2win(time: int, distance: int) -> int:
    out = 0
    for x in range(time):
        if (time - x) * x > distance:
            out += 1
    return out

if __name__ == '__main__':
    input_file_name = 'Dia6/ProblemaB_input.txt'
    output_file_name = 'Dia6/ProblemaB_output.txt'
    race = {'times': [], 'distances': []}
    current_line = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if current_line == 0:
                aux = list(map(str, line.strip().split(' ')))
                while '' in aux:
                    aux.remove('')
                aux = aux[1:]
                race['times'] = aux
                current_line += 1
            elif current_line == 1:
                aux = list(map(str, line.strip().split(' ')))
                while '' in aux:
                    aux.remove('')
                aux = aux[1:]
                race['distances'] = aux
                current_line += 1
        time = ''
        distance = ''
        for i in range(len(race['distances'])):
            time += race['times'][i]
            distance += race['distances'][i]
        number_races = how2win(int(time), int(distance))

    with open(output_file_name, 'w') as file:
        file.write(str(number_races))
