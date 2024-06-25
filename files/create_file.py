#!/usr/bin/python3

def main():
    """ Create a file """

    # technique 01
    tabbed_folder = open("myfile.txt", "w")  # Create a file object named tabbed folder
    print("This line goes into the file", file=tabbed_folder)  # Placeline in file object
    print("Second line", file=tabbed_folder)
    tabbed_folder.close() # Don't forget to close your file


    # Technique 02 - auto closing by using "with"
    with open("myfile2.txt", "w") as glossy_folder:
        print("This line goes into the file", file=glossy_folder)
        glossy_folder.write("You can wtire into a file object with the write method\n") 

if __name__ == "__main__":
    main()

