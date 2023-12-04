def search_number(coord: tuple, limit0: int) -> tuple:
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    coords_between = [coord]
    number = matrix[coord[0]][coord[1]]
    y = coord[1]
    while y + 1 <= limit0 and matrix[coord[0]][y + 1] in numbers:
        y += 1
        number += matrix[coord[0]][y]
        coords_between.append((coord[0], y))
    y = coord[1]
    while y - 1 >= 0 and matrix[coord[0]][y - 1] in numbers:
        y -= 1
        number = matrix[coord[0]][y] + number
        coords_between.append((coord[0], y))
    return (int(number), coords_between)

def is_gear(coord: tuple, limit0: int, limit1: int) -> list:
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    coords_seen = []
    numbers_near = []
    for i in possible_moves:
        new_coord = (coord[0] + i[0], coord[1] + i[1])
        if 0 <= new_coord[0] <= limit0 and 0 <= new_coord[1] <= limit1 and matrix[new_coord[0]][new_coord[1]] in numbers and new_coord not in coords_seen:
            number, l = search_number(new_coord, limit0)
            coords_seen = coords_seen + l
            numbers_near.append(number)
    return numbers_near

if __name__ == '__main__':
    input_file_name = 'Dia3/ProblemaB_input.txt'
    output_file_name = 'Dia3/ProblemaB_output.txt'
    matrix = []
    sum_gears = 0
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            matrix.append(line)
        for i in range(len(matrix)):
            matrix[i] = matrix[i].replace('\n', '')
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if matrix[i][x] == '*':
                    gear = is_gear((i, x), len(matrix) - 1, len(matrix[i]) - 1)
                    if len(gear) == 2:
                        sum_gears += gear[0] * gear[1]
                
    with open(output_file_name, 'w') as file:
        file.write(str(sum_gears))
