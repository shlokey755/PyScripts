# PyScripts

An index of every script in this repository, organized by what the code actually does rather than just its filename (a few filenames are misleading — flagged where relevant).

## About this collection

This is a personal collection of Python practice scripts built up while learning the language and then applying it with **pandas** and **matplotlib**. Based on the code itself, it looks like coursework for a CBSE-style Informatics Practices (IP) / Computer Science subject, paired with an Accountancy project — several scripts analyze a company's real financial statements (in ₹ Crore) through ratio analysis and comparative/common-size statements, and one draft file even has a note reading `24 acc / 28 ip / 3 eco`.

The collection spans:

- **Fundamentals** — variables, input/output, conditionals, loops, functions, lists, dictionaries, and strings.
- **pandas** — creating and accessing `Series` and `DataFrame` objects in nearly every common way.
- **matplotlib** — bar, line, histogram, and pie charts, plus one parametric "butterfly curve."
- **Two capstone-scale projects** — a menu-driven Sleep Health dataset explorer, and a set of Accountancy scripts analyzing comparative/common-size financial statements.
- **A few extras** — a K-Means clustering pass over a weather dataset, two small games, and some scratch/REPL files.

### Requirements

Most scripts use only the standard library. Where third-party packages are imported:

```
pip install pandas matplotlib numpy scikit-learn
```

`scikit-learn` is only needed for one file (`iit.py`); everything else in pandas/matplotlib territory just needs `pandas`, `matplotlib`, and occasionally `numpy`.

### A few things to know before running anything

- Nearly every script calls `input()`, so they're meant to be run from a terminal, not double-clicked.
- All files use Windows-style (`\r\n`) line endings — one file (`type.py`) is literally a saved IDLE console session, confirming a Windows/IDLE origin.
- Three scripts load a CSV from a hardcoded local path (`C:\Users\Keerti\Downloads\...`) — you'll need to point these at your own copy of the dataset to run them: `Project File 2025.py`, `project file 2025 9th function.py`, and `iit.py`.
- A handful of scripts are incomplete drafts or contain small bugs that stop them from doing what their name suggests — these are flagged in *italics* below, not as criticism, just as a heads-up.
- Four pairs of files are byte-for-byte identical; each occurrence is flagged.

### Contents

1. Basics: Variables, Expressions & Simple I/O — 28 files
2. Conditionals — 12 files
3. Loops & Number Patterns — 25 files
4. Functions — 6 files
5. Lists, Dictionaries & Strings — 10 files
6. pandas — Series — 16 files
7. pandas — DataFrame — 12 files
8. Data Visualization (matplotlib) — 13 files
9. Capstone / Menu-Driven Project Files — 4 files
10. Accountancy & Finance Analytics Project — 5 files
11. Data Science (Clustering) — 1 file
12. Mini Games & Fun Scripts — 5 files
13. Miscellaneous, Scratch & Non-Runnable Files — 4 files

**Total: 141 scripts** (plus this README)

---

## 1. Basics: Variables, Expressions & Simple I/O (28 files)

