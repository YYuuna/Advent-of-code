def seat_code_to_bin(seat_code):
    bin_seat_code = list(map(lambda x: 0 if (x == 'F ' or x == "L") else 1, seat_code))
    return bin_seat_code


def flip_direction(direction):
    if direction == 'F': return 'B'
    if direction == 'B': return 'F'
    if direction == 'L': return 'R'
    if direction == 'R': return 'L'


def neighbors(seat_code):
    neighbors_list = []  # front back left back
    neighbors_seat_code = seat_code
    # front seat code
    i = 0
    for i in range(7, 0, -1):
        if seat_code[i] == 'B':
            break
    for i in range(i, 7):
        neighbors_seat_code[i] = flip_direction(neighbors_seat_code[i])
    neighbors_list.append(neighbors_seat_code)
    # back seat code
    # front seat code
    i = 0
    for i in range(7, 0, -1):
        if seat_code[i] == 'F':
            break
    for i in range(i, 7):
        neighbors_seat_code[i] = flip_direction(neighbors_seat_code[i])
    neighbors_list.append(neighbors_seat_code)
    # left seat code

    i = 0
    for i in range(10, 8, -1):
        if seat_code[i] == 'R':
            break
    for i in range(i, 10):
        neighbors_seat_code[i] = flip_direction(neighbors_seat_code[i])
    neighbors_list.append(neighbors_seat_code)
    # right seat code
    i = 0
    for i in range(10, 8, -1):
        if seat_code[i] == 'R':
            break
    for i in range(i, 10):
        neighbors_seat_code[i] = flip_direction(neighbors_seat_code[i])
    neighbors_list.append(neighbors_seat_code)
    return neighbors_list


def check_seat_neighbors(seat_code, seat_codes_list):
    empty_seats_list = []
    for neighbor_seat in neighbors(seat_code):
        if neighbor_seat not in seat_codes_list:
            empty_seats_list.append(neighbor_seat)
    if empty_seats_list: pass
    pass


def seat_code_to_id(seat_code):
    lower_row = 0
    upper_row = 127
    lower_column = 0
    upper_column = 7
    for i in range(7):
        if seat_code[i] == 'F':
            upper_row = upper_row - (upper_row - lower_row + 1) // 2
        else:
            lower_row = lower_row + (upper_row - lower_row + 1) // 2
    for i in range(7, 10):
        if seat_code[i] == 'L':
            upper_column = upper_column - (upper_column - lower_column + 1) // 2
        else:
            lower_column = lower_column + (upper_column - lower_column + 1) // 2
    seat_id = upper_row * 8 + upper_column
    return seat_id


def seat_id_max(seats_codes):
    seat_id_max = 0
    print(seats_codes)
    for seat_code in seats_codes:
        seat_id = seat_code_to_id(seat_code)
        print(seat_code,seat_id)
        if seat_id > seat_id_max: seat_id_max = seat_id
    return seat_id_max


with open("day-5-input.txt", 'r') as puzzle_input:
    empty_seat_list=[]
    seat_id_list=list(map(seat_code_to_id,puzzle_input.readlines()))
    for seat_id in seat_id_list:
        if seat_id-2 in seat_id_list and seat_id-1 not in seat_id_list:
            empty_seat_list.append(seat_id-1)
    print(empty_seat_list)

