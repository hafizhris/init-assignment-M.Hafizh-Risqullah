import math

def Various_Triangle (side_1, side_2, side_3):
    """

    :param side_1: First length of the Triangle side
    :param side_2: Second length of the Triangle side
    :param side_3: Third length of the Triangle side
    :return: str = Kinds of Triangle based on the input
    """
    if side_1 == side_2 == side_3 :
        return "This is Equaliteral Triangle"
    elif (side_1 == side_2) or (side_1 == side_3) or (side_2 == side_3) :
        return "This is Isosceles Triangle"
    elif (side_1 != side_2 != side_3) :
        return "This is Arbitrary Triangle"
    else:
        return "Invalid Input please insert other variable"

while True:
    try :
        side_1 = int(input("Enter the first length of side 1 :"))
        side_2 = int(input("Enter the scceond length of side 2 :"))
        side_3 = int(input("Enter the third length of side 3 :"))

        print(Various_Triangle(side_1, side_2, side_3))
        break
    except ValueError:
        print("Invalid Input, please enter a right numerical variable")
