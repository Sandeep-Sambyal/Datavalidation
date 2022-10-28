"""Utils file include all common functions."""
import os
import traceback
from .settings import BASE_DIR

def handle_uploaded_file(f):
    """Stores file submitted  in local for processing."""
    print(f"Creating file {f.name}")
    with open( os.path.join(BASE_DIR, "fileuploaded", f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def process(path1, path2):
    """Prcoesses logic of the code."""
    try:
        file_1 = open(os.path.join(BASE_DIR, "fileuploaded", path1.name),'r')
        file_2 = open(os.path.join(BASE_DIR, "fileuploaded", path2.name),'r')

        file_obj = open("op.txt", "a")
        file_obj.truncate(0)
        file_obj.write(f"Comparing files {path1} and {path2}. \n")
        file_1_line = file_1.readline()
        file_2_line = file_2.readline()
        line_no = 1

        with open(os.path.join(BASE_DIR, "fileuploaded", path1.name)) as file1:
            with open(os.path.join(BASE_DIR, "fileuploaded", path2.name)) as file2:
                same = set(file1).intersection(file2)
        file_obj.write("Common Lines in Both Files \n")
        for line in same:
            #Remove existing new line and add manually after every line to handle 
            #last line scenario.
            line = line.replace('\n','') if '\n' in line else line
            file_obj.write(f"{line}\n")
        file_obj.write('\n')
        file_obj.write("Difference Lines in Both Files: \n")
        while file_1_line != '' or file_2_line != '':
            # Removing whitespaces
            file_1_line = file_1_line.rstrip()
            file_2_line = file_2_line.rstrip()

            # Compare the lines from both file
            if file_1_line != file_2_line:

                # otherwise output the line on file1 and use @ sign
                if file_1_line == '':
                    file_obj.write(f"@ Line - {line_no}  {file_1_line} \n")
                    # print("@", "Line-%d" % line_no, file_1_line)
                else:
                    file_obj.write(f"@- Line - {line_no}  {file_1_line} \n")
                    # print("@-", "Line-%d" % line_no, file_1_line)

                # otherwise output the line on file2 and use # sign
                if file_2_line == '':
                    file_obj.write(f"# Line - {line_no}  {file_2_line} \n")
                    # print("#", "Line-%d" % line_no, file_2_line)
                else:
                    file_obj.write(f"#+ Line - {line_no}  {file_2_line} \n")
                    # print("#+", "Line-%d" % line_no, file_2_line)

            # Read the next line from the file
            file_1_line = file_1.readline()
            file_2_line = file_2.readline()

            line_no += 1

        file_1.close()
        file_2.close()
        file_obj.close()
        #"Removing files from project directory"
        os.remove(os.path.join(BASE_DIR, "fileuploaded", path1.name))
        os.remove(os.path.join(BASE_DIR, "fileuploaded", path2.name))

    except Exception as exc:
        print("Exception - ",exc)
        print(traceback.format_exc())