| File | Description |
|---|---|
| `17 july.py` | Reads weight and height, then evaluates `height>5 and weight>50` — *the result is never printed, so running it produces no visible output.* |
| `a-b+4ab.py` | Reads `a`, `b`, `c` and computes `a² − b² + 4ac`. |
| `actual time.py` | Subtracts a fixed offset of 1200 from a "digital time" input to get an "actual time." |
| `alternative exchange.py` | Swaps two hardcoded variables using Python's tuple-assignment trick (`a, b = b, a`). |
| `area of circle.py` | Computes the area of a circle from a radius input, using `pi = 3.14`. |
| `area.py` | Computes the perimeter and area of a rectangle from length/width input. |
| `distance.py` | Computes time taken, given a distance and speed input. |
| `even or odd.py` | Prints a number's floor-division and modulus results, labeled "even" and "odd" — *doesn't actually branch on the result (see `odd or even.py` for the working version of this idea).* |
| `exchanged values.py` | Swaps two hardcoded variables using a temporary third variable. |
| `execute code.py` | A short variable-reassignment trace (`x`, `y`, `z`) for practicing how to read code execution order. |
| `exp.py` | A draft percentage calculator — *calls `per(...)` as a function, which was never defined, so this raises a `NameError`.* |
| `exp2.py` | A draft percentage calculator over five subjects — *references a `percentage` variable that's never computed, so this raises a `NameError`.* |
| `exponent.py` | Cubes a user-entered number. |
| `height inches.py` | Converts a height given in total inches into feet plus remaining inches. |
| `illustration.py` | Reads two numbers and prints their sum and product. |
| `lost.py` | Another draft marks-percentage calculator — *same `per(...)` issue as `exp.py`, so it also raises a `NameError`.* |
| `percentage.py` | Sums five hardcoded subject marks and computes the percentage. |
| `practice1.py` | Reads two numbers and prints their sum and product (near-duplicate of `illustration.py`). |
| `practice2.py` | Distance/speed/time calculator (near-duplicate of `distance.py`). |
| `practice3.py` | Simple-interest calculator (principal, rate, time). |
| `profit.py` | Computes profit and loss from cost price and selling price, and prints both regardless of which one actually applies. |
| `ratioandvariables.py` | Reads four numbers and prints a "ratio" — *operator precedence means it actually computes `a + b/c − d`, not `(a+b)/(c−d)`.* |
| `simple interest.py` | Simple-interest calculator with a hardcoded time value of `1.3`. |
| `start code.py` | A bare variable-reassignment trace with no `print()` calls at all — a "predict the values" exercise. |
| `temperature conversion(fahrenheit to celsius).py` | Converts a Fahrenheit input into Celsius. |
| `time conversion.py` | Converts a total-minutes input into hours and minutes. |
| `timehehe.py` | The same minutes-to-hours conversion as `time conversion.py`. |
| `xyz.py` | The same variable-reassignment trace as `execute code.py`, this time with `print()` statements included. |

## 2. Conditionals (12 files)

| File | Description |
|---|---|
| `and operator.py` | Checks sports eligibility from height/weight using an `or` condition (the filename says "and"). |
| `areas of shapes.py` | Asks for a shape name, then computes area for square/circle/rectangle/triangle via an `elif` chain. |
| `harmendragupta.py` | A basic four-function calculator (+, −, ×, ÷, plus `**` for power) selected by an operator input; comments are in Hinglish ("calculator banayenge" = "let's build a calculator"). |
| `not operater.py` | Compares two hardcoded numbers with `>=` — *despite the filename, it doesn't use the `not` operator.* |
| `numbers and operators.py` | Another basic calculator (+, −, ×, ÷, `**`) selected by an operator input. |
| `odd or even.py` | Correctly checks whether a number is odd or even using `%`; comments are bilingual (English/Hindi). |
| `postive or negative.py` | Checks whether a number is positive or negative. |
| `salary and experience and bonus.py` | Calculates a bonus percentage from salary and years of experience using nested `if`/`elif` thresholds. |
| `time conversion if condition.py` | Converts a digital time value into 12-hour am/pm format. |
| `uppercaseandlowercase.py` | Checks whether a character is upper- or lowercase by comparing it against `'A'` and `'Z'`. |
| `username and password.py` | Grants "admin" / "user" / "guest" access levels based on hardcoded username/password combinations. |
| `weekday.py` | Maps a day number (1–7) to its weekday name via an `elif` chain. |

## 3. Loops & Number Patterns (25 files)

