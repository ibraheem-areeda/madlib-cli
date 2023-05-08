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
        text = str(temp_read.read())
        return text
    
def parse_template(row_text):
    print(type(row_text))
    stripped = re.sub("{\w*}", "{}" , row_text )
    parts = tuple(re.findall("\{(.*?)\}", row_text))
    return stripped , parts

def merge():
    pass


if __name__ == '__main__':
    welcome ()