import re
def welcome ():
    print (
        """
        *****************************
        ***** welcome to Madlib *****
        *****                   *****
        *****************************

        lets play the Mad Lib game!
        To get started, I need you to give me a list of words that I can use to fill in the blanks in a story.
        you will give me one word at a time, based on what type of word I ask for, (e.g. noun, adjective, verb, etc.).
        Once I have all the words, I will use them to fill in the blanks in a story,
        and we can read it back together to see what funny
        or silly story we have created. 
        Lets get started!
        """
        )
    

def read_template(dir):
    with open (dir, "r") as temp_read:
        row_text = str(temp_read.read())
        return row_text
    
def parse_template(row_text):
    stripped = re.sub("\{(.*?)\}", "{}" , row_text )
    parts = tuple(re.findall("\{(.*?)\}", row_text))
    return stripped , parts

def merge(stripped_txt,input_arr):
    appnd = stripped_txt.format(*input_arr)
    return appnd

def write_txt_file(user_answer):
    with open("result.txt" , "a") as result_file:
        print(user_answer)
        result_file.write(user_answer)

def user_input (arr):
    user_input=[]
    n = len(arr)
    for word in arr:
        n=n-1
        user_input.append(input(f" {n} remaning words, please enter {word} : ") )
        
    return user_input






if __name__ == '__main__':

    dir1 ="assets/short_text.txt"
    dir2 ="assets/long_text.txt"

    row_text = read_template(dir1)

    print(row_text)

    [stripped ,parts] = parse_template(row_text)

    print(list(parts))

    welcome ()

    user_input_words= user_input (list(parts))

    user_output = str(f"""
Your funny story --> {merge(stripped,user_input_words)}
    """)

    write_txt_file((user_output))






