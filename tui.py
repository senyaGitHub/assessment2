def welcome(width=100):
    # Calculate the number of dashes
    dashes = '-' * width

    # Print the dashes above
    print(dashes)

    # Calculate spaces for centering the title
    spaces = ((width - len("Records System")) // 2)
    print(" " * int(spaces) + "Records System")

    # Print the dashes below
    print(dashes)
