

def write_employees_to_file(employee_list, path):

    fh = open(path,"w")
    for sub_employee in employee_list:
        
        for employee in  sub_employee:
            print(employee)
            fh.write(employee + '\n')
    fh.close()



l = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(l,'homework6_1.txt')

