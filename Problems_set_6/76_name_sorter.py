import csv

def main():
    count = count_lines()
    sorted_list = write_new_file(read_file(), count)
    for element in sorted_list:
        new_element = ", ".join(element)
        print(new_element)

def count_lines():
    with open("76_names_sorter.csv", 'r') as file:
        amount_names = file.readlines()      
        return amount_names

def read_file():
    new_list = []

    with open("76_names_sorter.csv", 'r') as file:
        reader = csv.reader(file)      
        for element in reader:
            new_list.append(element)

        return sorted(new_list)
    

def write_new_file(sorted_list, count):
    sorted_list.insert(0,[f"Total of {len(count)} names"])
    sorted_list.insert(1,["-----------------"])
    with open("76_sorted_names.csv", 'w') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(sorted_list)
        return sorted_list


if __name__ == "__main__":
    main()


