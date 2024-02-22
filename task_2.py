
def read_employees_from_file(path): 

    fh = open(path,"w+")
    lines = fh.readlines()
    res = []
    print(lines)
    for line in lines:
        res.append(line.strip()) 

    print(res)
    
    fh.close()

    return res





read_employees_from_file('homework1.txt')