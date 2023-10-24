"""
Arithmetic arranger module for computing & formatting
arithmetic problems (Addition and subtraction)
"""


def add(a, b):
  """
  Add two operands.
  """
  return a + b


def subtract(a, b):
  """
  Subtract two operands.
  """
  return a - b


def arithmetic_arranger(problems, display_answers=False):
  """Compute and format problems.

    Args:
        problems (list): List of arithmetic problems.
        display_answers (bool, optional): Show answers. Defaults to False.

    Returns:
        str: Returns the formatted arithmetic problems as a single string.
    """
  # Check if the number of problems exceeds the limit
  if len(problems) > 5:
    return "Error: Too many problems."

  top_line = ""
  middle_line = ""
  bottom_line = ""
  answer_line = ""

  for problem in problems:
    # Split the problem into components
    a, operator, b = problem.split()

    # Check if the operator is valid
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Check if the operands are numeric
    if not a.isdigit() or not b.isdigit():
      return "Error: Numbers must only contain digits."

    # Check if the operands have more than 4 digits
    if len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Determine the length of the longest operand
    max_length = max(len(a), len(b))

    # Format the problem vertically
    top_line += a.rjust(max_length + 2)
    middle_line += operator + " " + b.rjust(max_length)
    bottom_line += "-" * (max_length + 2)
    if display_answers:
      if operator == '+':
        answer = str(add(int(a), int(b))).rjust(max_length + 2)
      else:
        answer = str(subtract(int(a),
                              int(b))).rjust(max_length + 2)
      answer_line += answer

    # Add four spaces between problems
    if problem != problems[-1]:
      top_line += "    "
      middle_line += "    "
      bottom_line += "    "
      if display_answers:
        answer_line += "    "

  # Return the formatted string with or without answers
  if display_answers:
    return f"{top_line}\n{middle_line}\n{bottom_line}\n{answer_line}"
  return f"{top_line}\n{middle_line}\n{bottom_line}"
