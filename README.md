# Morse — convertisseur texte ↔ code Morse en Python

Un petit programme en ligne de commande, écrit en Python pur (aucune dépendance externe), qui convertit un texte en code Morse et un code Morse en texte.

Le projet est volontairement court (un seul fichier, `morse.py`) et très lisible. Il sert à la fois d'outil utilisable tel quel et d'exemple pédagogique pour comprendre comment on manipule des dictionnaires, des chaînes de caractères et des compréhensions en Python.

---

## Table des matières

1. [Qu'est-ce que le code Morse ?](#1-quest-ce-que-le-code-morse-)
2. [Fonctionnalités](#2-fonctionnalités)
3. [Prérequis](#3-prérequis)
4. [Installation](#4-installation)
5. [Utilisation](#5-utilisation)
6. [Format du code Morse attendu et produit](#6-format-du-code-morse-attendu-et-produit)
7. [Table de correspondance](#7-table-de-correspondance)
8. [Comment fonctionne le code](#8-comment-fonctionne-le-code)
9. [Limites connues](#9-limites-connues)
10. [Tester rapidement](#10-tester-rapidement)
11. [Pistes d'amélioration](#11-pistes-damélioration)
12. [Structure du projet](#12-structure-du-projet)

---

## 1. Qu'est-ce que le code Morse ?

Le code Morse est un système de codage qui représente chaque lettre et chaque chiffre par une suite de signaux courts et longs. À l'écrit, on note :

- le signal court par un **point** : `.`
- le signal long par un **tiret** : `-`

Par exemple, la lettre `S` s'écrit `...` (trois signaux courts), la lettre `O` s'écrit `---` (trois signaux longs). Le message de détresse `SOS` s'écrit donc `... --- ...`.

Pour que le message reste compréhensible, il faut pouvoir distinguer :

- les **symboles d'une même lettre** (qui forment ensemble le code d'une lettre) ;
- les **lettres entre elles** ;
- les **mots entre eux**.

Dans ce projet, la convention de notation écrite est la suivante :

| Séparation | Représentation |
|---|---|
| Entre deux lettres | une espace |
| Entre deux mots | une barre oblique entourée d'espaces : ` / ` |

Ainsi, `SOS 123` devient :

```
... --- ... / .---- ..--- ...--
```

---

## 2. Fonctionnalités

- Conversion **texte → Morse** (les minuscules et les majuscules sont acceptées).
- Conversion **Morse → texte**.
- Prise en charge des **26 lettres** de l'alphabet latin (A–Z) et des **10 chiffres** (0–9).
- Les caractères non pris en charge sont remplacés par un point d'interrogation `?` plutôt que de provoquer une erreur.
- Un petit **menu interactif** pour choisir le sens de la conversion.
- **Aucune dépendance** : uniquement la bibliothèque standard de Python.

---

## 3. Prérequis

- **Python 3** installé sur la machine.

Pour vérifier que Python est disponible, ouvrir un terminal et taper :

```powershell
python --version
```

Sous Linux, macOS ou Termux, la commande est parfois `python3 --version`.

Si la commande affiche un numéro de version commençant par `3`, tout est en ordre. Sinon, il faut installer Python (voir la section suivante).

---

## 4. Installation

Il n'y a rien à « installer » au sens strict : le programme est un unique fichier `morse.py`. Il suffit de le placer dans un dossier de son choix.

### Sous Windows (PowerShell)

```powershell
cd .\Projets\
mkdir Morse
cd Morse
```

Puis créer le fichier `morse.py` avec un éditeur de texte (Bloc-notes, VS Code, etc.) et y coller le code du programme.

> **Attention aux habitudes venues de Linux.**
> La commande `cat > morse.py <<'EOF' ... EOF` est de la syntaxe **bash**. PowerShell ne connaît pas l'opérateur `<<` (appelé *heredoc*) : si on la colle dans PowerShell, chaque ligne du programme est interprétée comme une commande PowerShell, et on obtient une cascade d'erreurs.
>
> L'équivalent PowerShell s'appelle un *here-string* : on ouvre avec `@'`, on ferme avec `'@` placé seul en début de ligne, puis on redirige le tout vers `Set-Content` :
>
> ```powershell
> @'
> ... contenu du fichier ...
> '@ | Set-Content -Path morse.py -Encoding utf8
> ```
>
> Ce bloc doit être collé **à l'invite PowerShell** (`PS ...>`), jamais pendant qu'un programme Python attend une saisie.

### Sous Linux, macOS ou Termux (Android)

```bash
mkdir -p ~/Projets/Morse
cd ~/Projets/Morse
```

Sous Termux, si Python n'est pas encore installé :

```bash
pkg install python
```

On peut ensuite créer `morse.py` avec un éditeur (`nano morse.py`) ou avec un heredoc bash (ici, la syntaxe `cat > ... <<'EOF'` est valide).

---

## 5. Utilisation

Depuis le dossier contenant `morse.py` :

```powershell
python morse.py
```

Le programme affiche un menu :

```
1 = texte -> Morse, 2 = Morse -> texte :
```

### Exemple 1 — Convertir du texte en Morse

```
1 = texte -> Morse, 2 = Morse -> texte : 1
Texte : Bonjour le monde
-... --- -. .--- --- ..- .-. / .-.. . / -- --- -. -.. .
```

### Exemple 2 — Convertir du Morse en texte

```
1 = texte -> Morse, 2 = Morse -> texte : 2
Morse : ... --- ... / .---- ..--- ...--
SOS 123
```

Remarque : le texte obtenu en sortie est toujours en **majuscules**, car le code Morse ne distingue pas les majuscules des minuscules.

### Exemple 3 — Un choix invalide

```
1 = texte -> Morse, 2 = Morse -> texte : 3
Choix invalide.
```

---

## 6. Format du code Morse attendu et produit

Pour que la conversion **Morse → texte** fonctionne, la saisie doit respecter la convention suivante :

- les symboles (`.` et `-`) d'une même lettre sont **collés** : `.-` et non `. -` ;
- les lettres sont séparées par **une espace** : `.- -...` ;
- les mots sont séparés par **une barre oblique** `/`, avec ou sans espaces autour : `.- / -...` et `.-/-...` sont acceptés tous les deux.

Ce qui se passe si le format n'est pas respecté :

| Saisie | Résultat | Explication |
|---|---|---|
| `...---...` | `?` | Sans espaces, la suite est lue comme **un seul** symbole, qui n'existe pas dans la table. |
| `.- -.-.- ..` | `A?I` | Le groupe `-.-.-` ne correspond à aucun caractère connu. |
| `. -` | `ET` | Deux symboles séparés par une espace sont lus comme deux lettres (`E` puis `T`), pas comme `.-` (`A`). |

---

## 7. Table de correspondance

### Lettres

| Lettre | Morse | Lettre | Morse | Lettre | Morse |
|:---:|:---:|:---:|:---:|:---:|:---:|
| A | `.-` | J | `.---` | S | `...` |
| B | `-...` | K | `-.-` | T | `-` |
| C | `-.-.` | L | `.-..` | U | `..-` |
| D | `-..` | M | `--` | V | `...-` |
| E | `.` | N | `-.` | W | `.--` |
| F | `..-.` | O | `---` | X | `-..-` |
| G | `--.` | P | `.--.` | Y | `-.--` |
| H | `....` | Q | `--.-` | Z | `--..` |
| I | `..` | R | `.-.` | | |

### Chiffres

| Chiffre | Morse | Chiffre | Morse |
|:---:|:---:|:---:|:---:|
| 0 | `-----` | 5 | `.....` |
| 1 | `.----` | 6 | `-....` |
| 2 | `..---` | 7 | `--...` |
| 3 | `...--` | 8 | `---..` |
| 4 | `....-` | 9 | `----.` |

---

## 8. Comment fonctionne le code

Cette section détaille le programme pas à pas. Elle s'adresse à toute personne qui souhaite comprendre le code, et pas seulement l'utiliser.

Le fichier comporte quatre éléments : un dictionnaire (`MORSE`), un dictionnaire inversé (`REVERSE`), deux fonctions de conversion (`to_morse` et `from_morse`), et une fonction `main` qui sert d'interface.

### 8.1. Le dictionnaire `MORSE`

```python
MORSE = {
    "A": ".-",    "B": "-...",  ...
    "0": "-----", "1": ".----", ...
}
```

Un **dictionnaire** Python associe des **clés** à des **valeurs**. Ici, chaque clé est un caractère (`"A"`, `"7"`…) et chaque valeur est son code Morse (`".-"`, `"--..."`…).

On l'utilise pour répondre à la question : « quel est le code Morse de la lettre X ? ». L'accès est direct : `MORSE["S"]` renvoie `"..."`.

### 8.2. Le dictionnaire inversé `REVERSE`

```python
REVERSE = {code: lettre for lettre, code in MORSE.items()}
```

Pour le sens inverse, on a besoin de répondre à la question opposée : « quelle lettre correspond au code `...` ? ». Il faut donc un dictionnaire dont les clés sont les codes et les valeurs sont les lettres.

Plutôt que de le réécrire à la main (au risque d'introduire une erreur de copie), on le **génère automatiquement** à partir de `MORSE` grâce à une *compréhension de dictionnaire* :

- `MORSE.items()` fournit tous les couples `(lettre, code)` ;
- pour chaque couple, on crée l'entrée `code: lettre`, c'est-à-dire qu'on **inverse** la paire.

Cette technique n'est valable que parce que **chaque code Morse est unique** dans la table : deux lettres différentes n'ont jamais le même code. Si deux clés partageaient la même valeur, l'inversion écraserait silencieusement l'une des deux.

Un avantage important : une seule table à maintenir. Si on ajoute un caractère dans `MORSE`, il est automatiquement pris en compte dans le sens inverse.

### 8.3. La fonction `to_morse` (texte → Morse)

```python
def to_morse(texte):
    return " / ".join(
        " ".join(MORSE.get(caractere, "?") for caractere in mot)
        for mot in texte.upper().split()
    )
```

Cette fonction se lit **de l'intérieur vers l'extérieur** :

1. `texte.upper()` passe tout le texte en majuscules, car les clés de `MORSE` sont des majuscules.
2. `.split()` découpe le texte en **mots**. Sans argument, `split()` coupe sur n'importe quelle suite d'espaces, de tabulations ou de retours à la ligne, et ignore les espaces en trop.
3. Pour chaque `mot`, on parcourt ses `caractere` un par un.
4. `MORSE.get(caractere, "?")` cherche le code du caractère. La méthode `.get()` accepte une valeur par défaut : si le caractère n'est pas dans le dictionnaire, elle renvoie `"?"` au lieu de lever une erreur (`KeyError`) comme le ferait `MORSE[caractere]`.
5. `" ".join(...)` assemble les codes des lettres d'un mot en les séparant par une espace.
6. `" / ".join(...)` assemble ensuite les mots en les séparant par ` / `.

Exemple, étape par étape, avec `"Le SOS"` :

```
"Le SOS"  ->  "LE SOS"  ->  ["LE", "SOS"]
"LE"   ->  [".-..", "."]        ->  ".-.. ."
"SOS"  ->  ["...", "---", "..."] ->  "... --- ..."
résultat : ".-.. . / ... --- ..."
```

### 8.4. La fonction `from_morse` (Morse → texte)

```python
def from_morse(code):
    return " ".join(
        "".join(REVERSE.get(symbole, "?") for symbole in mot.split())
        for mot in code.split("/")
    )
```

C'est la démarche symétrique, appliquée dans l'ordre inverse :

1. `code.split("/")` découpe le message en **mots**, en coupant sur la barre oblique.
2. Pour chaque `mot`, `mot.split()` le découpe en **groupes de symboles** (les lettres), en coupant sur les espaces. Cela élimine aussi les espaces en trop autour de la barre oblique.
3. `REVERSE.get(symbole, "?")` retrouve la lettre correspondant à chaque groupe, ou `"?"` si le groupe est inconnu.
4. `"".join(...)` recolle les lettres d'un mot **sans séparateur**.
5. `" ".join(...)` recolle les mots avec **une espace**.

### 8.5. La fonction `main` et le point d'entrée

```python
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
```

- `input(...)` affiche une invite et renvoie ce que l'utilisateur tape, sous forme de chaîne.
- `.strip()` retire les espaces superflus au début et à la fin de la saisie, ce qui évite qu'un `"1 "` soit rejeté.
- Le bloc `if / elif / else` aiguille vers la bonne conversion, ou signale un choix invalide.
- La condition `if __name__ == "__main__":` signifie : « n'exécuter `main()` que si le fichier est lancé directement ». Si un autre programme fait `import morse`, les fonctions `to_morse` et `from_morse` deviennent utilisables sans que le menu ne se déclenche. C'est une convention très courante en Python.

### 8.6. Réutiliser les fonctions dans un autre script

Grâce à ce point d'entrée, on peut utiliser les conversions depuis un autre fichier placé dans le même dossier :

```python
from morse import to_morse, from_morse

code = to_morse("Bonjour")
print(code)                # -... --- -. .--- --- ..- .-.
print(from_morse(code))    # BONJOUR
```

---

## 9. Limites connues

Ces limites sont des choix de simplicité, pas des bugs cachés. Il vaut mieux les connaître avant d'utiliser l'outil.

1. **Les caractères accentués ne sont pas gérés.** `é`, `è`, `à`, `ç`… ne figurent pas dans la table et sont remplacés par `?`. Exemple : `Café` donne `-.-. .- ..-. ?`.
2. **La ponctuation n'est pas gérée** (point, virgule, point d'interrogation, apostrophe, etc.). Elle est également remplacée par `?`.
3. **La conversion n'est pas réversible pour les caractères non pris en charge.** Un `?` en sortie signifie « caractère inconnu », et on ne peut pas retrouver le caractère d'origine à partir de lui.
4. **La casse est perdue.** `Bonjour` et `BONJOUR` donnent le même code ; au retour, on obtient `BONJOUR`.
5. **Les espaces multiples et les retours à la ligne sont normalisés.** Ils sont traités comme une simple séparation entre mots.
6. **Un seul message par exécution.** Le programme ne boucle pas : il faut le relancer pour une nouvelle conversion.

---

## 10. Tester rapidement

Sans écrire de test automatisé, on peut vérifier l'aller-retour directement dans l'interpréteur Python :

```powershell
python
```

```python
>>> from morse import to_morse, from_morse
>>> to_morse("SOS 123")
'... --- ... / .---- ..--- ...--'
>>> from_morse("... --- ... / .---- ..--- ...--")
'SOS 123'
>>> from_morse(to_morse("Bonjour le monde"))
'BONJOUR LE MONDE'
>>> to_morse("Café")
'-.-. .- ..-. ?'
```

Un test automatisé minimal, à placer dans un fichier `test_morse.py` et à lancer avec `python -m unittest`, pourrait ressembler à ceci :

```python
import unittest

from morse import to_morse, from_morse


class TestMorse(unittest.TestCase):
    def test_sos(self):
        self.assertEqual(to_morse("SOS"), "... --- ...")

    def test_aller_retour(self):
        texte = "BONJOUR LE MONDE 2026"
        self.assertEqual(from_morse(to_morse(texte)), texte)

    def test_caractere_inconnu(self):
        self.assertEqual(to_morse("é"), "?")


if __name__ == "__main__":
    unittest.main()
```

---

## 11. Pistes d'amélioration

Pour aller plus loin, voici quelques exercices classés par difficulté croissante :

- **Faciliter l'usage** : faire boucler le menu jusqu'à ce que l'utilisateur quitte (`while True` et une option `q`).
- **Gérer la ponctuation** : ajouter à `MORSE` les signes usuels (point, virgule, point d'interrogation, etc.) en s'appuyant sur la table de l'Union internationale des télécommunications.
- **Gérer les accents** : normaliser le texte avant conversion (par exemple avec `unicodedata.normalize("NFD", ...)`) pour que `é` devienne `E`, au prix d'une perte d'information.
- **Passer par des arguments en ligne de commande** avec le module `argparse`, par exemple `python morse.py encode "texte"`. Attention : un code Morse commençant par `-` serait alors interprété comme une option ; il faudrait le séparer avec `--`.
- **Lire et écrire des fichiers** : convertir le contenu d'un fichier texte vers un fichier Morse.
- **Produire du son** : générer des signaux courts et longs (bips) à partir du code Morse.
- **Ajouter de vrais tests automatisés** et les exécuter dans un workflow d'intégration continue.

---

## 12. Structure du projet

```
Morse/
├── morse.py      # Le programme : table, conversions et menu
└── README.md     # Ce document
```

---

## Licence

À préciser par l'auteur du dépôt.
