def read_write(infile,outfile):
    #infile represents input file
    #outfile represents output file
    try:#error handling
        with open(infile,"r") as file:#reads the file
            data=file.read()
            modified=' '.join(sorted(data))#sorts characters
        with open(outfile,"w") as out_file:#writes to the new file
            out_file.write(modified)
        return f"Content from '{infile}' was successfully sorted and written to '{outfile}'."
    except FileNotFoundError:#returns error if file is missing
        return f"The file does not exist"
    except PermissionError:#returns error if permission denied
        return f"Permission denied for {infile} or {outfile}"
    
infile="test.txt"
outfile="out.txt"
print(read_write(infile,outfile))


