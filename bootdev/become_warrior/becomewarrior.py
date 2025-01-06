# The function was to print out a full name with the warrior behind it, and to take power and add +1 to it
def become_warrior(full_name, power):
    title = f"{full_name} the warrior" #Here i used a f-string 
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()
