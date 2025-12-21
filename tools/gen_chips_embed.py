import os
import glob


#navigate to config/chips folder
os.chdir(".")
os.chdir(os.getcwd()+"\\config\\chips")

#search all files
content = []
c_file = "#include " + '"' + "chips_embed.h" + '"' + "\n\n\nconst char* chips_str ="
h_file = "#ifndef __CHIPS_EMBED_H" + "\n#define __CHIPS_EMBED_H\n" + "extern const char* chips_str;\n"

new_file_str = "-*-*-*-"

chips_cnt = 0
for f in glob.glob("*.chip"):
    chips_cnt += 1
    file = open(f, 'r')
    ls = file.read().splitlines()
    file.close()
    for l in ls:
        content.append("\n" + '"' + l + '"')
        content.append("\n" + '"'+ '\\n' + '"') # assume as new line
    content.append("\n" + '"' + new_file_str + '"') # assume as new file
    content.append("\n" + '"'+ '\\n' + '"') # assume as new line

content.append(';')

for s in content:
    c_file += s


h_file += "#define CHIPS_CNT\t" + str(chips_cnt) + "\n"
h_file += "#define NEW_FILE_STR\t" + '"' + new_file_str + '\\n' + '"' + "\n"
h_file += "#endif\n"

# navigate to source folder
os.chdir("..")
os.chdir("..")
os.chdir(os.getcwd()+"\\src\\stlink-lib")
fc = open("chips_embed.c", 'w')
fc.write(c_file)
fc.close()

fh = open("chips_embed.h", 'w')
fh.write(h_file)
fh.close()



print(os.getcwd())