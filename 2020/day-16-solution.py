import re
from interval import Interval
from pprint import pprint


def count_valid_columns(columns_list):
    count = 0
    for column in columns_list:
        count += column
    return count


with open("day-16-input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().split("\n\n")
    fields = puzzle_input[0]
    my_ticket = puzzle_input[1].split("\n")[1].split(',')
    nearby_tickets = puzzle_input[2].split("\n")[1:]

    # parsing fields rules
    field_rules = {}
    fields = fields.split("\n")
    for i in range(len(fields)):
        fields[i] = re.split(": | or |-", fields[i])
        field_rules[fields[i][0]] = {range(int(fields[i][bound]), int(fields[i][bound + 1]) + 1)
                                     for bound in range(1, len(fields[i]), 2)}
    # parsing nearby tickets
    for i in range(len(nearby_tickets)):
        nearby_tickets[i] = nearby_tickets[i].split(',')

    # finding bad filds
    invalid_tickets = set({})
    ticket_scaning_error_rate = 0


    def part_one(ticket_scaning_error_rate):
        for i in range(len(nearby_tickets)):
            valid_ticket = True
            for field_value in nearby_tickets[i]:
                field_value_is_valid = False
                for field_rule in (field_rules.values()):
                    for field_range in field_rule:
                        if int(field_value) in field_range:
                            field_value_is_valid = True
                            break
                    if field_value_is_valid: break
                if field_value_is_valid == False:
                    ticket_scaning_error_rate += int(field_value)
                    invalid_tickets.add(i)
        return ticket_scaning_error_rate


    print(part_one(0))


    def part_two(invalid_tickets):
        # parsing valid tickets
        fields_order = {}
        fields_validity = {}
        valid_tickets = set(range(len(nearby_tickets))).difference(invalid_tickets)
        valid_tickets = [nearby_tickets[i] for i in valid_tickets]
        valid_tickets.insert(0,my_ticket)
        print("debug")
        rows_count = len(field_rules)
        for field in field_rules:
            valid_order = [1] * rows_count
            for ticket_values in valid_tickets:
                for i in range(rows_count):
                    if valid_order[i] == 1:
                        ticket_value_is_valid = False
                        for field_range in field_rules[field]:
                            ticket_value_is_valid = int(ticket_values[i]) in field_range
                            if ticket_value_is_valid:
                                break
                        if ticket_value_is_valid:
                            continue
                        else:
                            valid_order[i] = 0

            fields_validity[field] = (valid_order)

        while(len(fields_order)<rows_count):
            for field in fields_validity:
                if count_valid_columns(fields_validity[field]) == 1:
                    fields_order[field] = fields_validity[field].index(1)
                    fields_validity.pop(field)
                    for other_field in fields_validity:
                        fields_validity[other_field][fields_order[field]] = 0
                    break
        answer=1
        for field in fields_order:
            if "departure" in field:
                answer*=int(my_ticket[fields_order[field]])
        pprint(fields_order)
        pprint(answer)


    part_two(invalid_tickets)
