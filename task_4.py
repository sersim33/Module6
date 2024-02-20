def get_cats_info(path):
    
    vocab = []
    with open(path, 'r') as fh:
        lines = fh.readlines()
    for line in lines:
        id,name,age = line.strip().split(",")
        vocab.append({"id": id, 'name': name, 'age': age}) 
    return vocab           




print(get_cats_info("homework4.txt"))