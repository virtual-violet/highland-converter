from markdown2 import markdown
import shutil, os, zipfile, re, argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="Input file. Must be a .highland file.", required=True)
# parser.add_argument('-o', '--output', help="Output file. Will be the name of the folder that is generated. Not required, output folder will just be file name if not passed. End in .html if you want to generate an HTML file as well.", required=False)
parser.add_argument('--html', help="Use this flag if you'd like to generate an HTML file.", action="store_true")
args = parser.parse_args()

highland_file = args.input

filename = os.path.splitext(highland_file)[0]

if os.path.exists(filename):
    overwrite = None
    while overwrite == None:
        user = input('Folder named ' + filename + ' already exists. Overwrite it? [y/n] ')
        if user.upper() == 'Y' or user.upper() == 'YES':
            overwrite = True
            shutil.rmtree(filename)
        elif user.upper() == 'N' or user.upper() == 'NO':
            overwrite = False
            exit()

shutil.copyfile(highland_file, filename + ".zip")

NewZip = zipfile.ZipFile(filename + ".zip")
NewZip.extractall()
os.remove(filename + ".zip")
os.rename(filename + ".textbundle", filename)


if args.html:
    text_in = open(filename + "/text.md", 'r').read()
    text_in = re.sub(r'^> (.*) <$', r'<p align="center">\1</p>', text_in, flags=re.MULTILINE)
    output_file_contents = markdown(text_in, extras=['fenced-code-blocks', 'code-friendly', 'strike', 'tables', 'metadata'])
    output_file = open(filename + '/' + filename + '.html', 'w')
    output_file.write(output_file_contents)
    