def special_near(coord: list, limit0: int, limit1: int) -> bool:
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    normal_things = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    for i in possible_moves:
        new_coord = (coord[0] + i[0], coord[1] + i[1])
        if 0 <= new_coord[0] <= limit0 and 0 <= new_coord[1] <= limit1 and matrix[new_coord[0]][new_coord[1]] not in normal_things:
            return True
    return False

def should_sum(coord1: list, coord2: list, limit0: int, limit1: int) -> bool:
    while coord1[1] <= coord2[1]:
        if special_near(coord1, limit0, limit1):
            return True
        coord1[1] += 1
    return False

if __name__ == '__main__':
    input_file_name = 'Dia3/ProblemaA_input.txt'
    output_file_name = 'Dia3/ProblemaA_output.txt'
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    initial_coords = [0, 0]
    final_coords = [0, 0]
    matrix = []
    sum_part_number = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            matrix.append(line)
        for i in range(len(matrix)):
            matrix[i] = matrix[i].replace('\n', '')
        for i in range(len(matrix)):
            x = 0
            while x < len(matrix[i]):
                number = ''
                if matrix[i][x] in numbers:
                    initial_coords = [i, x]
                    number += matrix[i][x]
                    while x + 1 < len(matrix[i]) and matrix[i][x + 1] in numbers:
                        x += 1
                        number += matrix[i][x]
                    final_coords = [i, x]
                    if should_sum(initial_coords, final_coords, len(matrix) - 1, len(matrix[i]) - 1):
                        sum_part_number += int(number)
                x += 1
            
    with open(output_file_name, 'w') as file:
        file.write(str(sum_part_number))
