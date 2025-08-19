from collections import deque
from datetime import datetime
data = []
f = open("wordsEn.txt")
data = (f.readlines())
f.close()
for i in range(len(data)):
    data[i] = data[i].strip("\n")


def main():
    start_word = input("Enter start word: ")
    end_word = input("Enter end word: ")
    # Check if Start word or End word is in the dictionary
    if start_word not in data or end_word not in data:
        print("Start word/End word is not in the words dictionary")
        return None
    # Implement the logic to find the chain
    start_time = datetime.now()
    print("Start time:", start_time)
    print("---------------")
    queue = deque([start_word])
    tracker = {start_word: None}
    while queue:
        current_word = queue.popleft()
        #Filter a list of neighbors of the current word
        neighbors = filter(lambda x: x[:2] == current_word[-2:] and len(x) > 2, data)
        for neighbor in neighbors:
            #Check if neighbor is tracked or not
            if neighbor not in tracker:
                tracker[neighbor] = current_word
                queue.append(neighbor)
        #Found a chain
        if end_word in tracker:
            break
    #Rebuild the chain
    if end_word in tracker:
        chain = []
        current_word = end_word
        while current_word is not None:
            chain.append(current_word)
            current_word = tracker[current_word]
        chain.reverse
        print("The shortest chain is:")
        for word in chain:
            print(word)
    else:
        print("No chain found!")
    end_time = datetime.now()
    print("---------------")
    print("End time:", end_time)
    print("Duration:", end_time - start_time)

if __name__ == '__main__':
    main()