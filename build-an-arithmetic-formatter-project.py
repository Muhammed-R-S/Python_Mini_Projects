def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

        if operator == '+':
            answer = str(int(first_operand) + int(second_operand))
        elif operator == '-':
            answer = str(int(first_operand) - int(second_operand))

        answers.append(answer)

    arranged_problems = []

    # First line
    first_line = '    '.join([f"{operand:>{max(len(first_operands[i]), len(second_operands[i])) + 2}}" for i, operand in enumerate(first_operands)])
    arranged_problems.append(first_line)

    # Second line
    second_line = '    '.join([f"{operators[i]} {operand:>{max(len(first_operands[i]), len(second_operands[i]))}}" for i, operand in enumerate(second_operands)])
    arranged_problems.append(second_line)

    # Third line
    third_line = '    '.join(['-' * (max(len(first_operands[i]), len(second_operands[i])) + 2) for i in range(len(problems))])
    arranged_problems.append(third_line)

    # Fourth line (if show_answers is True)
    if show_answers:
        fourth_line = '    '.join([f"{answer:>{max(len(first_operands[i]), len(second_operands[i])) + 2}}" for i, answer in enumerate(answers)])
        arranged_problems.append(fourth_line)

    return '\n'.join(arranged_problems)

# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems, show_answers=True)
print(result)
