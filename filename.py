def file_name():
    name=input("Enter your file name:")
    try:
        with open(name,"r") as file:
            data=file.read()
            print("Contents of the file are:")
            print(data)
    except FileNotFoundError:
        return f"File is missing"
    except PermissionError:
        return f"Permission to read the {name} file has been denied"
file_name()