"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
Then from the text file, we create a list of strings form each line in the text file.
Then, we create a dictionary with the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of strings("Enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we 
loop through each word, find the key matching the word and return back the value tied to that word
in our dictionary.

print out the translated sentence to the user.
"""

