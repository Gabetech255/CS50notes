def main():
    userin = input("Input a Sentence: ")
    userin = convert(userin)
    print(userin)

def convert(emojiinput):
    emojiinput = emojiinput.replace(":)", "🙂")
    emojiinput = emojiinput.replace(":(", "🙁")
    return emojiinput

main()