MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}

REVERSE = {code: lettre for lettre, code in MORSE.items()}


def to_morse(texte):
    return " / ".join(
        " ".join(MORSE.get(caractere, "?") for caractere in mot)
        for mot in texte.upper().split()
    )


def from_morse(code):
    return " ".join(
        "".join(REVERSE.get(symbole, "?") for symbole in mot.split())
        for mot in code.split("/")
    )


def main():
    choix = input("1 = texte -> Morse, 2 = Morse -> texte : ").strip()
    if choix == "1":
        print(to_morse(input("Texte : ")))
    elif choix == "2":
        print(from_morse(input("Morse : ")))
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()
