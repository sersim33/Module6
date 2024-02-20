
def save_credentials_users(path, users_info):
    res = ""   
    for key,value in users_info.items():
        string = key + ":" + value + "\n"
        res+=string

    with open(path,"w") as fh:
        fh.write(res)