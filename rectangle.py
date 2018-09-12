def get_input (prompt, accepted):
    while True:
        value = input (prompt).lower()

        if value in accepted:
            return value
        else:
            print ("that is not a recognised answer, must be one of ", accepted)

print ("i can do geometry on a rectangle")
length = int(input ("what is the length of your rectangle?"))
width = int(input  ("what is the width of your rectangle?"))
mode = get_input ("do you want to know the area or perimeter?", ["area","perimeter"])
if mode == "area":
    area = length * width
    print ("area:", area)
elif mode == "perimeter":
    perimeter = (length * 2) + (width * 2)
    print ("perimeter:", perimeter)