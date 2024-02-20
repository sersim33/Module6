def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for employee in employee_list:
        fh.write('employee' + '\n') 
    print(fh.read())    


    fh.close