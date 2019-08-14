import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
speech = ''.join(obama)
print(speech)

for line in obama:
  if re.findall(r"^.*the\s.*$", line):
    print(line)

# TODO: print lines that contain a word of any length starting with s and ending with e

for line in obama:
  if re.findall(r"^.*\ss[a-z]*e\s.*$", line):
    print(line)

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY

date = r"Please enter a date in the format MM.DD.YY: "
date1 = r"Please enter a date in the format 01.01.99: "

def date_printer(raw):
  md = re.findall(r"(\w\w)\.", raw)
  y = re.findall(r"(\w\w)\:", raw)
  print('\n Month: %s \n Day: %s \n Year: %s' % (md[0], md[1], y[0]))
  
date_printer(date)
date_printer(date1)
