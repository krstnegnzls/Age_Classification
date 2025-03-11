marks = int(input("Your category based on your age: "))
while True:
    if marks >= 65:
        print("You are a Senior.")
        break
    elif marks >= 20:
        print("You are an Adult.")
        break
    elif marks >= 13:
        print("You are a Teen.")
        break
    elif marks >= 0:
        print("You are a Child.")
        break
    else:
        print("Undefined age. Please try again.")  
        b2 = input("Re-enter your age? (yes/no): ")
        if b2 == "yes":
            marks = int(input("Your category based on your age: ")) 
        elif b2 == "no":
            print("Okay, goodbye.")
            break
        else:
            print("Invalid age number. Please try again.")
            break