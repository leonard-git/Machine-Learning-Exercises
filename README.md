# Machine Learning Exercises
---

## Exercise 8: Word Chain Finder

**Description:**  
Write a program that lets the user input two English words. The program should find and print the shortest possible chain of words connecting the two, following these rules:

- Each word in the chain must have **at least 3 letters**.
- The **first word** in the chain is the first user input; the **last word** is the second user input.
- For every pair of consecutive words in the chain, the **last two letters** of the previous word must be the **same as the first two letters** of the next word.
- All words used must be from the file `wordsEn.txt`.
- If there are multiple shortest chains, returning any one of them is sufficient.

**Example:**

Enter start word: paper
Enter end word: pen
The shortest chain is:
pen
radarscope
era
paper