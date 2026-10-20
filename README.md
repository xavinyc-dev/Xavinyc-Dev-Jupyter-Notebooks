# Self-Dev Practice Notes

My study notes for learning software engineering, written as Jupyter notebooks. Each notebook pairs short explanations with code examples that run, so the output shown under every cell is real.

This is a **public** repository. The notes were made for studying and educational purposes only, and they are not for sale or commercial use.

## What is a Jupyter notebook?

A Jupyter notebook is a file ending in `.ipynb` that mixes written notes with code you can run. It is made of blocks called **cells**:

- **Markdown cells** hold text: headings, explanations, tables.
- **Code cells** hold Python. When you run one, its output appears directly underneath.

That makes notebooks a good fit for study notes, because every example can be run and changed to see what happens. If you have never used one, start with **View a notebook** under [Using these notes](#using-these-notes) below. It needs no setup.

## Sources

The material in these notes comes from two places:

- **[The Marcy Lab School GitBook](https://marcylabschool.gitbook.io/swe)**: the software engineering curriculum I am following.
- **[freeCodeCamp](https://www.freecodecamp.org/learn/python-v9/)**: the Python certification lessons.

These notebooks are a mix of two things:

- **Content taken directly from the sources.** Some definitions, explanations, tables, and code examples are copied or closely follow the original lessons, because in my opinion they explain the idea best.
- **My own work.** Many of the summaries, examples, tables, and notes are written by me, including places where I recorded my own predictions and mistakes.

All credit for the original lesson material goes to The Marcy Lab School and freeCodeCamp. For the full, official lessons, go to the sources above.

## A note for other readers

These notes might not be for everyone. They are written for the way I study, they follow the order of my course, and they are a work in progress, so they may contain mistakes. If you are learning the same material, use them as a companion to the original lessons and not as a replacement.

## Terms to know from the start

These terms apply to every lesson, so they are listed here instead of in a single notebook.

### CRUD

**CRUD** stands for the four basic things a program can do with stored data:

| Letter | Action | What it means | Example |
|---|---|---|---|
| **C** | Create | Add new data | Sign up for a new account |
| **R** | Read | Look at existing data | View your profile |
| **U** | Update | Change existing data | Edit your username |
| **D** | Delete | Remove data | Delete your account |

Most apps are built around these four actions, so the term comes up often in software engineering.

## Notebooks

### The Marcy Lab School GitBook

Numbered to match the module and lesson (`0.1` is Mod 0, Lesson 1).

| Notebook | Topic |
|---|---|
| [0.1_command_line_interface_cli.ipynb](0.1_command_line_interface_cli.ipynb) | Terminal, shell, and CLI basics: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `echo`, `cat`, `rm`, `mv`, `cp` |
| [0.2_git_and_github.ipynb](0.2_git_and_github.ipynb) | What Git and GitHub are, the working directory / staging area / repository workflow, `add`, `commit`, `push`, `pull`, `clone` |
| [0.4_git_branching.ipynb](0.4_git_branching.ipynb) | Feature branches, switching and merging, pull requests, deleting branches |
| [1.1_intro_to_programming.ipynb](1.1_intro_to_programming.ipynb) | Programs, comments, expressions vs statements, `print()`, f-strings, control flow, code style |
| [1.2_data_types_variables_and_operators.ipynb](1.2_data_types_variables_and_operators.ipynb) | Data types, operators and order of precedence, variables and naming, arithmetic, comparison, logical, membership, identity, and assignment operators, the conditional expression |
| [1.3_functions.ipynb](1.3_functions.ipynb) | `print()`, DRY, defining and invoking functions, docstrings, parameters and arguments, `return` vs `print()`, default values and keyword arguments, `*args` and `**kwargs`, local scope and `global`, the `player_damage` example |
| [1.4_conditional_statements.ipynb](1.4_conditional_statements.ipynb) | `if` / `elif` / `else`, why order matters, narrow vs broad conditions, only-`if` chains, guard clauses, truthy and falsy values, conditional expressions |
| [1.5_strings_inputs_and_outputs.ipynb](1.5_strings_inputs_and_outputs.ipynb) | Strings and escape characters, `input()`, cleaning, validating, and parsing input, type casting, indexing and slicing, `find()` and `split()`, printing with `sep` and `end`, f-strings and number formatting, the Madlib challenge |
| [1.6_loops.ipynb](1.6_loops.ipynb) | Iteration, `for` loops over strings, `range()`, and lists, `sum()`, `.append()` and the build-a-list pattern, converting with `int()`, list comprehensions, `while` loops, validating input in a loop, `break` and `continue`, the coin-flip and guessing-game challenges |

### freeCodeCamp

Prefixed with `fc_`.

| Notebook | Topic |
|---|---|
| [fc_understanding_variables_and_data_types.ipynb](fc_understanding_variables_and_data_types.ipynb) | Variables, naming rules, comments, integers, floats, strings, booleans, `type()` and `isinstance()` |
| [fc_introduction_to_strings.ipynb](fc_introduction_to_strings.ipynb) | Quotes and escaping, the `in` operator, indexing, immutability, concatenation and `+=`, f-strings, slicing, and 14 string methods |
| [fc_build_an_employee_profile_validator.ipynb](fc_build_an_employee_profile_validator.ipynb) | Workshop: validating and cleaning employee data with `.find()`, slicing, `in`, `.strip()`, `.title()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, `.join()`, `.startswith()`, `.endswith()`, `.count()` |

### Practice programs

Challenge solutions written as regular Python files. Run them from the terminal with `python3`, for example `python3 guessing_game.py`.

| File | From | What it does |
|---|---|---|
| [madlib-challenge/main.py](madlib-challenge/main.py) | 1.5 Strings, Inputs and Outputs | A madlib story built from the user's answers, with the name, "a"/"an", and plurals fixed up using string methods |
| [guessing_game.py](guessing_game.py) | 1.6 Loops | Guess a secret number from 1 to 10 in 5 tries, with input validation and `exit` to quit |

### Reference

| Notebook | Topic |
|---|---|
| [markdown_cheat_sheet.ipynb](markdown_cheat_sheet.ipynb) | The Markdown used to write these notes: headings, tables, code blocks, lists, and callouts |

## How the notebooks are laid out

Every notebook follows the same pattern:

1. A title and a contents list
2. A key terms table
3. One section per concept: a short explanation in a Markdown cell, then a code cell with a runnable example
4. A quick reference table at the end

## Using these notes

### View a notebook

Click any notebook in the tables above. GitHub shows it in your browser with the explanations, code, and outputs. You do not need to install anything or have an account to read them.

### Get your own copy to edit

You cannot change the notebooks in this repository, but you can make your own copy and edit that as much as you like.

**1. Fork the repository.** At the top right of this page, click **Fork**, then **Create fork**. This makes a copy under your own GitHub account. You need a free GitHub account for this step.

**2. Clone your fork to your computer.** On your fork's page, click the green **Code** button and copy the URL. Then open a terminal (the **Terminal** app on a Mac, or your **WSL** terminal, such as Ubuntu, on Windows) and run:

```bash
git clone https://github.com/YOUR-USERNAME/Xavinyc-Dev-Jupyter-Notebooks.git
cd Xavinyc-Dev-Jupyter-Notebooks
```

Replace `YOUR-USERNAME` with your GitHub username. You need [Git](https://git-scm.com/downloads) installed.

New to the terminal or to Git? The [0.1_command_line_interface_cli.ipynb](0.1_command_line_interface_cli.ipynb) and [0.2_git_and_github.ipynb](0.2_git_and_github.ipynb) notebooks in this repository cover the basics, and you can read them on GitHub before installing anything.

**3. Set up your editor.** Install:

- [Python 3](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- The **Python** and **Jupyter** extensions for VS Code (open the Extensions panel, search for each, and click Install)

**4. Open and run a notebook.** In VS Code, choose **File > Open Folder** and pick the `Xavinyc-Dev-Jupyter-Notebooks` folder. Click a `.ipynb` file to open it. The first time, click **Select Kernel** at the top right and choose your Python 3. Then click **Run All** to run every code cell.

The first time you run a cell, VS Code may ask to install a package called `ipykernel`. Click **Install**. It is the piece that lets VS Code run notebook code, and it only needs installing once.

**5. Edit it.**

- Double-click a Markdown cell to edit the notes, then press `Shift+Enter` to render it.
- Click a code cell to change the code, then press `Shift+Enter` to run it.
- Hover between two cells and click **+ Code** or **+ Markdown** to add a new one.

The [markdown_cheat_sheet.ipynb](markdown_cheat_sheet.ipynb) notebook explains the formatting used in the notes.

**6. Save your changes to your fork.**

```bash
git add -A
git commit -m "Describe what you changed"
git push
```

Your changes go to your own copy on GitHub. This repository is not affected.

### Other ways to run Jupyter notebooks

VS Code is what I use, but it is not the only option. Pick whichever suits you.

**Jupyter in the browser, started from the terminal.** This is the classic way. With Python 3 installed, run:

```bash
python3 -m pip install notebook
```

Then, from inside the `Xavinyc-Dev-Jupyter-Notebooks` folder:

```bash
jupyter notebook
```

A page opens in your web browser listing the notebooks. Click one to open it. To stop Jupyter, go back to the terminal and press `Control + C`.

**JupyterLab.** A newer version of the same thing, with tabs and a file browser:

```bash
python3 -m pip install jupyterlab
jupyter lab
```

**Google Colab.** Nothing to install. Go to [colab.research.google.com](https://colab.research.google.com/), choose **File > Upload notebook**, and pick a `.ipynb` file. You need a Google account.

| Option | Install needed | Good for |
|---|---|---|
| VS Code + Jupyter extension | Python, VS Code, two extensions | Editing notebooks next to your other code |
| Jupyter Notebook | Python, then `pip install notebook` | A simple, classic notebook in the browser |
| JupyterLab | Python, then `pip install jupyterlab` | Working with several notebooks at once |
| Google Colab | Nothing | Trying a notebook quickly, or a computer you cannot install on |

If `pip install` gives an "externally-managed-environment" error, create a virtual environment first and install inside it:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install notebook
```

On Windows with WSL, all of these commands are the same as on a Mac, including `python3` and `source .venv/bin/activate`. Only Windows without WSL is different: there the commands are `python` and `.venv\Scripts\activate`.

### Just want one notebook?

Open the notebook on GitHub and click the **Download raw file** button at the top right of the file. Open the downloaded `.ipynb` file with any of the options above.

### How I study from them

- **Before a session:** open the previous notebook, cover the outputs and comments, and predict what each code cell prints.
- **Once a week:** skim the quick reference tables and redo anything I blanked on.
- **Before an assessment:** explain each key term out loud before reading my definition.

## Notes

- These notes are for studying and educational purposes only.
- Lesson material belongs to The Marcy Lab School and freeCodeCamp, as credited under Sources. Some of it appears here word for word.
- Some notebooks were written or reviewed with help from an AI assistant.
