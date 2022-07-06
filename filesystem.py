import os, glob

# Windows Directory
os.chdir("\\Users\\gerar\\Pictures")
for file in glob.glob("*.jpg"):
    print(file)