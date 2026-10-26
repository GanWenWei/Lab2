import statistics


def get_user_input():
    user_input=input ("Enter temperature values: ")
    float_list=[float(x) for x in user_input.split(",")]
    return float_list

def calc_average(float_list):
    average = sum(float_list)/len(float_list)
    return average

def find_min_max(float_list):
    maximum=max(float_list)
    minimum=min(float_list)
    print ("Min is ", minimum)
    print ("Max is ", maximum)
    return [min(float_list), max(float_list)]

def calc_median_temperature(float_list):
    median =statistics.median(float_list)
    return median
    

def sort_temperature (float_list):
    return sorted(float_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

    

if __name__ == "__main__":
    display_main_menu()
    float_list = get_user_input()
    print("Average =", calc_average(float_list))

    print("Min and Max =", find_min_max(float_list))

    print("Median =", calc_median_temperature(float_list))

    print("Sorted =", sort_temperature(float_list))

