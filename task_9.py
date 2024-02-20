def get_credentials_users(path):
    
    with open(path, 'rb') as file:
        lines = file.readlines()
        decoded_lines = [line.decode('utf-8').strip() for line in lines]
        

    return decoded_lines
