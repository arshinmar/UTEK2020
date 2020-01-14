# UTEK2020
Main repository for our submission to the UTEK 2020 Programming Competition. The submission received 3rd place in the competition.

### Team
Arsh Kadakia, Sean Wu, Ben Natra, Matthew Leung

## Problem
### Main Problem: Arrange Books in a Library
In a library, given the current arrangement of books, and a new desired arrangement, generate an optimal set of moves to rearrange the shelves. Allowed moves (each of equal cost) are insert, delete, and replace.

### Parts of the Competition
The competition consisted of three parts, which could be found in the PDF file in this repository. The second part of the competition is to generate an optimal set of moves to rearrange strings (e.g. rearrange "Sunday" into "Saturday"). The third part of the competition is to generate an optimal set of moves to rearrange library shelves (main problem).


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

### ```dp``` Matrix
Given a string ```s``` of length m, which we want to rearrange into a string ```t``` of length n, a ```dp``` matrix of size (m+1) x (n+1) would be needed. ```s``` would be placed along the column, and ```t``` would be placed along the row (see example below). Now let's say we have an index ```i``` that iterates over the rows of ```dp```, and an index ```j``` that iterates over the columns of ```dp```. Every entry ```dp[i][j]``` in ```dp``` contains the minimum number of moves required to change the first ```i``` characters of ```s``` into the first ```j``` characters of ```t```. We would start at the top left corner of the matrix, and fill it in the bottom right direction, until the entire matrix is filled. The most bottom right entry of ```dp``` would contain the minimum number of moves required to change ```s``` into ```t```.

Intuitively, as we fill ```dp```, if we go from left to right, it is an insertion operation. If we go from top to bottom, it is a deletion operation. Finally if we go diagonally from an entry top left, it is a replacement operation; this is unless the ```i```th element of ```s``` is equal to the ```j```th element of ```t```, in which no operation would have been done. After filling the matrix, we can simply backtrack to determine the most optimal set of moves needed to change ```s``` into ```t```.

### Identifier
When the initial input file ```<input_file>.in``` was parsed, the names of the books were placed in a list of lists with a unique integer key (identifier) mapped to each book for quick access. Our algorithm needed to compare whether or not two books were equal, and since comparisons between integers are faster than comparisons between strings, this data structure was used. Format of the data structure:
```[[0, book1], [1, book2], [2, book3], ...]```

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

### Future Improvements

We noticed that not all elements of the ```dp``` matrix have to be computed. Some entries, near the top right corner or bottom left corner of the matrix would give sets of moves that are not the most optimal. In these areas of the matrix, there would be a larger set of moves, because more insertions/deletions are performed rather than replacements.

## Project Structure
The competition was broken up into three parts. Each part has its own designated python file for relevant functions and its own main file to execute the code. The test input files are also provided in this repository along with our outputs.

```
├── An_Analysis_Post-Mortem.pdf
├── README.md
├── main1.py
├── main2.py
├── main3.py
├── part1.py
├── part2-input/
├── part2-output/
├── part2.py
├── part3-input/
├── part3.py
└── utek2020_programming_package.pdf
```
