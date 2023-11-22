# this project talks about boxing day
# boxing day is a day thaat people box up gift to present to friends and family
# this project helps user to give accurate account of gift that has been given out to people
# File Word Counter

# Problem:
# Create a program that counts the occurrences of each word in a text file. Implement functions to:

# * Read the contents of a text file.
# * Count the occurrences of each word.
# * Print the word count.
# Instructions:

# * Create a module named word_counter.py.
# * Implement a function read_file(file_path) that reads the contents of a text file.
# * Implement a function count_words(text) that counts the occurrences of each word in the text.
# * Implement a function print_word_count(word_count) that prints the word count.
# * Create a script named word_counter_script.py to interact with these functions.
while True:
    mmm=[]
    user_input1=input("please input the names of people you wish to give out your gift to: ").strip()
    user_input3=input("please enter the gift you would like to give you would like to give to the listed people above ")
    number=[]
    # to append all gift given to the prefeered choice of people listed above
    number.append(user_input3)

    # to append all  names
    mmm.append(user_input1)

    zzz=number,mmm
    # print(f" this are the list of preffered gift wished to give to the listed people {number}")
    # print(f" this are the list of name inputed {mmm}")
    ccc=mmm[0],number[0]
    # print(ccc)
    dictionary={}
    dictionary[mmm,number]={mmm[0]:number[0]}
    print(dictionary)









