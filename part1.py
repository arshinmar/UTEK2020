from part3 import *

# parser function
def parse(input_file_path):
    """
    INPUT:
    ::str:: input_file_path
    OUTPUT:
    ::array:: original_list
    ::array:: desired_list
    """
    original_list = []
    desired_list = []
    try:
        file1 = open(input_file_path, "r+") #open file
    except:
        return [[],[]]

    num_orig = int(file1.readline().split(' ')[1][0:-1]) #get the number of original books
    #print(num_orig) #test

    #iterate over the original books list
    for i in range(0,num_orig,1):
        current = file1.readline()
        if current[-1] == '\n': #if there is newline character, remove it
            original_list += [current[0:len(current)-1]]
        else:
            original_list += [current]

    temp = file1.readline() #get rid of middle line in between

    num_desired = int(file1.readline().split(' ')[1][0:-1]) #get the number of desired books
    #print(num_desired) #test

    #iterate over the desired books list
    for i in range(0,num_desired,1):
        current = file1.readline()
        if current[-1] == '\n': #if there is newline character, remove it
            desired_list += [current[0:len(current)-1]]
        else:
            desired_list += [current]
    file1.close() #close file
    return original_list, desired_list

# generator function
def generate(main_path):
    # remember to call generate with a list of actions like below
    #actions = ['Insert​ ​0-0​, ​"Religion and Mythology, Neil Potts"','Delete​ ​2-3','Insert​ ​3-4​, ​"Foundation, Isaac Asimov"​ ​"Intro to Algorithms, Thomas Cormen"']
    previous_action=0 #set all variables to 0 or empty lists
    final=[]
    temp=[]
    start_index=0
    end_index=0
    previous_action=main_path[0][0] #set previous action to be the first action in the first path

    for i in range(0,len(main_path),1): #this loops through all of the paths with the minimal steps
        if main_path[i][0]!=previous_action: #if the previous action is nt equal to the cur
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
                final+=[temp]
    return print_best_path(final)
