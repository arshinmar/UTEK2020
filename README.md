# UTEK2020
Main repository for UTEK 2020 Competition.

### Team
Arsh Kadakia, Sean Wu, Ben Natra, Matthew Leung

## Problem
### Main Problem: Arrange Books in a Library
In a library, given the current arrangement of books, and a new desired arrangement, generate an optimal set of moves to rearrange the shelves. Allowed moves (each of equal cost) are insert, delete, and replace.

### Parts
The second part of the competition is to generate an optimal set of moves to rearrange strings (e.g. rearrange "Sunday" into "Saturday"). The third part of the competition is to generate an optimal set of moves to rearrange library shelves (main problem).


## Build/Run Instructions
Download all the necessary files, and type into command line:
```python <script_name>.py <input_file>.in```


```<input_file>.in``` is the path to the input file (input files are those that have a ```.in``` extension; see the repository for examples for each part). To generate an optimal set of moves to rearrange strings, use ```main2.py``` as ```<script_name>.py``` To generate an optimal set of moves to rearrange shelves in a library, use ```main3.py``` as   ```<script_name>.py```.

## Our Model
### Algorithm
- Used the **Wagner-Fischer Algorithm** to compute the costs for each set of moves to rearrange a string/library-shelf.
- Backtracked to determine the process (set of moves) corresponding to each cost.
- Noted each process in a separate list.

### Algorithm Steps
1. Given two strings/library-shelves of size m and n, compute the minimum-cost matrix of size (m+1) x (n+1), called ```dp```, filled with number of moves.
2. Backtrack and note down process to get to zero cost (top left corner of matrix).
3. Track all of the potential paths.
4. Determine the optimal path by measuring which path has the most number of similar consecutive moves (consecutive inserts, deletes, replaces).
5. Convert to printable syntax and output to file.

### Hash Table
When the initial input file ```<input_file>.in``` was parsed, the names of the books were placed in a hash table for quick access. Each book was assigned an integer key. Our algorithm needed to compare whether or not two books were equal, and since comparisons between integers are faster than comparisons between strings, a hash table was used.

### Example
To rearrange the string ```kitten``` into ```sitting```, our model gives a corresponding ```dp``` matrix of:
```
      s  i  t  t  i  n  g
  [0, 1, 2, 3, 4, 5, 6, 7]
k [1, 1, 2, 3, 4, 5, 6, 7]
i [2, 2, 1, 2, 3, 4, 5, 6]
t [3, 3, 2, 1, 2, 3, 4, 5]
t [4, 4, 3, 2, 1, 2, 3, 4]
e [5, 5, 4, 3, 2, 2, 3, 4]
n [6, 6, 5, 4, 3, 3, 2, 3]
```

After determining the most optimal path, the output is:
```
Replace 0, ‘s’
Replace 4, ‘i’
Insert 6, ‘g’
```
