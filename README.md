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
- **Day 11**: Recursion Basics & Functional Logic. ✅
- The Core Concept: Moved from iterative loops to the recursive "self-calling" model. Learned that recursion is simply a function solving a small part of a problem and delegating the rest to another instance of itself.
- The Call Stack: Understood how memory manages recursive calls. Each call stays in the stack until it hits the Base Case, then they all resolve (pop) in reverse order.
- Complexity Analysis: Learned that while recursion looks "cleaner," it carries an $O(N)$ space complexity due to the stack, unlike a simple loop which is $O(1)$ space.
## 🔢 Mathematical Implementation
- Recursive Patterns
- Printing $1$ to $N$ vs. $N$ to $1$: Explored the difference between printing before the recursive call (top-down) and printing after the call (backtracking).
- Parameterized Recursion: Implemented the "Sum of $N$ Numbers" by passing the running total as a parameter through the function calls.
- Functional Recursion: Solved the Factorial problem by returning values up the stack: $f(n) = n \times f(n-1)$.
## 🛠️ Lessons from the Trenches: Debugging
- Avoiding the Stack OverflowProblem: 
- Encountered RecursionError while testing larger ranges.
- Cause: Missing or unreachable Base Case. If the condition if n == 0 is never met, the function calls itself until the computer runs out of memory.
- Solution: Always ensure the input variable is moving toward the base case (e.g., $n-1$) and that the base case is defined before the recursive call.
- **Day 12**: Functional Recursion & Hashing Foundations. ✅
- Functional Recursion: Moved beyond printing values to returning them up the stack. Implemented the Fibonacci series, where each call returns the sum of the two preceding calls.
- Hashing & Frequency Arrays: Learned that hashing is the process of mapping data to a fixed size for faster access. This is the key to solving "Count Frequency" problems in $O(N)$ time. 
- Python Dictionary Optimization: Integrated the .get() method to handle frequency counting efficiently.
## 🔢 Mathematical Implementation
- Recursive String/List ManipulationPalindrome Check: Used two pointers $(s, e)$ in a recursive function to compare characters from both ends of the string "ABBA".Fibonacci Series: Implemented $f(n) = f(n-1) + f(n-2)$, visualizing the recursive tree and the exponential increase in calls.Frequency Counting (Hashing)The .get() Method: Used d[item] = d.get(item, 0) + 1.
- Why it matters: The .get(key, default) method returns the default value if the key doesn't exist, eliminating the need for if key in dict checks.
## 🛠️ Lessons from the Trenches:
-  DebuggingRecursive Tree ExplosionInsight: While $f(n-1) + f(n-2)$ is mathematically beautiful, it becomes very slow for large $N$ because it recalculates the same values multiple times. This is my first real-world encounter with the need for Dynamic Programming (Memoization)!
- **Day 13**: Advanced Hashing & Comparison Sorts. ✅
- Frequency Analysis: Extended the hashing logic to identify elements with the highest and lowest frequencies.
- Sorting Foundations: Started the Sorting chapter, focusing on two $O(N^2)$ algorithms: Selection Sort and Bubble Sort.In-Place Swapping: Practiced Python’s elegant tuple unpacking for swapping: arr[i], arr[j] = arr[j], arr[i].
## 🔢 Mathematical Implementation1. 
- 1. Selection Sort (Select Min)Strategy: Find the minimum element in the unsorted part and swap it with the first element of that part.Complexity: $O(N^2)$ for both best and worst cases.2. 
- 2. Bubble Sort (Push Max to End)Strategy: Repeatedly swap adjacent elements if they are in the wrong order.Complexity: $O(N^2)$ (Average/Worst).
- 3. Frequency TrackingLogic: After building the dictionary with .get(), I iterated through d.items() to compare counts against mxcount and mncount variables.
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

- **Day 14**: Advanced Sorting & Divide and Conquer ✅
- Insertion Sort: Implemented the logic of placing each element in its correct position relative to the already sorted part of the array.
- Merge Sort: Leveraged recursion to divide arrays into single elements and then merge them back in sorted order. Learned that it is a stable sort with $O(N \log N)$ time complexity.
- Quick Sort: Practiced the partition algorithm, using a pivot to rearrange elements. Explored how recursive sub-problems are solved in-place.Python Built-in Sorting: Experimented with .sort() and sorted() for basic lists and nested structures (lists of lists).
## 🔢 Mathematical Implementation
- 1. Merge Sort (The Merge Step)Concept: Uses three pointers ($i, j, k$) to compare elements from two temporary sub-arrays (left and right) and place the smaller one back into the original array.Complexity: Always $O(N \log N)$ because the division is always logarithmic and the merge is linear.
- 2. Quick Sort (The Partition Step)Pivot Logic: Selected the last element as the pivot and moved all smaller elements to its left using an index pointer $i$.Recursion: Once the pivot is in its final "sorted" spot, the function calls itself for the left and right partitions.
- 3. Multi-Dimensional SortingTested Python's ability to sort nested lists like [[4,5],[2,4],[1,2],[1,4],[6,7]]. 
- Observations: Python sorts based on the first element, then the second by default.

- **Day 15**: Array Basics - Extremes & Second Extremes. 
- Largest/Smallest: Basic $O(N)$ traversal to find the maximum and minimum values in a single loop.
- Optimal Second Extremes: Developed a one-pass algorithm to find the second-best values.
- Efficiency Goal: Reduced time complexity from $O(N \log N)$ to $O(N)$ and space complexity to $O(1)$.
## 🔢 Mathematical Implementation
- 1. Finding the Second Smallest

- Logic:
- Initialize smallest and second_smallest to infinity (float('inf')).
- If current num < smallest, update second_smallest to the old smallest and set new smallest to num.
- Else if num < second_smallest and num != smallest, update only second_smallest.
- Result: Found 2 as smallest and 12 as second smallest for the test array.

- **Day 16**: Array Basics - Recursion & Searching 🔍
- Is Array Sorted:Iterative Approach: Uses a simple loop comparing neighbors ($O(N)$ time complexity).
- Recursive Approach: Compares the first two elements and recurses on the remainder of the list ($O(N^2)$ space complexity due to list slicing).
- Linear Search (Recursive): Traverses the array by passing an index parameter. 
- Returns the index if the target is found, otherwise returns -1.
## 🔢 Mathematical Implementation
- 1. Checking Sorted State
- Recursive Logic: if arr[0] > arr[1]: return False. Else, return issort(arr[1:]).
- Note: List slicing arr[1:] in Python creates a copy, which increases space complexity compared to passing an index.
- 2. Recursive Linear Search
- Base Case: If index >= len(arr), return -1 (Item not found).
- Target Found: If arr[index] == target, return index.Recursive Step: linear_search(arr, target, index + 1).

## 🔗 Connect with Me
- **LinkedIn**: https://www.linkedin.com/in/parvindersinghbagga/
- **University**: Guru Tegh Bahadur Institute of Technology (GTBIT)
## 🔍 Technical Deep Dive: Linear Search
Today, I implemented a Linear Search algorithm to find a target element $k$ in a list.

- **Time Complexity**: $O(n)$ — In the worst case, we check every element once.
- **Optimization**: Used a `break` statement to stop the loop the moment the target is found, improving the average-case runtime.
- **Logic Pattern**: Initialized a result variable to `-1` to handle the "Not Found" edge case gracefully.