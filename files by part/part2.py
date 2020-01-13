# Part 2
#Insertion followed by deletion is the same as replacement
#Insertion and deletion both modify the length of the string.
    # Replacement doesnt.
#Multiple solutions exist.

# Constants
INSERTION_ID = 1
DELETION_ID = 2
REPLACEMENT_ID = 3

# parser function for part 2 only
def modified_parse(input_file_path):
    """
    INPUT:
    ::str:: input_file_path
    OUTPUT:
    ::str:: original_string
    ::str:: desired_string
    """
    try:
        file1 = open(input_file_path, "r+")
    except:
        return ["",""]

    original_string = file1.readline()[0:-1]
    desired_string = file1.readline()[0:-1]

    file1.close()
    return original_string, desired_string

def compute_DP_matrix(s1, s2):
    m=len(s1)
    n=len(s2)
    # Create a table to store results of subproblems
    dp = []
    for i in range(0,m+1,1):
        dp += [[]]
        for j in range(0,n+1,1):
            dp[i] += [0]

    for i in range(1,m+1,1):
        dp[i][0] = i
    for j in range(1,n+1,1):
        dp[0][j] = j

    for j in range(1,n+1,1):
        for i in range(1,m+1,1):
            if s1[i-1] == s2[j-1]:
                substitutionCost = 0
            else:
                substitutionCost = 1

            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + substitutionCost)
    return dp

def process_DP_matrix(s1, s2, dp):
    # get lengths of the 2 strings
    i = len(s1)
    j = len(s2)

    # initialize array to store actions
    actions = []

    # traverse DP_matrix to get actions
    while (i >= 0 and j >= 0):

        # check if characters are the same (i.e. do nothing)
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1

        # check for replacement case
        elif dp[i][j] == dp[i-1][j-1] + 1:
            actions.insert(0, [REPLACEMENT_ID, i-1, s2[j-1]])
            #actions.insert(0, 'Replace %d, \'%c\'' % (i-1, s2[j-1]) )
            #actions.append('Replace %d, \'%c\'' % (i-1, s2[j-1]) )
            i -= 1
            j -= 1

        # check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, [DELETION_ID, i-1, "not applicable"])
            #actions.insert(0, 'Delete %d' % (i-1) )
            #actions.append('Delete %d' % (i-1) )
            i -= 1

        # check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, [INSERTION_ID, j-1, s2[j-1]])
            #actions.insert(0, 'Insert %d, \'%c\'' % (j-1, s2[j-1]) )
            #actions.append('Insert %d, \'%c\'' % (j-1, s2[j-1]) )
            j -= 1

    return actions

def batch_sort_actions(actions):
    # gets a list of actions
    processed_actions = []
    unsorted_insertion_deletions = []
    sorted_insertion_deletions = []


    for action in actions:
        if action[0] == REPLACEMENT_ID:
            processed_actions += [action]
            print("here start")
            print(len(actions))
            actions.remove(action)
            print(len(actions))
            print("hi")
            print("here end")
            print(action)
        else:
            unsorted_insertion_deletions += [action]

    print("unsorted")
    print(actions)

    # sort remaining actions (only deletions and insertions) by the index they affect
    sorted_insertion_deletions = sorted(unsorted_insertion_deletions, key = lambda x: x[1])

# check here

#    for i, remaining_action in enumerate(sorted_insertion_deletions):
#        if remaining_action[1] == INSERTION_ID:
#            for x in range(i+1, len(sorted_insertion_deletions)):
#                sorted_insertion_deletions[x][1] += 1 # insertion pushes indices up
#        elif remaining_action[1] == DELETION_ID:
#            for x in range(i+1, len(sorted_insertion_deletions)):
#                sorted_insertion_deletions[x][1] -= 1 # insertion pushes indices up
#        print(i)
#        print(remaining_action)

    #for remaining_action in sorted_insertion_deletions:
    #    if remaining_action[0] == INSERTION_ID:

    #    insertion_deletions += [action]

    print("only replaces")
    print(processed_actions)
    processed_actions += sorted_insertion_deletions

    print("all the stuff")
    print(processed_actions)

    return processed_actions

#   all replacements move to the top & merge
#   sort all inserts and deletes by index
#   update index +1 for insert
#   update index -1 for delete

def format_actions(path_segments):
    # path_segments is a list of segments of consective actions of same type
    # [[action_id, start_idx, end_idx, books], [...], [...], ...]
    best_path = []

    for seg in path_segments:

        if seg[0] == INSERTION_ID:
            best_path.append('Insert %d, \'%c\'' % (seg[1], seg[2]) )
            #best_path.insert(0, 'Insert %d-%d, %s' % (seg[1], seg[2], books) )
            #actions.append('Insert %d, \'%c\'' % (j-1, s2[j-1]) )

        elif seg[0] == DELETION_ID:
            best_path.append('Delete %d' % (seg[1]) )
            #best_path.insert(0, 'Delete %d-%d' % (seg[1], seg[2]) )
            #actions.append('Delete %d' % (i-1) )

        elif seg[0] == REPLACEMENT_ID:
            best_path.append('Replace %d, \'%c\'' % (seg[1], seg[2]) )
            #best_path.insert(0, 'Replace %d-%d, %s' % (seg[1], seg[2], books) )
            #actions.append('Replace %d, \'%c\'' % (i-1, s2[j-1]) )

    print(best_path)

    return best_path
