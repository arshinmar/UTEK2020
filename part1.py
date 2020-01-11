# parser function
def parse(input_file_path):
    """
    INPUT:
    ::str:: input_file_path
    OUTPUT:
    ::array of type str:: [original_list,desired_list]
    """
    original_list = []
    desired_list = []
    try:
        file1 = open(input_file_path, "r+")
    except:
        return [[""],[""]]

    try:
        num_orig = int(file1.readline()[-2]) #num of original books
        #print(num_orig)
        for i in range(0,num_orig,1):
            current = file1.readline()
            original_list += [current[0:len(current)-1]]

        num_desired = int(file1.readline()[-2]) #num of desired books
        #print(num_desired)
        for i in range(0,num_desired,1):
            current = file1.readline()
            desired_list += [current[0:len(current)-1]]
    except:
        file1.close()
        return [[""],[""]]
    file1.close()
    return [original_list,desired_list]

# generator function
def generate(actions):
    # remember to call generate with a list of actions like below
    #actions = ['Insert​ ​0-0​, ​"Religion and Mythology, Neil Potts"','Delete​ ​2-3','Insert​ ​3-4​, ​"Foundation, Isaac Asimov"​ ​"Intro to Algorithms, Thomas Cormen"']

    with open("something.out" , "w") as output_file:
        for action in actions:
            output_file.write(action + "\n")

    return True
