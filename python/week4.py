def main():
    # Ask the user for the filename
    filename = input("Enter the file name to read: ")
    
    try:
        # try to open and read the file
        with open(filename) as file:
            content = file.read();
            print(content)
            
        # example modification - convert ext to uppercase
        modified_content = content.upper()
        
        # create a new file and write modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
            
        print(f"File modified and saved as '{new_filename}'")
        
    except FileNotFoundError:
        print("Error: The file does not exist")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        

if __name__ == "__main__":
    main()