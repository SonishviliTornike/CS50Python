def main():
    while True:           
        fraction = input("Fraction: ")
        if convert(fraction) == True or convert(fraction) == 0:
                if int(gauge(convert(fraction))) >= 99:
                    print("F")
                    break
                elif int(gauge(convert(fraction))) <= 1:
                    print("E")
                    break
                else:                    
                    print(f"{gauge(convert(fraction))}%")
                    break
        else:
            continue

def convert(fraction):
    try:
        fraction = fraction.split("/")
        calculate_fraction = 100 / int(fraction[1]) * int(fraction[0])
        percentage = round(calculate_fraction)
        return percentage
    except ValueError:
        return 
    except ZeroDivisionError:
        return      
    except IndexError:
        return 


def gauge(percentage):
    return f"{percentage}"


if __name__ == "__main__":
    main()