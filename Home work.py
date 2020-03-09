List = []
Fp = open("Book")
Fp.contents = Fp.read()
punct = "?!+=@!,;:()*"
Text= ""

for x in Fp.contents:
    if x not in punct:
        Text= Text + x

Text = Text.split()

for x in Text:
    if x not in List:
        List.append(x)
print("book has", len(List), "unique words")
