# Solution

```python
current_sequence = int(input())
num_even = 0
while current_sequence != 0:
  if current_sequence % 2 == 0:
    num_even += 1
  current_sequence = int(input())
print(num_even)
```
  