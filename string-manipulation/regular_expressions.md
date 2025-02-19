# Regular Expressions in Python

***Regular expressions are used for text processing, data filtering and preprocessing.***

---

## 1. Basic Regex Syntax

| Regex   | Description                       | Example                                              |
|---------|-----------------------------------|------------------------------------------------------|
| `.`     | Wildcard                          | `"c.t"` -> `"cat", "cut"`                            |
| `^`     | Start of string                   | `"^Hello"` -> 🟢 `"Hello world"`, 🔴 `"world Hello"` |
| `$`     | End of string                     | `"world$"` -> 🟢 `"Hello world"`, 🔴 `"world Hello"` |
| `*`     | Zero or more repetitions          | `"ab*c"` -> `"ac"`, `"abbc"`                         |
| `+`     | One or more repetitions           | `"ab+c"` -> `"abbc"`, 🔴 `"ac"`                      |
| `?`     | Zero or one occurrence (optional) | `"colou?r"` -> `"color"`, `"colour"`                 |
| `{n}`   | Exactly n repetitions             | `"a{3}"` -> 🟢 `"aaa"`, 🔴 `"aa"`                    |
| `{n,}`  | At least n repetitions            | `"a{2,}"` -> `"aa"`, `"aaa"`                         |
| `{n,m}` | Between n and m repetitions       | `"a{2,4}"` -> `"aa"`, `"aaa"`, `"aaaa"`              |

---

## 2. Character Classes

| Regex          | Description                             | Example          |
|----------------|-----------------------------------------|------------------|
| `[abc]`        | Any one of a, b, or c                   | 🟢`"b"`, 🔴`"f"` |
| `[^abc]`       | Any character except a, b, c            | 🟢`"f"`, 🔴`"a"` |
| `[a-z]`        | Any lowercase letter                    | `"hello"`        |
| `[A-Z]`        | Any uppercase letter                    | `"HELLO"`        |
| `[0-9]`        | Any digit from 0 to 9                   | `"123"`          |
| `[a-zA-Z0-9_]` | Any alphanumeric charater or underscore | `"hello_123"`    |

---

## 3. Frequent Regex Operations in Python

### Extracting all words from a string

```python
import re

text = "Hello, world! Python is great."
words = re.findall(r'\w+', text)
print(words)  # ['Hello', 'world', 'Python', 'is', 'greate']
```

> `\w+` Extracts words by matching sequences of alphanumeric characters.

### Checking if a string starts with a specific pattern

```python
import re

pattern = r'^Hello'
text1 = "Hello world"
text2 = "world Hello"

print(bool(re.match(pattern, text1)))  # true
print(bool(re.match(pattern, text2)))  # false
```

> `^` ensures the match occurs at the beginning of the string.

---

## 4. Key Regex Functions

| Function                         | Description                                                |
|----------------------------------|------------------------------------------------------------|
| `re.match(pattern, text)`        | Checks if the text starts with a specific pattern.         |
| `re.search(pattern, text)`       | Find the first values of the pattern in the text.          |
| `re.findall(pattern, text)`      | Extracts all values of the pattern in a list.              |
| `re.sub(pattern, replace, text)` | Replace all values of the pattern with a specified string. |

---

## 5. Most Frequently Used Regex Patterns
| Regex           | Description                        |
|-----------------|------------------------------------|
| `r'\w+'`        | Extract words                      |
| `r'\d+'`        | Extract all numbers                |
| `r'^\w+'`       | Extract the first word in a string |
| `r'\b[A-Z]+\b'` | Find all uppercase words           |
| `r'\s+'`        | Find whitespace                    |

---
## At least remeber...
`re.findall(r'\w+', text)` for extracting words in most cases.  
`re.sub(r'[^\w]', ' ', text)` to remove punctuation.

## Reference
[Official Regular Expressions(Python)](https://docs.python.org/3/library/re.html)