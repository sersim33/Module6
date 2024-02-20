def add_employee_to_file(record, path):

    fh = open(path,"a")
    fh.write(record + '\n')
    fh.close()



add_item = "Drake Mikelsson,19"
add_employee_to_file(add_item, path="homework6_1.txt")

    

