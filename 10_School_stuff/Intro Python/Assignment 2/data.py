def read_file(filename):
    with open(filename, mode='r', encoding='utf-8') as fh:
        return fh.read().splitlines()

def parse_csv_lines(lines):
    return [line.split(',') for line in lines]

def parse_delimited_lines(lines, delimiter):
    return [line.split(delimiter) for line in lines]

def age_difference(lines): 
    age_diff = []
    for line in lines:
        tmp = line[0].split(';')
        age_diff.append((round(float(tmp[1])-float(tmp[len(tmp)-1]), 1)))
    return age_diff

def find_unisex_names(male_names, female_names):
    male = read_file(male_names)
    female = read_file(female_names)
    return set(male).intersection(female)

def build_name_dataset(female_names, male_names, unisex_names):
    with open('all_names.csv', mode='w', encoding='utf-8') as all_names:
        for m_name in male_names:
            if m_name not in unisex_names:
                all_names.write(m_name + ",M\n")
        for f_name in female_names:
            if f_name not in unisex_names:
                all_names.write(f_name + ",F\n")
        for u_name in unisex_names:
            all_names.write(u_name + ",U\n")

def write_sorted_names(names):
    alphabet = set()
    for name in names:
        if name[0] in alphabet:
            with open(f'{name[0]}.csv', mode='a', encoding='utf-8') as f:
                f.write(name + '\n')
        else:
            with open(f'{name[0]}.csv', mode='w', encoding='utf-8') as f:
                f.write(name + '\n')
            alphabet.add(name[0])
    print("Done")


def main():
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

if __name__ == "__main__":
    main()
