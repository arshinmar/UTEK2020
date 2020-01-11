# Constants
INSERTION_ID = 1
DELETION_ID = 2
REPLACEMENT_ID = 3

def generate():
    actions = ['Insert​ ​0-0​, ​"Religion and Mythology, Neil Potts"','Delete​ ​2-3','Insert​ ​3-4​, ​"Foundation, Isaac Asimov"​ ​"Intro to Algorithms, Thomas Cormen"']

    with open("something.out" , "w") as output_file:
        for action in actions:
            output_file.write(action + "\n")

    return True

#generate()
s1 = "Sunday"
s2 = "Saturday"

dp = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 0, 1, 2, 3, 4, 5, 6, 7],
    [2, 1, 1, 2, 2, 3, 4, 5, 6],
    [3, 2, 2, 2, 3, 3, 4, 5, 6],
    [4, 3, 3, 3, 3, 4, 3, 4, 5],
    [5, 4, 3, 4, 4, 4, 4, 3, 4],
    [6, 5, 4, 4, 5, 5, 5, 4, 3]]


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
            i -= 1
            j -= 1

        # check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, 'Delete %d' % (i-1) )
            i -= 1

        # check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, 'Insert %d, \'%c\'' % (j-1, s2[j-1]) )
            j -= 1

    print(actions)

    return actions
    #print(actions)

def process_DP_matrix2(s1, s2, dp):
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
            actions.insert(0, [REPLACEMENT_ID, i-1, s2[j-1]])
            i -= 1
            j -= 1

        # check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, [DELETION_ID, i-1, "not applicable"])
            i -= 1

        # check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, [INSERTION_ID, j-1, s2[j-1]])
            j -= 1

    print(actions)

    return actions


best_path = [[1, 2, 5,['Religion and Mythology, Neil Potts', 'Ancient Egypt, unknown', 'Intro to Algorithms, Thomas Cormen',
'Foundation, Isaac Asimov', 'Intro to Algorithms, Thomas Cormen']],
[2, 4,5,['Religion and Mythology, Neil Potts', 'Ancient Egypt, unknown', 'Intro to Algorithms, Thomas Cormen',
'Foundation, Isaac Asimov', 'Intro to Algorithms, Thomas Cormen']],
[3, 7, 8,['Religion and Mythology, Neil Potts', 'Ancient Egypt, unknown', 'Intro to Algorithms, Thomas Cormen',
'Foundation, Isaac Asimov', 'Intro to Algorithms, Thomas Cormen']]]
"""
def print_best_path(path_segments):
    # path_segments is a list of segments of consective actions of same type
    # [[action_id, start_idx, end_idx, books], [...], [...], ...]
    best_path = ""

    for seg in path_segments:
        books = ""
        for book in seg[3]:
            books += '"%s"' %(str(book)) + ' '
        books = books[0:-1]

        if seg[0] == INSERTION_ID:
            best_path += 'Insert %d-%d, %s\n' % (seg[1], seg[2], books)

        elif seg[0] == DELETION_ID:
            best_path += 'Delete %d-%d\n' % (seg[1], seg[2])

        elif seg[0] == REPLACEMENT_ID:
            best_path += 'Replace %d-%d, %s\n' % (seg[1], seg[2], books)

    print(best_path)
    return best_path
"""
def print_best_path(path_segments):
    # path_segments is a list of segments of consective actions of same type
    # [[action_id, start_idx, end_idx, books], [...], [...], ...]
    best_path = []

    for seg in path_segments:
        books = ""
        for book in seg[3]:
            books += '"%s"' %(str(book)) + ' '
        books = books[0:-1]

        if seg[0] == INSERTION_ID:
            best_path.insert(0, 'Insert %d-%d, %s' % (seg[1], seg[2], books) )

        elif seg[0] == DELETION_ID:
            best_path.insert(0, 'Delete %d-%d' % (seg[1], seg[2]) )

        elif seg[0] == REPLACEMENT_ID:
            best_path.insert(0, 'Replace %d-%d, %s' % (seg[1], seg[2], books) )

        print(best_path)
    return best_path


print_best_path(best_path)
#process_DP_matrix2(s1, s2, dp)
