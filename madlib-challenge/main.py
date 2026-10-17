def madlib(name, verb, quantity, item, new_item, is_happy):
    name = name.title()
    title = f"The Story Of {name}".title()
    print(title)
    print("=" * len(title))
    print(f"There once was a man named {name}.")
    print(
        f"Every day he would {verb} with his {quantity} {item}{'' if quantity == 1 else 's'}"
    )
    vowel = "aeiou"
    if is_happy:
        print(
            f"But then, he found {'an' if new_item[0] in vowel else 'a'} {new_item} and everything changed!"
        )
    else:
        print(
            f"But then, {'an' if new_item[0] in vowel else 'a'} {new_item} took over his life and he couldn't {verb} again!"
        )

    print("The end.")


def main():
    name = input("A Name: ").strip()
    verb = input("A Verb: ").strip().lower()
    quantity = input("A Number: ").strip()
    if not quantity.isdigit():
        return print("Must input a valid number.")
    quantity = int(quantity)
    if quantity == 0:
        print("Must input a number greater than 0.")
        return
    item = input("An Item: ").strip().lower()
    new_item = input("A New Item: ").strip().lower()

    is_happy = input("Are You Happy?(y/n): ").strip().lower()
    if is_happy != "y" and is_happy != "n":
        return print("Must input either y or n.")
    is_happy = is_happy == "y"

    madlib(name, verb, quantity, item, new_item, is_happy)


main()
