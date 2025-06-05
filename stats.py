def get_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def word_count(filepath):
    count = (len(get_text(filepath).split()))
    return count

def sort_on(dict):
    return(dict)["num"]

def char_count(filepath):

### DECLARATIONS ###

    text = (list(get_text(filepath).lower()))
    list_char_dic = []
    temp_list=[]
    char_dic = {}
    final_list = "" 

### REMOVES NON-ALPHABET ###

    for char in text:
        if char.isalpha():
            temp_list.append(char)
        text = temp_list
            
### DICTIONARY CREATION ###

    for char in text:
        if char in char_dic:
            char_dic[f"{char}"] += 1
        else:
            char_dic[f"{char}"] = 1
        
### LIST CREATION ###

    for char in char_dic:
        num = char_dic[f"{char}"]
        temp_dict={"char" :char,
                   "num": num}
        list_char_dic.append(temp_dict)

### LIST SORT ###

    list_char_dic.sort(reverse=True, key=sort_on)

### LIST TO STRING ###

    for char in list_char_dic:
        str = f"{char["char"]}: {char["num"]}"
        final_list += f"\n{str}"

### OUTPUT STRING ###

    return final_list          
                  
