# BRAIN GAMES

## The package contains five simple mathematics quiz games:
* Even check brain-even
* Calculator brain-calc
* Greatest common divider brain-gcd
* Arithmetic progression brain-progression
* Prime number brain-prime

## Installation requirements

```Python-version = 3.8.1``` \
```Poetry-version = 1.5.1 ```

## How install: 
* ```git clone https://github.com/JsRend/python-project-49.git``` Copy the repository to the desired directory. 
* ```make install``` to install poetry packages. 
* ```make build``` to build your packages inside your project. 
* ```make package-install``` installs the built package from our OS, so we can start using simple shell commands.

## Example of how the game works:

The game "Even Check".
The essence of the game is as follows: a random number is shown to the player.
And he needs to answer "yes" if the number is even, or "no" if it is odd:


```
Welcome to the Brain Games!
May I have your name? Bill
Hello, Bill!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: yes

```

If the player gives an incorrect answer, it is necessary to end the game and display a message:

```

'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!

```

If the player has entered the correct answer, the following will be displayed:

```
Correct!

```
The player must give the correct answer to three questions in a row.

# How it works

## Calc-game

Starting the game:

```
brain-calc
```
What is the result of the expression?

```
Question: 6 + 20
Your answer: 26
Correct!

```
[![asciicast](https://asciinema.org/a/PYLr7u0QKyJSQXlzSBEAjI5b6.svg)](https://asciinema.org/a/PYLr7u0QKyJSQXlzSBEAjI5b6)

## Even-game

Starting the game:

```
brain-even
```
Answer "yes" if number even otherwise answer "no".

```
Question: 17
Your answer: no
Correct!

```

[![asciicast](https://asciinema.org/a/DJrJyVc94o0VPmmhX7e7XbCl3.svg)](https://asciinema.org/a/DJrJyVc94o0VPmmhX7e7XbCl3)

## Gcd-game

Starting the game:

```
brain-gcd
```
Find the greatest common divisor of given numbers.

```
Question: 36 60 
Your answer: 12
Correct!

```

[![asciicast](https://asciinema.org/a/TjfjIA8iPWjZv09BNvt6bzyWC.svg)](https://asciinema.org/a/TjfjIA8iPWjZv09BNvt6bzyWC)

## Prime-game

Starting the game:

```
brain-prime
```
Is this number prime?

```
Question: 7
Your answer: yes
Correct!

```

[![asciicast](https://asciinema.org/a/pqjAPtj7AnyWHwYMirpB0oyfq.svg)](https://asciinema.org/a/pqjAPtj7AnyWHwYMirpB0oyfq)

## Progression-game

Starting the game:

```
brain-progression
```
What number is missing in this progression?

```
Question: 5 7 9 11 13 15 .. 19 21 23
Your answer: 17
Correct!

```
[![asciicast](https://asciinema.org/a/4abxuwX2ay3Bw3tDN1pHKKtUF.svg)](https://asciinema.org/a/4abxuwX2ay3Bw3tDN1pHKKtUF) 

### Hexlet tests and linter status:
[![Actions Status](https://github.com/JsRend/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/JsRend/python-project-49/actions)
