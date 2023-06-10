def read_file(filename):
    # returns a list of strings
    with open(filename, mode='r', encoding='utf-8') as fh:
        return fh.readlines()

def parse_csv_lines(lines):
    # returns a list of lists
    return [line.split(',') for line in lines]

def parse_delimited_lines(lines, delimiter):
    return [line.split(delimiter) for line in lines]

def age_difference(lines):
    age_diff = []
    for line in lines:
        tmp = line[0].split(';')
        age_diff.append((tmp[0], round(float(tmp[1])-float(tmp[len(tmp)-1]), 1)))
    return age_diff

def find_unisex_names(male_names, female_names):
    male = read_file(male_names)
    female = read_file(female_names)

    # uni_sex = set()
    # for string in set(male).intersection(female):
    #     uni_sex.add(string.rstrip('\n'))
    # return uni_sex
    return set(male).intersection(female)

def build_name_dataset(female_names, male_names, unisex_names):
    with open('all_names.csv', mode='w', encoding='utf-8') as all_names:
        for m_name in male_names:
            if m_name not in unisex_names:
                all_names.write(m_name.rstrip('\n') + ",M\n")
        for f_name in female_names:
            if f_name not in unisex_names:
                all_names.write(f_name.rstrip('\n') + ",F\n")
        for u_name in unisex_names:
            all_names.write(u_name.rstrip('\n') + ",U\n")

def write_sorted_names(names):
    alphabet = []
    for name in names:
        if name[0] in alphabet:
            with open(f'{name[0]}.csv', mode='a', encoding='utf-8') as f:
                f.write(name)
        else:
            with open(f'{name[0]}.csv', mode='w', encoding='utf-8') as f:
                f.write(name)
            alphabet.append(name[0])
    print("Done")


# print(read_file('municipalities-2005-2019.csv'))

dataList = read_file('municipalities-2005-2019.csv')

# print(parse_csv_lines(dataList))

parsedList = parse_csv_lines(dataList)

# print(age_difference(parsedList))

age_difference(parsedList)

unisex_names = find_unisex_names('male_names.csv', 'female_names.csv')

# print(find_unisex_names('male_names.csv', 'female_names.csv'))

male_names = read_file('male_names.csv')
female_names = read_file('female_names.csv')

# print(male_names)

build_name_dataset(female_names, male_names, unisex_names)

all_names = read_file('all_names.csv')

write_sorted_names(all_names)


