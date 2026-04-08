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
## 🛠️ Lessons from the Trenches: Debugging
### The "Subscriptable" Range Error
**Problem**: Encountered `TypeError: 'range' object is not subscriptable`.
**Cause**: Using square brackets `[]` instead of parentheses `()` when calling the `range` function. 
- `[]` is used for **indexing/subscripting** (accessing an existing element).
- `()` is used for **invoking a function**.
**Fix**: Changed `range[start, stop]` to `range(start, stop)`.

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