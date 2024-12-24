def AlphaOrdered(text):
    alpha = "BCDFGHJKLMNPQRSTVWXYZ"

    final = "piano: (tempo 100) "
    notes = ["c", "d", "e", "f", "g", "a", "b"]
    vowelnotes = ["d-", "e-", "g-", "a-", "b-"]
    vowels = ["A", "E", "I", "O", "U"]

    for letter in text:
        if letter != " ":
            if letter in vowels:
                note = vowelnotes[vowels.index(letter)]
            elif letter in alpha:
                note = str(notes[(ord(letter) - 64) % 7])
        else:
            note = "r" # rest for spaces

        final += note + " "

    return final

def CommonOrdered(text):
    # Most common letters separated by fifths starting on F
    final = "piano: (tempo 100) "
    common = "RTNSLCDPMHGBFYWKVXZJQ"
    notes = ["f", "c", "g", "d", "a", "e", "b"]
    vowelnotes = ["d-", "e-", "g-", "a-", "b-"]
    vowels = ["A", "E", "I", "O", "U"]
    
    for letter in text:
        if letter != " ":
            if letter in vowels:
                note = vowelnotes[vowels.index(letter)]
            elif letter in common:
                note = str(notes[common.index(letter) % 7])
        else:
            note = "r"
    
        final += note + " "

    return final


def main():
    text = input("Enter phrase: ").upper()

    # final = AlphaOrdered(text)
    final = CommonOrdered(text)

    import os
    print(final)
    print(final, file=open("temp.alda", "w"))

    os.system("alda play -f ./temp.alda")

if __name__ == "__main__":
    while True:
        main()
