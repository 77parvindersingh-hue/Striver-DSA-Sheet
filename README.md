# Striver's A to Z DSA Sheet - Python Journey 🚀

This repository tracks my progress as I solve the **Striver's A to Z DSA Sheet** using Python. My goal is to build a strong foundation in data structures and algorithms while maintaining a professional development workflow.

## 🛠️ My Workflow Setup
I use a custom-built **3-Pane VS Code Environment** to optimize my solving speed:
- **coding.py**: Core logic and algorithm implementation.
- **input.txt**: Test cases (pulled via standard input redirection).
- **output.txt**: Results log (pushed via standard output redirection).

By using the **uv** package manager and custom VS Code tasks, I can run and test my code instantly with a single keyboard shortcut (`Ctrl+Shift+B`).

## 📈 Progress Log
- **Day 1**: Environment setup, Git integration, and VS Code automation.
- **Day 2**: Mastering Input/Output streams, handling multiple values per line with `map()`, and capturing data into lists.
- **Day 3**: Deep dive into Python Collections: Operations on Lists, Tuples, Dictionaries, and Sets without errors! ✅
- **DAY-4**: Understanding Mutability vs. Immutability and Data Type Conversion. ✅
- **Day 5**: Mastered Python Slicing (`[start:stop:step]`) and implemented complex decision-making with `if-elif-else` conditional blocks. ✅
- **Day 6**: Mastered Iteration using `for` and `while` loops. Implemented Linear Search with early-exit optimization and documented syntax-level debugging. ✅
- **Day 7**: Modularized code using Functions and began analyzing algorithms using Time and Space Complexity (Big O Notation). ✅
- **Day 8**: Mastered Nested Loops and Pattern Problems. Implemented over 10 different patterns including triangles, inverted pyramids, and character-mapped ASCII art. ✅
- **Day 9**: Completed 7 core Math problems (Count Digits, Reverse Number, Palindrome, GCD, Armstrong Numbers, and Divisors). ✅
- **Day 10**: Advanced Number Theory - Sieve of Eratosthenes. ✅

## 🚀 Key Technical 
- LearningsAlgorithmic Shift: Learned that while the $O(\sqrt{N})$ primality test is perfect for a single number, it becomes a bottleneck when checking a large range.
- The Sieve Logic: Implemented the Sieve of Eratosthenes to systematically "strike out" multiples of each prime, ensuring each composite number is marked only when necessary.
- Complexity Optimization: * Time: Successfully implemented a solution with $O(N \log (\log N))$ complexity.
- Space: Utilized a boolean array (Sieve) for efficient state tracking.
- Inner Loop Optimization: Applied the optimization of starting the multiple-marking process from $p^2$, as all smaller multiples would have been marked by previous primes.- 
- Python Input Handling: Mastered handling multi-line and space-separated inputs from input.txt to run batch tests on the sieve.
## 🔢 Mathematical Implementation
### Digit Extraction
- Used `remainder = num % 10` to isolate the last digit.
- Used `num = num // 10` to reduce the number in each iteration.
- Time Complexity for these operations is generally $O(\log_{10}N)$ because we divide the number by 10 in each step.

### GCD (Greatest Common Divisor)
- Implemented the **Euclidean Algorithm** ($GCD(a, b) = GCD(b, a \% b)$). 
- This is significantly more efficient than checking every number from 1 to $N$.

### Armstrong Numbers
- Logic: Reached the total count of digits first, then iterated through each digit to calculate the power sum.
## 🛠️ Lessons from the Trenches: Debugging
### The "Subscriptable" Range Error
**Problem**: Encountered `TypeError: 'range' object is not subscriptable`.
**Cause**: Using square brackets `[]` instead of parentheses `()` when calling the `range` function. 
- `[]` is used for **indexing/subscripting** (accessing an existing element).
- `()` is used for **invoking a function**.
**Fix**: Changed `range[start, stop]` to `range(start, stop)`.
## 📐 Pattern Logic & Nested Loops
### Key Concepts:
- **Outer Loop**: Controls the number of rows.
- **Inner Loop**: Controls the columns/content of each row.
- **Character Mapping**: Used `chr(65 + i)` to generate alphabetical patterns.
- **Complexity**: $O(n^2)$ time complexity for nested iteration.

### 💡 Pro-Tip:
When building symmetric patterns, always analyze the relationship between the row index ($i$) and the number of spaces or stars required before writing the code.

## ⏱️ Algorithmic Complexity
### Time Complexity ($O(n)$)
- Learned that complexity measures the growth of operations relative to input size.
- Identified $O(n)$ linear time in loop-based operations (like my `sum` and `update` functions).

### Space Complexity
- **Input Space**: Space for the initial data.
- **Auxiliary Space**: Extra space used (e.g., temporary lists).
- Aiming for **In-place algorithms** with $O(1)$ auxiliary space whenever possible!

## 🧠 Key Concepts Mastered
### Mutability & Memory
I explored how Python handles data in memory using the `id()` function:
- **Immutable Types**: Integers, Floats, Strings, and Tuples. (Changing them creates a new object in a new memory location).
- **Mutable Types**: Lists, Dictionaries, and Sets. (Can be modified in place).

### Advanced Data Handling
- **Type Casting**: Converting between collections (e.g., `list(set(obj))` to get unique elements).
- **Zipping**: Combining lists into dictionaries using `zip()`.
- **Boolean Logic**: Understanding "Truthy" and "Falsy" values in Python collections.
## 🔗 Connect with Me
- **LinkedIn**: https://www.linkedin.com/in/parvindersinghbagga/
- **University**: Guru Tegh Bahadur Institute of Technology (GTBIT)
## 🔍 Technical Deep Dive: Linear Search
Today, I implemented a Linear Search algorithm to find a target element $k$ in a list.

- **Time Complexity**: $O(n)$ — In the worst case, we check every element once.
- **Optimization**: Used a `break` statement to stop the loop the moment the target is found, improving the average-case runtime.
- **Logic Pattern**: Initialized a result variable to `-1` to handle the "Not Found" edge case gracefully.