| File | Description |
|---|---|
| `100 to 1.py` | Prints 100 down to 1 using a `for` loop with a step of `-1`. |
| `1000 to 1 while loop.py` | Prints 1000 down to 1 using a `while` loop. |
| `911.py` | Four levels of nested `for` loops, printing a marker at each level to show how nested loops unwind. |
| `912.py` | Builds a small dictionary inside a nested loop — *has no `print()`, so it produces no visible output.* |
| `914.py` | Prints a triangle made of `^` characters using nested loops. |
| `ListAppend.py` | Builds a list of numbers from 1–100 through a long chain of `elif` conditions checking specific values one at a time (8, 18, 28…78, the range 80–89, and 98) rather than a general divisibility rule. |
| `factorial of a no.py` | Computes the factorial of a number with a `for` loop. |
| `gg.py` | Sums the numbers from 0 up to (but not including) a user-entered value. |
| `list for average.py` | Collects marks for *n* students into a list, then computes the average. |
| `looping.py` | The simplest possible `for` loop, printing 1 through 10. |
| `odd and even separately.py` | Reads 10 numbers and sums the odd ones and even ones separately. |
| `odd no looping.py` | Prints all odd numbers from 1 to 49 using a step of 2. |
| `practicepaper.py` | Attempts to merge two dictionaries on matching keys — *a chained-comparison bug (`i in a == i in b`) means the merge condition never actually triggers, so the result stays empty.* |
| `prime or not prime.py` | Checks whether a number is prime via trial division. |
| `rev wile loop 100 to 1.py` | Prints 100 down to 1 using a `while` loop (the `while`-loop version of `100 to 1.py`). |
| `reversing no.py` | Intended to print a number's digits in reverse — *the loop counter is never decremented, so this is an infinite loop.* |
| `reversing numbers.py` | Reverses the digits of a number using `//` and `%` inside a `while` loop — the working version of the idea in `reversing no.py`. |
| `sum of 10 manually.py` | Reads 10 numbers one at a time and sums them. |
| `sum of n numbers.py` | Sums the numbers from 1 to *n*, entered at runtime; comments explain the loop logic in Hinglish. |
| `tables while loop.py` | Prints a multiplication table using a `while` loop. |
| `tables.py` | Prints a multiplication table using a `for` loop; comments explain each line in Hinglish. |
| `traversing a list.py` | Reads a string as a list of characters and prints each one with a `for` loop. |
| `traversing via while loop.py` | The same list traversal, using a `while` loop and an index counter instead. |
| `useless program i guess.py` | Groups the words of a sentence by their first letter into a dictionary. |
| `while loop 1 to 1000.py` | Prints 1 through 1000 using a `while` loop. |

## 4. Functions (6 files)

| File | Description |
|---|---|
| `add1.py` | A no-argument `add1()` function that reads two numbers via `input()` internally and returns their sum. |
| `add2.py` | An `add2(x, y)` function that takes its two numbers as parameters instead. |
| `add3.py` | An `add3()` function with two hardcoded numbers, printing each before returning the sum. |
| `areacircle.py` | An `areacircle(x)` function that prints the radius and computed area. |
| `function.py` | A `func1()` function that reads 10 numbers and sums the odd and even ones separately. |
| `multiples.py` | A `multiples(x)` function that prints the first five multiples of `x`. |

## 5. Lists, Dictionaries & Strings (10 files)

| File | Description |
|---|---|
| `811.py` | Collects admission no., roll no., name, and subject for *n* students into a dictionary, then prints all records (identical to `dictionary.py`). |
| `dictionary.py` | Identical to `811.py` — the same student-records exercise. |
| `fh.py` | Reads a name, class, and age, then prints a flattering multi-line description of "the boy" as a footballer — a string-formatting/`input()` exercise. |
| `football.py` | Prints a three-part string introducing itself as "my first script in python." |
| `friends table.py` | Prints a tab-formatted table of classmates' names, classes, and sections. |
| `hehe.py` | Collects 10 numbers into a list, then reverses the first five — *has no final `print()`, so the result is never shown.* |
| `inverted.py` | Reverses the string `'ayruam'` using slice notation `[::-1]`. |
| `names and passes.py` | Collects *n* name/password pairs into parallel lists and a dictionary, then prints all three. |
| `start code1.py` | A scratch file of seven mini-programs, each wrapped in triple-quotes so none of them actually run: computing an average, building a list of even numbers, searching a list for an element, counting occurrences, and three dictionary lookup/search variants. |
| `str.py` | Reverses the string `'chess'` using slice notation. |

## 6. pandas — Series (16 files)

