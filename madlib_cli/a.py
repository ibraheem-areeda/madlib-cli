import re 
def parse_template(row_text):
    print(type(row_text))
    stripped = re.sub("{\w*}", "{}" , row_text )
    parts = tuple(re.findall("\{(.*?)\}", row_text))
    return stripped , parts


print( parse_template("It was a {Adjective} and {Adjective} {Noun}."))