
## Description

Vim-multisheets is a vim plugin that displays 2-dimensional slices of N-dimensional arrays. The N-dimensional array is defined by specifying values of cells pointwise or with python functions.

This readme gives details of how to use vim-multisheets; see this blog post XXX for a general description, real demonstrations, and motivation for the idea of multisheets. 

## Installation

Before installing, please read the Warning section, next. 

Use the plugin manager of your choice.

E.g. with pathogen: https://github.com/tpope/vim-pathogen
Clone this directory into your ```bundle/``` directory, maybe in ```~/.config/nvim/bundle/```:
```git clone https://github.com/tsvibt/vim-multisheets```

## Warning

I don't know about best practices for writing plugins for other people to use, so this code does not follow usual safety / modularity practices. In particular:

* The plugin generally isn't "sealed", e.g. vim and python variables might be clobbered and autocommands might be triggered.
* If the main function, MSViewSheet, is called in a file starting with "ms-", vim-multisheets will be loaded and will create a number of directories. It will also overwrite a file in ```sheets/```. So don't run commands from vim-multisheets in a random directory. 
* vim-multisheets looks for python code in certain files (e.g. anything in ```propositions/yourfunctionname/```), and runs it using ```exec()```. So viewing a multisheet should be treated not like reading a file but rather like running code in terms of safety and security. 


## Dependencies

Tested only with:

NVIM v0.6.1

Python 3.9.10

Pathogen 2.4

I'm not sure what other dependencies there are; hopefully you can get it working by ```pip3 install```-ing python dependencies by looking at error messages, e.g. the package ```tabulate```.

## Use

I recommend only using multisheets in a dedicated directory without other files, because multisheets will create directories and will overwrite files in ```sheets/```, as well as move files in ```propositions/``` and create various files.

Recommended use:

0. For convenience, set up keymaps for the main commands; see below, "Conditional keymaps".
1. Make a directory, e.g. ```mkdir multisheets```.
3. To make a multisheet named ```sheetname```, edit with vim a file that starts with "ms-": ```nvim ms-sheetname```
4. Put type names on second line; types can't contain white space. Optionally put argument names on first line (these don't do anything but will be formated above the type names in the sheet). Optionally describe the meaning of the sheet in the lines after line 2.

E.g.: 
```
start-thing end-thing pathway
Thing Thing PathType

is there a path from start-thing to end-thing that has type pathway?
```

5. Populate types by editing files like ```type-Typename```, e.g. ```type-Thing```. For any line that starts with ". ", the remainder of that line is taken as an instance of that type. For convienience, ```MSEnterFile``` with the cursor over a type name ```Typename```, either in ```ms-sheetname``` or in ```sheets/sheetname```, will open ```type-Typename```.

E.g. in ```type-Thing```:

```
. thing1
this thing is big and green
. thing2
. thing3
this thing is good
. thing444
```

And in ```type-PathType```:

```
. long
. crowded
has at least 500 other travelers
. slippery
```

6. Call MSViewSheet. This initializes the values of the arguments (i.e. positions on each axis) with the first value of that type (X, if no values are given). No table is shown because there aren't two variable axes. The first line is the names of the axes, the second line is the types, the third line is the currently selected values of the arguments. 


