import sys
from pyfiglet import Figlet

figlet = Figlet()

# No arguments → random font
if len(sys.argv) == 1:
    font = None

# With arguments
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

# Invalid number of arguments
else:
    sys.exit("Invalid usage")

# Set font if provided
if font:
    figlet.setFont(font=font)

# Get input
text = input("Input: ")

# Output result
print("Output:")
print(figlet.renderText(text))
