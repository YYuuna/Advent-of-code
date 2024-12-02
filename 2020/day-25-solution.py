import re


def transform(loop_size, subject_number):
    encryption_key = 1
    for i in range(loop_size):
        encryption_key = (encryption_key * subject_number) % 20201227
    return encryption_key


with open("day-25-input.txt", "r") as puzzle_input:
    puzzle_input = re.findall("\d+", puzzle_input.read())
    card_public_key = int(puzzle_input[0])
    door_public_key = int(puzzle_input[1])
    card_loop_size = 0
    door_loop_size = 0
    key = 1
    subject_number=7
    while (key != card_public_key):
        key = (key * subject_number) % 20201227
        card_loop_size += 1
    key = 1
    while (key != door_public_key):
        key = (key * subject_number) % 20201227
        door_loop_size += 1
    print(transform(card_loop_size,door_public_key))
