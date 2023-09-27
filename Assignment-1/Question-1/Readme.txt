Input Structure-->
The program expects the following input structure:

1. The first line contains an integer K, which represents the number of words in the dictionary.
2. The second line contains two space-separated words: the start word and the end word. Note that the end word must belong to the dictionary.
3. The next K lines contain different words in the dictionary.


Output Structure -->
The program will output the smallest order of words that converts the start word to the end word, separated by spaces. If no valid path is found, it will display "No path found" for both BFS and IDDFS.


How to Run?
1. Ensure you have Python 3 installed on your system.
2. Download the Python script (Q1.py) to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the following command: python Q1.py

Sample Input/Output:
INPUT: 
5
sky sun
spy
soy
son
sun
sum

OUTPUT: 
BFS Result:  sky soy son sun
IDDFS Result:  sky soy son sun
