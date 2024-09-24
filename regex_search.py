import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"ain"
matches = re.findall(pattern, text)

for match in matches:
    print(match)
