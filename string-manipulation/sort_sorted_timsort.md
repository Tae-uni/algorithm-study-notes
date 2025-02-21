# Python sort function

## sorted() function
`sorted()` return a new sorted **list**. It can be used to sort lists, string and number.
```python
a = [2, 5, 4, 9, 7]
sorted(a)    # [2, 4, 5, 7, 9]

b = 'zbdaf'
sorted(b)    # ['a', 'b', 'd', 'f', 'z']
```

Also, merge together with `join`
```python
b = 'zbdaf'
"".join(sorted(b))    # 'abdfz'
```

sorting with `key=` option 
```python
c = ['ccc', 'aaaa', 'd', 'bb']
sorted(c, key=len)    # ['d', 'bb', 'ccc', 'aaaa']
```
custom function for sorting
```python
a = ['cde', 'cfc', 'abc']

def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
```

---

## sort() function
sort() performs `In-place` sorting, meaning it does not return a new list but modifies the original list.
```python
alist.sort() 
alist = blist.sort()    # Wrong.. sort() has no return
```

---

## Timsort
One of the most well-known sorting algorithms is Merge Sort, invented by John von Neumann.
Most of the time, Quick Sort is faster, but the performance depends heavily on the data.
Merge Sort guarantees a consistent `O(nlogn)` performance.  
Python `sorted()` uses **Timsort**. Timsort assumes that most real-world data is already somewhat sorted and optimizes for that.  
Theoretically, if a sorting algorithm compares each element once, it cannot be faster than `O(nlogn)`. 

---

**Time Complexity of Sorting Algorithm**

<table border="0.5" width="80%">
  <tr>
    <th rowspan="2">Algorithm</th>
    <th colspan="3">Time Complexity</th>
  </tr>
  <tr>
    <th>Best</th>
    <th>Average</th>
    <th>Worst</th>
  </tr>
  <tr>
    <td>Quick Sort</td>
    <td>Ω(n log n)</td>
    <td>Θ(n log n)</td>
    <td>O(n²)</td>
  </tr>
  <tr>
    <td>Merge Sort</td>
    <td>Ω(n log n)</td>
    <td>Θ(n log n)</td>
    <td>O(n log n)</td>
  </tr>
  <tr>
    <td>TimSort</td>
    <td>Ω(n log n)</td>
    <td>Θ(n log n)</td>
    <td>O(n log n)</td>
  </tr>
</table>

