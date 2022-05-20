import os

def get_mail_msg(fname, to, link):
    txt = get_txt_from_file(fname)
    custom_txt = txt.replace('@username', to)
    custom_txt = custom_txt.replace('@link', link)
    return custom_txt
    
def get_txt_from_file(fname):
    dir = os.path.dirname(__file__)
    file_path = os.path.join(dir, 'files', fname)   #full path to text.
    data_file = open(file_path , 'r')
    data = data_file.read()
    return data
