def arithmetic_arranger(problems, result_display=False):
    # Possible Errors

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in range(len(problems)):
        if not problems[problem][0].isdigit():
            return "Error: Numbers must only be digits."
        elif not problems[problem][1].isdigit():
            return "Error: Numbers must only be digits."
        elif len(problems[problem][0]) > 4 or len(problems[problem][1]) > 4:
            return 'Error: Numbers should be less than 4 digits.'
        elif "+" in problems[problem]:
            continue
        elif "-" in problems[problem]:
            continue
        else:
            return "Error: Operator must be '+' or '-'."

    # ----------------------------------------

    # Extracting the operators into "operations"
    operations = list(map(lambda x: x.split()[1], problems))

    # list of all the operands
    numbers = []
    for problem in problems:
        n = problem.split()
        numbers.extend([n[0], n[2]])
    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4
    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if result_display:
        return_statement = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        return_statement = '\n'.join((top_row, bottom_row, dashes))
    return return_statement
