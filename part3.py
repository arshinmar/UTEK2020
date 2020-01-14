# Constants
INSERTION_ID = 1
DELETION_ID = 2
REPLACEMENT_ID = 3

def makehash(oa, da):
    """
    INPUT:
    ::array:: oa    #array of original books
    ::array:: da    #array of desired books
    OUTPUT:
    ::array of 3 elements::
        ::array:: ht        #"hash table"
        ::array:: new_oa    #new array with integers
        ::array:: new_da    #new array with integers
    """
    #"hash table" format:
    #[[0, book1], [1, book2], [2, book3], ...]

    ht = [] #"hash table"
    new_oa = []
    new_da = []
    idx = 0 #array idx
    ht_idx = 0 #current ht index
    exists = False #whether or not element already exists

    #go through oa
    for idx in range(0,len(oa),1):
        #check if book already exists in ht
        for i in range(0,len(ht),1):
            if ht[i][1] == oa[idx]:
                new_oa += [ht[i][0]] #add to the new array
                exists = True
                break
        if exists == False: #if book does not already exist in ht
            ht += [[ht_idx, oa[idx]]] #add book to hash table
            new_oa += [ht_idx] #add to the new array
            ht_idx += 1 #increment ht index
        exists = False

    #go through da
    for idx in range(0,len(da),1):
        #check if book already exists in ht
        for i in range(0,len(ht),1):
            if ht[i][1] == da[idx]:
                new_da += [ht[i][0]] #add to the new array
                exists = True
                break
        if exists == False: #if book does not already exist in ht
            ht += [[ht_idx, da[idx]]] #add book to hash table
            new_da += [ht_idx] #add to the new array
            ht_idx += 1 #increment ht index
        exists = False
    return [ht, new_oa, new_da]
#-------------------------------------------------------------------------------
def compute_DP_matrix(s1, s2):
    """
    INPUT
    ::array:: s1
    ::array:: s2
    OUTPUT
    ::2D array:: dp
    """
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

'''def process_DP_matrix(s1, s2, dp):
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
            #actions.insert(0, [REPLACEMENT_ID, i-1, s2[j-1]])
            actions.insert(0, [REPLACEMENT_ID, i, s2[j]])
            i -= 1
            j -= 1

        # check for deletion case
        elif dp[i][j] == dp[i-1][j] + 1:
            actions.insert(0, [DELETION_ID, i, "not applicable"])
            #actions.insert(0, [DELETION_ID, i-1, "not applicable"])
            i -= 1

        # check for insertion case
        elif dp[i][j] == dp[i][j-1] + 1:
            actions.insert(0, [INSERTION_ID, j, s2[j]])
            #actions.insert(0, [INSERTION_ID, j-1, s2[j-1]])
            j -= 1
    print('All paths',actions)
    return actions'''

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

def get_best_path(all_paths):
    #Note: Insert is 1, Remove is 2, Replace is 3
    #Takes an array of arrays of arrays
    # Format [[Path1],[Path2],...]
    # Format of Path1: [[ActionID,Index,Character],[...],[...]]
    previous_action=0 # initialize variables
    cost=0
    best=0
    best_path_id = 0
    for i in range(0,len(all_paths),1):
        for j in all_paths[i]:
            if j != previous_action:
                previous_action = j
                cost+=1
        if i==0:
            best=cost
            best_path_id=i
        else:
            if cost<best:
                best=cost
                best_path_id=i
    return all_paths

def print_best_path(path_segments):
    # path_segments is a list of segments of consective actions of same type
    #INPUT:
    # [[action_id, start_idx, end_idx, books], [...], [...], ...]
    #OUTPUT:
    #best_path is an array of strings
    best_path = []

    for seg in path_segments:
        books = ""
        for i in range(3,len(seg),1):
            #books += '"%s"' %(str(book)) + ' '
            a=str('"')
            b=str('"')
            main=a+seg[i]+b
            books+=main
        #books = books[0:-1]

        if seg[0] == INSERTION_ID:
            best_path.insert(0, 'Insert %d-%d, %s' % (seg[1], seg[2], books) )

        elif seg[0] == DELETION_ID:
            best_path.insert(0, 'Delete %d-%d' % (seg[1], seg[2]) )

        elif seg[0] == REPLACEMENT_ID:
            best_path.insert(0, 'Replace %d-%d, %s' % (seg[1], seg[2], books) )
    return best_path

def generate2(main_path,ht):
    # remember to call generate with a list of actions like below
    #actions = ['Insert​ ​0-0​, ​"Religion and Mythology, Neil Potts"','Delete​ ​2-3','Insert​ ​3-4​, ​"Foundation, Isaac Asimov"​ ​"Intro to Algorithms, Thomas Cormen"']
    # Format of Path1: [[ActionID,Index,Character],[...],[...]]
    '''previous_action=0
    final=[]
    temp=[]
    start_index=0
    end_index=0
    previous_action=main_path[0][0]
    for i in range(0,len(main_path),1):
        if main_path[i][0]!=previous_action:
            temp=[previous_action,start_index,end_index-1]
            for i in range(start_index,end_index,1):
                temp+=[main_path[i][2]]
            final+=[temp]
            start_index=i
            end_index=i+1
        else:
            end_index+=1
            if i==len(main_path)-1:
                temp=[previous_action,start_index,end_index-1]
                for i in range(start_index,end_index,1):
                    temp+=[main_path[i][2]]
                final+=[temp]'''
    #Commented out version above takes in a different kind of array.
    #The following code is if one path is given:
    #Format of Input Here: [[ActionID,Index,Character],[...],[...]]
    previous_action=0
    final=[]
    temp=[]
    start_index=0
    end_index=0
    previous_action=main_path[0][0]
    quick_counter=0 #Replacing length counter
    for i in main_path:
        #Check if this action equals previous action
        if i[0]!=previous_action:
            #If not, create an entry that includes the previous_action, start_index, end_index
            temp=[previous_action,start_index,end_index-1]
            #Add items corresponding to all indexes between start and end indexes
                #This does rely on assuming inserts correspond to consecutive indices.
            for j in range(start_index,end_index,1):
                temp+=[main_path[j][2]]
            #Add this to the final path list.
            final+=[temp]
            #Start index is now current index
            #End index is next index temporarily.
            #Previous action is now current action.
            start_index=i[1]
            end_index=start_index+1
            previous_action=i[0]
        else:
            end_index+=1
        if quick_counter==len(main_path)-1: #Need Replacement due to for loop kind.
            temp=[previous_action,start_index,end_index-1]
            for i in range(start_index,end_index,1):
                temp+=[main_path[i][2]]
            final+=[temp]
        quick_counter+=1
    #Convert back to book names
    for i in range(0,len(final),1):
        for idx in range(3, len(final[i]),1):
            num = final[i][idx]
            final[i][idx] = ht[num][1]
    return print_best_path(final)
