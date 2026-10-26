print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height,weight):
    print ("value of height is: ",height)
    print ("value of weight is: ",weight)
    bmi=weight/(height*height)
    print("Value of bmi is: ",bmi)
    if bmi <18.5:
        print ("Underweight")
    elif bmi >=18.5 and bmi<25:
        print ("Normal weight")
    else:
        print("Overweight")
    
    return bmi


def display_main_menu():
    print ("display main menu")

def get_user_input():
    print ("user input")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()



bmi_output = calculate_bmi(1.75,70)
print ("BMI output is: ",bmi_output)