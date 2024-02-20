data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    res = ""   
    for dict_info in source:
        name = dict_info.get('name')
        specialty = dict_info.get('specialty')
        math = dict_info.get('math')
        lang = dict_info.get('lang')
        eng = dict_info.get('eng')

        string = name + "," +  str(specialty) + "," + str(math) + "," + str(lang) + ',' + str(eng) + "\n"
        res+=string

    with open(output,"w") as fh:
        fh.write(res)





save_applicant_data(data,"output.txt")