![](https://github.com/tsvibt/vim-multisheets/blob/main/screenshots/multisheets-example-init.png)
![](https://github.com/tsvibt/vim-multisheets/blob/main/screenshots/multisheets-example-no-table.png)

7. Set one argument to X and another to Y, either by editing the text or by calling MSCycleArg with the cursor over an argument. A table should display:

![](https://github.com/tsvibt/vim-multisheets/blob/main/screenshots/multisheets-example-XY.png)

Now the table is set up. The basic usage is adding "propositions", i.e. files like ```propositions/sheetname/msprop-examplepropname.py``` and refreshing the sheet with MSViewSheet. A proposition gives a condition that specifies which cells it applies to, and specifies the values on those cells. (These "propositions" aren't expressions in any formal language, they're just functions. So they're easy to write, but are not constrained to make sense or be true or relate to other "propositions", and it's up to you to write "propositions" that do the right thing. Direct contradictions, though, are displayed as ```>X<```.)

To edit the value at one cell, go to that cell and call MSEnterFile. This creates a proposition file and puts the condition for that specific cell (just a list of the values of the arguments for that cell). Then put a line after the """ that starts with ". "; the remainder of that line is the value of that cell. See Formats for how to use python functions in propositions.

There's a full example in ```vim-multisheets/example/```. Note: the math in the example is not done very carefully and likely contains errors. Also note that, as mentioned in the Warnings section above, viewing a multisheet executes python code in the multisheet's directory, and so should be treated like code in terms of safety and security.

### List of commands

```:MSEnterFile```

Opens a file relevant to the cursor position. Cursor on...
* The name of the multisheet at the start of line 1: opens the sheet definition file, ```ms-sheetname```.
* The name of a type in line 2: opens the definition of that type, ```type-Typename```.
* A cell in the sheet: if propositions match the arguments at that cell, those files are opened. Otherwise, a new proposition file is created with a condition matching those arguments.

```:MSViewSheet```

If in a sheet definition file or a sheet file, recomputes the sheet and edits the sheet file.

```:MSViewSheetReinit```

Like MSViewSheet, but resets the arguments.

```:MSCycleArg 1```
```:MSCycleArg -1```

Whichever argument is vertically over the cursor, cycles that argument through its values plus X and Y.


```:MSCycleProp 1```
```:MSCycleProp -1```

If in a proposition file, edits the next/previous proposition file (for the same sheet).

```:MSRenameProp```

If in a proposition file, reads the line under the cursor, and if there's no proposition with that name, moves the current proposition file to that name.

### Conditional keymaps

I recommend mapping vim-multisheets functions to convenient keys, conditionally on being in a directory where you want to use vim-multisheets. It's made with keymaps in mind, not ex commands.

E.g., put something like this in your (n)vimrc:

```vim
if index(['~/multisheets', '~/multisheets-sandbox'], getcwd())>= 0
   :nnoremap <Enter> :MSEnterFile<CR>

   :nnoremap <leader>f :MSViewSheet<CR>
   :nnoremap <leader>F :MSViewSheetReinit<CR>

   :nnoremap <leader>m :MSCycleArg 1<CR>
   :nnoremap <leader>M :MSCycleArg -1<CR>

   :nnoremap <leader>l :MSCycleProp 1<CR>
   :nnoremap <leader>L :MSCycleProp -1<CR>

   :nnoremap <leader>p :MSRenameProp<CR>
endif
```
(This isn't what I use, I use various Alt+[some key].)


### Formats

Sheet definition: A sheet definition file's name starts with ```ms-```, and its second line is a space-separated list of names of types. Optionally its first line is a space-separated list of names of arguments, and lines after line 2 can be anything.

Type definition: A type definition file's name starts with ```type-```. For any line that starts with ". ", the remainder of that line is taken as an instance of that type.

Utilities: the file ```utilities/sheetname.py``` is initialized empty, and sourced. This is for code shared between propositions, e.g. my multisheet about groups has

```python
GSubscriptDigits = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', ]

def isCyclic(x):
   return len(x) == 2 and x[0] == 'ℤ' and x[1] in GSubscriptDigits
```

in ```utilities/groupmaps.py``` because many propositions want to detect whether an argument looks like a cyclic group (of order <10 due to laziness).

Propositions: 

A proposition file is in ```propositions/sheetname/``` and its name starts with ```msprop-```. A proposition is split by """. (The point of this is to get syntax highlighting for python code.)

The first split is the condition. It can either be a python function, or it can be one or more lists, one per line, of argument values. If it's a python function, the proposition applies to cells that this function returns ```True``` on. If it's argument lists, it applies if any list matches the arguments. A list matches if each position matches. A position is either a string (matches if it's identical to the argument) or a list; a list matches any of its elements, unless its first element is '!', in which case it matches any argument that's not an element. E.g.

```['thing3', ['thing1', 'thing2'], ['!', 'long']]```

matches argument values with ```thing3``` first, either ```thing1``` or ```thing2``` second, and any PathType other than ```long```.

The last split can be text. If it contains a line starting with ". ", the remainder is interpreted as the conclusion of the proposition. E.g. in ```propositions/groupmaps/msprop-ℤ₂²-cyclic.py```:

```python
def fun(args):
   return args[0] == 'ℤ₂²' and isCyclic(args[1])  
"""
. 0
cyclic groups have at most 1 element of order 2
"""
```

(See blog post XXX for details about this math question; this question is the example in ```vim-multisheets/example/```.)

If there are >2 splits, the penultimate one is interpreted as a python function giving the result of the proposition. E.g.:

```python
def fun(args):
   return isCyclic(args[0]) and isCyclic(args[1]) and args[2] == '{id}'
""" """
def fun(args):
   n=GSubscriptDigits.index(args[0][1])
   m=GSubscriptDigits.index(args[1][1])
   if m%n != 0:
      return 0
   else:
      return totient(n)
"""
ℤ𝘯 ℤ𝑚 {id}
if not n || m , none. if yes, then, it's the number of guys k relatively 
prime to n; then take the generator to r^km/n
"""
```

This asserts that the number of embeddings of the cyclic group ℤ𝘯 into ℤ𝑚 is 0 or totient(n). This proposition produces part of the leftmost column in this table:

![](https://github.com/tsvibt/vim-multisheets/blob/main/screenshots/multisheets-groups-Z2-table.png)

The following proposition shows the union of two rectangular match conditions, used to state that D₂ is an alias of ℤ₂²:

```python
['X', 'D₂', 'X']
['D₂', 'X', 'X']
""" """
def fun(args):
   if args[0] == 'D₂':
      args[0] = 'ℤ₂²'
   if args[1] == 'D₂':
      args[1] = 'ℤ₂²'
   return Args_LookupValue(args)
""" 
D₂=ℤ₂²
D₂ is another name for ℤ₂²
""" 
```

Lookups: To look up the value at some cell, just pass the argument values for that cell to ```Args_LookupValue()```. E.g.:

![](https://github.com/tsvibt/vim-multisheets/blob/main/screenshots/multisheets-groups-lookup-example.png)

This asserts that if there's only 0 or 1 embeddings from a group to another, then there's also that same number of embeddings up to conjugation (inner automorphism of the target group). This proposition produces part of the second-leftmost column in the above table. (Note that putting """ """ between the condition and the result code, lets the result code get python syntax highlighting.)

Instances: To get a list of the possible values of a type ```Typename``` (i.e., the things written in ```type-Typename``` after ". "), call ```Instances('Typename')```. E.g.: 

```python
def fun(args):
   return args[2] == 'inner' and args[1] in Instances('AbelianGroup')
"""
"""
def fun(args):
   args[2] = '{id}'
   return Args_LookupValue(args)
"""
if the target is abelian, conjugation doesn't do anything, so there's 
only the trivial inner automorphism, and no embeddings are made equivalent.
"""
```

### What MSViewSheet does

When MSViewSheet is called: read the types from the sheet definition file. Read arguments from the sheet file. Load utilities. For each choice of the X and Y from their respective types (read from the type definition files), try to apply each proposition to that full selection of arguments. If the proposition's condition matches those arguments, compute the result of the proposition. If all the propositions return nothing or '??', return '??'; if all the non-'??' results are the same for a given cell, return that result; if there are multiple different results, return '>X<', indicating a contradiction.

To let a proposition lookup values, just evaluate again at the arguments they pass. (This uses a bit of metaprogramming to pass the compiled propositions, avoiding having to recompile the propositions many times.) Note that this means you can make an infinite loop, e.g. by having a proposition with a match function that looks up the value at whatever cell is passed to it. This causes python to crash with too big a stack, harmlessly I think. (Results could instead be computed using a fixed-point scheme, tracking which values have been updated and recomputing propositions that looked up those values. That would allow circular dependencies, which would be nice in contexts where propositions are more like constraints and less like functions. I implemented this because circular references would be better and because I thought it'd be faster, but it turned out to be considerably slower, and it was a kind of messy and complicated, so I shelved it.)

## License

Copyright 2022 Tsvi Benson-Tilsen

Licensed under the GNU General Public License. 

See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt




