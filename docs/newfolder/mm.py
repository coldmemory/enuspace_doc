import glob

files = glob('./*.md')
for file in files:
    with open(file, 'rw') as f:
        f.read()
    print(f)
f.close()