| File | Description |
|---|---|
| `changing index after creation of series.py` | Attempts to reassign a Series' index after creation — *calls `s.index(...)` as if it were a function, which isn't valid (it should be an assignment like `s.index = [...]`), so this raises a `TypeError`.* |
| `creating a series using a dictionary.py` | Creates a `Series` from a `dict` of names. |
| `creating a series using a list.py` | Creates a `Series` from a list, with custom letter-based index labels. |
| `creating a series using a mathematical expression.py` | Creates a `Series` from a numpy array, indexed by the squares of its own values. |
| `creating a series using a numpy array.py` | Creates a `Series` directly from a numpy array. |
| `creating a series using constant value.py` | Creates a `Series` where one scalar value is repeated across custom index labels. |
| `creating an empty series.py` | Creates an empty `Series` (doesn't print it). |
| `giving index to series using for loop.py` | Creates a `Series` from a `range()` with custom letter index labels. |
| `program to access elements of a Series using iloc and loc functions.py` | Demonstrates `.iloc[]` (position-based) vs. `.loc[]` (label-based) slicing on the same Series. |
| `program to access elements of a Series using index labels.py` | Selects specific elements from a name-indexed Series by label (identical to `program to change name of a series.py`). |
| `program to access elements of a Series using index position.py` | Slices a Series by integer position, including a reversed slice. |
| `program to access elements using conditions.py` | Filters a Series using boolean conditions (`s[s > 1]`, `s[s < 2]`). |
| `program to change name of a series.py` | Identical to `program to access elements of a Series using index labels.py` — despite the filename, it doesn't demonstrate renaming a Series. |
| `program to delete an element from a series.py` | Removes an element from a Series with `.drop()`. |
| `program to print first five elements of a series.py` | Uses `.head()` to print the first five elements. |
| `program to print last five elements of a series.py` | Uses `.tail()` to print the last five elements. |

## 7. pandas — DataFrame (12 files)

| File | Description |
|---|---|
| `4.py` | Builds a small `DataFrame` of fruit sales across four Jammu & Kashmir cities. |
| `913.py` | Builds a `DataFrame` of school computer inventory (working/non-working counts) and prints its `.shape`. |
| `IP Final q36.py` | Builds a `DataFrame` from a dict of hospital department/fee data — reads like an exam-style practice question. |
| `creating a dataframe using dictionary of lists.py` | Creates a `DataFrame` from a `dict` where each value is a list. |
| `creating a dataframe using dictionary of series.py` | Creates a `DataFrame` from a `dict` of `Series` objects. |
| `creating a dataframe using list of dictionary.py` | Creates a `DataFrame` from a list of `dict` records. |
| `creating a dataframe using lists.py` | Creates a `DataFrame` from a list of lists, with named columns. |
| `creating a dataframe using ndarray.py` | Creates a `DataFrame` from a list of numpy arrays. |
| `creating a dataframe using series.py` | Creates a `DataFrame` directly from two `Series` objects. |
| `niga.py` | Builds a `DataFrame` of products and prices (laptop, desktop, monitor, tablet). |
| `program to create an empty dataframe.py` | Creates and prints an empty `DataFrame`. |
| `team.py` | Builds a `DataFrame` of a football team roster (name, class, position) with a couple of `NaN` positions, for slicing practice. |

## 8. Data Visualization — matplotlib (13 files)

| File | Description |
|---|---|
| `915.py` | Plots a small `DataFrame` as a line chart. |
| `916.py` | A basic line plot connecting a fixed sequence of x/y coordinate pairs, with the grid turned off. |
| `917.py` | Plots three overlaid lists as a multi-line chart. |
| `IP practical.py` | A styled bar chart of (fictional) app download counts, with axis labels and a title. |
| `assignment.py` | Three chart "assignments" (sports tally, weekly temperature, programming-language popularity) — *all three are commented out, so running the file produces no output.* |
| `bar chart.py` | Two stacked subplots (bar + line) sharing the same data points. |
| `butterfly.py` | Plots a parametric "butterfly curve" using `numpy`; an earlier draft version is kept commented out above the final one. |
| `circle.py` | A minimal line plot of four points (the comment references the circle equation `x² + y² = r²`, though the plotted points don't actually trace a circle). |
| `ddd.py` | A histogram of 100 random normal values. |
| `histofram.py` | A histogram of a fixed list of numbers (identical to `histogram.py`). |
| `histogram.py` | Identical to `histofram.py` — the same histogram example. |
| `plotting a quadratic equation using dashed line chart.py` | Plots a downward parabola (`1 − 0.5x²`) as a dashed blue line. |
| `pusaa.py` | Plots three labeled lines ("Normal," "Slow," "Fast") on one chart with a legend. |

## 9. Capstone / Menu-Driven Project Files (4 files)

These are the largest and most developed files in the collection.

| File | Description |
|---|---|
| `Project File 2025.py` | **The main capstone project** (~640 lines): a menu-driven console app for exploring a "Sleep Health" dataset with pandas. Lets you choose how to load the CSV (full / no index / no header / *n* rows / specific columns), then explore it via `.head()`/`.tail()`, index, columns, size, shape, dtypes, transpose, and `.iloc`/`.loc` slicing, before visualizing it as a bar (vertical/horizontal), line, or histogram chart. |
| `project file 2025 9th function.py` | A working draft of the project above — practice with `.iloc`/`.loc` row/column filtering on a small sample DataFrame, then several draft chart attempts (sleep duration, physical activity, stress level) against the real sleep-health CSV, before settling on one final simple plot. |
| `module.py` | A menu-driven "learning reference" tool: you type the name of a topic (e.g. `Areaofsquare`, `forloopfibonacciseries`, `whileloopfibonacciseries`) and it prints the corresponding beginner code snippet as text. Covers area formulas, unit conversions, and `for`/`while` loop patterns including Fibonacci. |
| `3232343.py` | Byte-for-byte identical to `module.py`. |

## 10. Accountancy & Finance Analytics Project (5 files)

Together these read as one running project: pulling apart a company's financial statements (figures in ₹ Crore) through ratio analysis, comparative statements, and common-size statements, all visualized with matplotlib.

| File | Description |
|---|---|
| `CASHFLOW CALCULATOR.py` | An interactive cash-flow-from-operations calculator (surplus, dividends, general reserve, tax provisions/adjustments) built from chained `input()` prompts — *the tax-adjustment branch always evaluates true due to a common beginner pitfall (`x == 'Yes' or 'YES' or 'yes'` is always truthy, regardless of `x`).* |
| `acc.py` | A sequence of financial-ratio bar/pie charts (profitability, liquidity, debt-to-equity, activity turnover), mostly kept as commented-out drafts, ending in an active Interest Coverage Ratio bar chart. |
| `acc2.py` | A cleaner, final version of the Interest Coverage Ratio bar chart from `acc.py`, with value labels on top of each bar. |
| `acc3.py` | The most complete file in this group: comparative and common-size Balance Sheet & P&L statements across five years (Mar 2020–2024), with several charting approaches drafted and commented out, ending in an active line-chart comparison of Mar 2023 vs. Mar 2024. |
| `common size income statement.py` | Two pie charts comparing a common-size income statement between Mar 2023 and Mar 2024 — *references `ax1`/`ax2` subplot axes that are never created, so this raises a `NameError`.* |

## 11. Data Science — Clustering (1 file)

| File | Description |
|---|---|
| `iit.py` | Loads a weather dataset and works through descriptive stats (hottest record, average humidity, most common wind direction), a nearest-neighbor-style distance comparison, and finally K-Means clustering (`scikit-learn`) to group records by similarity. Several earlier analysis steps are kept commented out above the final clustering code. |

## 12. Mini Games & Fun Scripts (5 files)

| File | Description |
|---|---|
| `PT tactics.py` | A single `print()` statement listing football teammates by nickname with informal notes on playing style — a multi-line string-formatting exercise rather than a program with logic. |
| `goats.py` | Prints a celebration phrase for a chosen footballer (Ronaldo/Messi/Neymar) via `elif` — *the `else` branch is missing `print()`, so an unrecognized name shows nothing.* |
| `race.py` | A complete little text-based car race: a `Car` class with random movement, run in a loop until one car crosses the finish line. |
| `run.py` | A "choose your GOAT" sketch — *uses undefined names (`cr7`, `lm10`) and invalid syntax (`if a1 then=`), so it doesn't run as written.* |
| `ttt.py` | A full two-player Tic-Tac-Toe game in the console, with board printing, win-checking (rows/columns/diagonals), and turn-taking. |

## 13. Miscellaneous, Scratch & Non-Runnable Files (4 files)

| File | Description |
|---|---|
| `iitm.py` | A Kaggle-notebook snippet: randomly samples 50 GIFs from a Pokémon image dataset and builds an HTML `<table>` to display them — *written for a Kaggle/Jupyter environment (hardcoded `/kaggle/input/...` path, and calls `HTML()` without importing it), so it won't run standalone.* |
| `reversing no.s` | An empty file — the unusual `.s` extension suggests it's an accidental save artifact from `reversing no.py`. |
| `s.py` | An empty file. |
| `type.py` | A saved Python IDLE console session, not a runnable script — it explores `type()`, `bool`, `None`, and the `NameError` you get from typing `none` instead of `None`. Kept as reference notes rather than a program. |

---

*Descriptions above come from reading each script's actual code, not just its filename — a few filenames (`not operater.py`, `even or odd.py`, `program to change name of a series.py`, `and operator.py`) describe something different from what the code inside actually does.*
