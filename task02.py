# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
data = open('equation1.txt', 'r')
string1 = str(data.readline())
data.close()
print(string1)
data2 = open('equation2.txt', 'r')
string2 = str(data2.readline())
data.close()
print(string2)

string1_to_list = string1[0:(string1.find('=') - 1)].split(' + ')
string2_to_list = string2[0:(string2.find('=') - 1)].split(' + ')

print(string1_to_list)
print(string2_to_list)


def create_dict_for_polinomial(str_to_list):
    dict_nom = {}
    for i in range(len(str_to_list)):
        if len(str_to_list[i]) > 8:
            dict_nom[str_to_list[i][(str_to_list[i].rfind(' ')):]] = str_to_list[i][0:str_to_list[i].find(' ')]
        elif len(str_to_list[i]) > 3:
            dict_nom['1'] = str_to_list[i][0:str_to_list[i].find(' ')]
        else:
            dict_nom['0'] = str_to_list[i]
    return dict_nom


string1_dict = create_dict_for_polinomial(string1_to_list)
string2_dict = create_dict_for_polinomial(string2_to_list)
print(string1_dict)
print(string2_dict)

def sum_polinomial(sm_dict1: dict, sm_dict2 : dict):
    sum_polinom = ''
    for key in sm_dict1:
        if sm_dict2.get(key) == None:
            sm_dict2[key] = '0'
    for key in sm_dict2:
        if sm_dict1.get(key) == None:
            sm_dict1[key] = '0'
    for i in sm_dict1:
        if i != '0' and i != '1':
            sum_polinom += f'{str(int(sm_dict1.get(i))+int(sm_dict2.get(i)))} * x **{i} + '
        elif i == '1':
            sum_polinom += f'{str(int(sm_dict1.get(i)) + int(sm_dict2.get(i)))} * x + '
        else:
            sum_polinom += f'{str(int(sm_dict1.get(i)) + int(sm_dict2.get(i)))}  = 0 '
    return sum_polinom

sum_str1_str2 = sum_polinomial(string1_dict, string2_dict )
print(sum_str1_str2)

path = 'equation3.txt'
data = open(path, 'w')
data.write(sum_str1_str2)
data.close()
