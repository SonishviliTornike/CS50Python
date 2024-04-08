
import inflect

p = inflect.engine()

name_list = []

while True:
    try: 
        get_name = input("Name: ")
        name_list.append(get_name)
    except EOFError and KeyboardInterrupt:
        sorted_list = p.join(name_list)
        print(f"Adieu, adieu, to {sorted_list}.")
        break
