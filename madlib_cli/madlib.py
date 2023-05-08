def read_template(dir):
    
    with open (dir, "r") as temp_read:
        text = str(temp_read.read())
        return text
    
