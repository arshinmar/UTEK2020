#main2
from part2 import *
import sys

if __name__ == "__main__":
    # get file path
    command_line_args = sys.argv
    filename = command_line_args[1] #Command_line_input = python main3.py filename

    original_string, desired_string = modified_parse(filename)

    dp = compute_DP_matrix(original_string, desired_string)
    actions = process_DP_matrix(original_string, desired_string, dp)

    # write to file
    with open(filename[0:len(filename)-3] + ".out" , "w") as output_file:
        for action in actions:
            output_file.write(action + "\n")
