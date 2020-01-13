"""This Python file contains helper functions using the Wagner-Fisher Algorithm
to determine the least number of moves (insertions, deletions, replacements) to
convert a string into another desired string.

The Wagner-Fisher Algorithm is used to determine the minimum edit distance and
the corresponding moves. This is accomplished by tracking changes in a matrix
which is then traversed to determine the moves. Note that a replacement is
equivalent to a deletion followed by an insertion, but is still considered to be
a single move.

Convention:

Insert​ <​index​>, ​‘<char>’
Inserts ​<char> a​t the given ​<index>.​ For eg. I​nsert 1, ‘c’​ on “brain” gives
“bcrain”.

Delete​ <​index​>
Deletes the character at the given ​<index>​.

Replace​ <​index​>, ​‘<new-char>’
Replaces character at ​<index>​ with ​<new-char>​.
"""

# Constants
INSERTION_ID = 1
DELETION_ID = 2
REPLACEMENT_ID = 3

def modified_parse(input_file_path):
    """Parses the original and desired strings from an input file

    Args:
        input_file_path (str): path to input file with two strings on separate
        lines

    Returns:
        A tuple containing the original and desired string
    """
    try:
        file1 = open(input_file_path, "r+")
    except:
        return ("", "")

    original_string = file1.readline()[0:-1]
    desired_string = file1.readline()[0:-1]

    file1.close()
    return original_string, desired_string

def compute_DP_matrix(s1, s2):
    """Generates dp matrix to store potential sets of actions to change the
    original string into the desired string

    Args:
        s1 (str): original string
        s2 (str): desired string

    Returns:
        A 2D list representation of the dp matrix
    """
    m = len(s1)
    n = len(s2)
    # Create a table to store results of subproblems. The original and desired
    # strings correspond with the columns and rows respectively.
    dp = []
    for i in range(0, m+1, 1):
        dp += [[]]
        for j in range(0, n+1, 1):
            dp[i] += [0]

    for i in range(1, m+1, 1):
        dp[i][0] = i
    for j in range(1, n+1, 1):
        dp[0][j] = j

    for j in range(1, n+1, 1):
        for i in range(1, m+1, 1):
            if s1[i-1] == s2[j-1]:
                substitutionCost = 0
            else:
                substitutionCost = 1

            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + substitutionCost)
    return dp

def process_DP_matrix(s1, s2, dp):
    """Traverses dp matrix from the bottom right corner to the top left corner
    to determine the set of the least number of actions to convert the original
    string into the desired string

    Args:
        s1 (str): original string
        s2 (str): desired string
        dp (list): 2D list containing the dp matrix

    Returns:
        A 2D list of actions [[Action1],[Action2],...]. Each action is a list of
        the format [ActionID,Index,Character].
    """
    i = len(s1)
    j = len(s2)

    # Initialize array to store actions corresponding with minimum edit distance
    actions = []

    # Traverse DP_matrix to get actions up to and including when the top left
    # corner is reached.
    while (i >= 0 and j >= 0):

        # Check if characters are the same (i.e. do nothing)
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1

        # Check for replacement case
        elif dp[i][j] == dp[i-1][j-1] + 1:
            actions.insert(0, [REPLACEMENT_ID, i-1, s2[j-1]])
            i -= 1
            j -= 1

        # Check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, [DELETION_ID, i-1, "not applicable"])
            i -= 1

        # Check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, [INSERTION_ID, i, s2[j-1]])
            j -= 1

        # Edge case where the first letter of each word (top left corner of dp)
        # are the same. This is required to avoid an infinite loop.
        else:
            i -= 1
            j -= 1

    return actions

def batch_sort_actions(actions):
    """Sorts actions obtained from dp matrix such that the correct indices for
    each action are respected. This ensures that the final set of actions
    actually changes the original string into the desired string.

    Args:
        actions (list): 2D list of actions [[Action1],[Action2],...] where each
        action is a list of the format [ActionID,Index,Character]

    Returns:
        A 2D list of actions [[Action1],[Action2],...].
    """
    processed_actions = []
    insertion_deletion_dict = {}

    # Since replacements do not affect indices, all of the replacments should be
    # performed first. Therefore they should also be stored first since they
    # require no further processing.
    for action in actions:
        if action[0] == REPLACEMENT_ID:
            processed_actions += [action]
        else:
            # Since insertions and deletions affect indices, they are stored
            # into a dictionary where the action's index is the key and the
            # value is a list containing the action. The dictionary allows
            # actions affecting the same index to be stored together
            if action[1] not in insertion_deletion_dict:
                insertion_deletion_dict[action[1]] = [action]
            else:
                insertion_deletion_dict[action[1]].append(action)

    # Since insertions and deletions at higher indices do not affect the
    # positions of lower indices, they should be performed first and thus be put
    # in the processed_actions before actions at lower indices.

    # Also note that if multiple actions are meant to be performed at the same
    # index, the first action will affect the indices of the future actions.
    # Thus, the later insertions/deletions should once again be performed first.

    for index in reversed(sorted(insertion_deletion_dict.keys())):
        # Store the actions at each index in reversed order
        processed_actions += reversed(insertion_deletion_dict[index])

    return processed_actions


def format_actions(actions):
    """Formats actions into the required convention.

    Args:
        actions (list): 2D list of actions [[Action1],[Action2],...] where each
        action is a list of the format [ActionID,Index,Character]
        
    Returns:
        A list of strings corresponding to each action. Each string is of the
        form "Insert​ <​index​>, ​‘<char>’", "Delete​ <​index​>", or
        "Replace​ <​index​>, ​‘<new-char>’"
    """
    best_path = []

    for action in actions:

        if action[0] == INSERTION_ID:
            best_path.append('Insert %d, \'%c\'' % (action[1], action[2]))

        elif action[0] == DELETION_ID:
            best_path.append('Delete %d' % (action[1]))

        elif action[0] == REPLACEMENT_ID:
            best_path.append('Replace %d, \'%c\'' % (action[1], action[2]))

    return best_path
