import os


def _get_file_content():
    while True:
        file_path = input("Please provide path to the file you'd like to examine: ")
        if not os.path.exists(file_path):
            print("The path doesn't exist! Please input correct path!")
            continue
        # checking if the extension is correct
        file_path_tuple = os.path.splitext(file_path)
        if not file_path_tuple[1] == ".txt":
            print("Wrong extension of the file. The file's extension must be '.txt'! Please input the path again!")
            continue
        # checking if file is empty - if size == 0 - it's empty
        is_file_empty = os.path.getsize(file_path)
        if is_file_empty == 0:
            print("The file is empty! Please input the path once again!")
            continue
        break

    with open(file_path) as file:
        return file.read()


def _get_text():
    print("Selected option: text input.")
    print("Please note that it's a multiline input.")
    print("If you wish to finish input please type '$' and press enter.")
    print("Input your text here: ")
    txt = ""

    while True:
        txt += input() + "\n"
        if "$" in txt:
            break

    character_index = txt.find("$")
    return txt[:character_index]


def get_content():
    text_input_or_path = input("If you wish to input the text to analyze on your own, please input 'txt',\
 if you wish to analyze text from a file please input 'file' ")

    if text_input_or_path == "file":
        return _get_file_content()
    else:
        return _get_text()


