# Part 2
#Insertion followed by deletion is the same as replacement
#Insertion and deletion both modify the length of the string.
    # Replacement doesnt.
#Multiple solutions exist.


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
    while (i > 0 and j > 0):

        # check if characters are the same (i.e. do nothing)
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1

        # check for replacement case
        elif dp[i][j] == dp[i-1][j-1] + 1:
            actions.insert(0, 'Replace %d, \'%c\'' % (i-1, s2[j-1]) )
            #actions.append('Replace %d, \'%c\'' % (i-1, s2[j-1]) )
            i -= 1
            j -= 1

        # check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, 'Delete %d' % (i-1) )
            #actions.append('Delete %d' % (i-1) )
            i -= 1

        # check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, 'Insert %d, \'%c\'' % (j-1, s2[j-1]) )
            #actions.append('Insert %d, \'%c\'' % (j-1, s2[j-1]) )
            j -= 1

    return actions
