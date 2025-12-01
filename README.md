## README.md Template

Name: Kacper Wycka. 
Student Number: C00311158. 


---

### Task 1 (10%)

> Completed all steps from "Exam recording" requirements
> Completed all steps from "Setup Instructions"
> Created this Document!


---

### Task 2: Festive Cheer (10%)

```bash
alias cheer='echo Almost XMas. you got this! lets go!'
```


---

### Task 3 : Echo whoami to file (10%)

```bash
echo whoami task2.md 
```


---

### Task 4 : details.sh script (20%)

```bash
echo "User: $(whoami)"
echo "Current dir: $(pwd)"
echo "Host: $(hostname)"
```


---

### Task 5 : Readme python (20%)

```python
with open("input.txt", "r") as input:
    for line in input:
        number = line.strip()
        number2 = int(number)

        if number2 % 2 == 0:
            print("even")
        else:
            print("odd")


```


---

### Task 5b : python output (10%)

```python
with open("input.txt", "r") as input:
    for line in input:
        number = line.strip()
        number2 = int(number)
        number3 = str(number2)

        with open("output.md", "w") as output:        
            if number2 % 2 == 0:    
                output.write((number3 + " even"))
                print(number3 + " even")
            else:
                output.write((number3 + " odd"))
                print(number3 + " odd")

```


---

### Task 6 : Bash Function (20%)

```bash
cipher () {
        echo "$1" | tr 'abcdefghijklmnopqrstuvwxyz' 'zyxwvutsrqponmlkjihgfedcba'
}

```