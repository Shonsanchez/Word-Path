import queue as q
import os

def convertTexttoSet(filename):
    dictionary = set()
    file = open(filename, "r")
    for line in file:
        dictionary.add(line.strip())
    return dictionary

def getChildren(word,visited,dictionary):
    words = []
    #for each character iterate that character to a to z
    for char_index in range(len(word)):
        # store the ascii value of the ch at char_index
        ascii_value = ord(word[char_index])
        current_ascii_value = ascii_value+1
        if(current_ascii_value > 122):
            current_ascii_value = 97
        while(current_ascii_value != ascii_value):
            new_word = create_word(word, char_index, current_ascii_value)
            if new_word in dictionary and new_word not in visited:
                visited.add(new_word)
                words.append(new_word)
            current_ascii_value+=1
            if(current_ascii_value > 122):
                current_ascii_value = 97
        # for each word not in visted add it to words and include it
        # in the visted list
    return words

def create_word(word, index, ascii_value):
    return  word[:index] + chr(ascii_value) + word[index+1:]

def solution(source, target,dictionary,visited):
    #create a list for the path
    if source == target:
        return [source]
    if len(source) != len(target):
        return None
    queue = q.Queue()
    queue.put([source])
    while(not queue.empty()):
        count = queue.qsize()
        for i in range(count):
            # add all of it's children into the queue
            current_stack = queue.get()
            current_word = current_stack[-1]
            for word in getChildren(current_word,visited,dictionary):
                new_stack = current_stack.copy()
                new_stack.append(word)
                if word == target:
                    return new_stack
                queue.put(new_stack)
    return None

def print_solution(stack,source,destination):
    if stack:
        result = "The path from " + source + " to " + destination + " is "
        for element in stack:
            result += element +" => " 
        result = result[:-4]
    else:
        result ="There is no path from " + source + " to " + destination
    print(result + ".")

def prompt_user_for_path():
    print("Enter the path to file: ", end='')
    path = input()
    while(not os.path.exists(path)):
        print(path, "does not exist. Please enter a valid path: ",  end="")
        path = input()
    return path

def main():
    print("Welcome to inplace word conversion. Where this program attempts to convert one word to another word by altering one character at a time.")
    print("In order to get started please provided the path to the file with the list of valid words.")
    print("The words in the file must be separated by a new line character.")
    path_to_file = prompt_user_for_path()
    dictionary = convertTexttoSet(path_to_file)
    # create while loop for multiple words
    continue_ = True
    while(continue_):
        # dictionary = convertTexttoSet("exampleWords.txt")
        print("Provide the word with which to begin: ", end ='')
        word1 = input()
        # word1 = "small"
        print("Provide the word with which to end: ", end ='')
        word2 = input()
        # word2 = "short"
        path = solution(word1,word2,dictionary,set())
        print_solution(path,word1,word2)
        print("To exit now type \"exit\" or hit ENTER to continue: ", end ="")
        continue_ = (input() != "exit")

if __name__ == "__main__":
    main()

# A good one to try is "great" to "hater".