def sanitize_file(source, output):

    with open(source, 'r') as fh:
        lines = fh.readlines()
    res = ""     
    for line in lines:
        modified_string = ''.join([i for i in line if not i.isdigit()])
        res += modified_string
    print(res)

    with open(output,"w") as fh:
        fh.write(res)

          

sanitize_file("homework4.txt", "homework5.txt")

