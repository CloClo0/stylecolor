# Stylecolor - 1.0.0

## Stylecolor
`stylecolor` is the simplest package for coloring and/or styling text in the terminal.  
`stylecolor` requires no other modules and is very lightweight and efficient.  

## Installation
No prerequisites are needed, only stylecolor.
```bash
pip install stylecolor
```

## Description
`stylecolor` uses [ANSI escape codes](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797) to work. It is therefore compatible with all other libraries that use ANSI codes.

Some terminals do not support ANSI escape codes, so you can disable styling with `deactivate()`. In this case, you will still be able to use the functions, but the various styles will no longer be applied.  
Use `reactivate()` to reactivate the styling.

I recommend importing `stylecolor` as `sc` or `st`.\
Additionally, if you are debugging, I suggest importing the `rprint()` function like this: `from stylecolor import rprint()`

More, source code is available on [Stylecolor's](https://github.com/CloClo0/stylecolor) GitHub page


## Coloring
8 colors are available natively: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, and `white`.  
For each color, there are functions (e.g. `stylecolor.red()`), as well as constants (e.g. `stylecolor.RED`).  
For other colors, use [`stylecolor.rgb()`](#custom-colors) or [`stylecolor.hexa()`](#custom-colors).

### Simple Colors

```python
import stylecolor as sc

print(sc.red('red text'))
print(sc.green_text('green text'))
print(sc.blue('blue text'))
# ...
# AND/OR
print(sc.RED + 'constant red text' + sc.RESET)
print(sc.GREEN + 'constant green text' + sc.RESET)
print(sc.BLUE + 'constant blue text' + sc.RESET)
# ...
```
**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/simple_colors.png" width="180"/>

### Light Colors
You can add the prefix `l` in front of the color to make it a `light` version.

````python
import stylecolor as sc
print(sc.lred('light red'))
print(sc.lgreen('light green'))
print(sc.lblue('light blue'))
# ...
# AND/OR
print(sc.LRED + 'constant red text' + sc.RESET)
print(sc.LGREEN + 'constant green text' + sc.RESET)
print(sc.LBLUE + 'constant blue text' + sc.RESET)
# ...
````
**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/light_colors.png" width=180/>

### Background Colors
You can add the prefix `b` in front of each color to set it as a background color.

```python
import stylecolor as sc
print(sc.bred('red background'))
print(sc.bgreen('green background'))
print(sc.bblue('blue background'))
# ...
# AND/OR
print(sc.BRED + 'constant red background' + sc.RESET)
print(sc.BGREEN + 'constant green background' + sc.RESET)
print(sc.BBLUE + 'constant blue background' + sc.RESET)
# ...
```

**output**\
<img src='https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/background_colors.png' width=250>

>**NOTE**\
> You can also add `b` in front of the `light` colors.
> 
> ```python
> import stylecolor as sc
> print(sc.blred('light red background'))
> print(sc.blgreen('light green background'))
> print(sc.blblue('light blue background'))
> # ...
> #AND/OR"
> print(sc.BLRED + 'constant light red background' + sc.RESET)
> print(sc.BLGREEN + 'constant light green background' + sc.RESET)
> print(sc.BLBLUE + 'constant light blue background' + sc.RESET)
> # ...
> ```
> 
> **output**\
> <img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/light_background_colors.png" width='250' />

### Custom Colors
The `rgb()` and `hexa()` functions allow you to apply custom colors.

```python
import stylecolor as sc
print(sc.rgb('personalised rgb color', '(background)', r=250, g=150, b=0))
print(sc.rgb('personalised tuple rgb color', '(background)', rgb=(250, 150, 0)))
print(sc.hexa('personalised hexadecimal color', '(background)', hexa='#fA9600'))
print(sc.hexa('personalised background hexadecimal color', "without '#'", hexa='Fa9600'))
``` 

**output**\
<img src='https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/custom_colors.png' width=450>

### Custom Background Colors
The `brgb()` and `bhexa()` functions allow you to apply custom background colors.

````python
import stylecolor as sc
print(sc.brgb('personalised rgb color', '(background)', r=250, g=150, b=0))
print(sc.brgb('personalised tuple rgb color', '(background)', rgb=(250, 150, 0)))
print(sc.bhexa('personalised hexadecimal color', '(background)', hexa='#fA9600'))
print(sc.bhexa('personalised background hexadecimal color', "without '#'", hexa='Fa9600'))
````

**output**\
<img src='https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/custom_background_color.png' width=450>

### Reset Colors
The functions `stylecolor.rcolor()` or `stylecolor.RCOLOR` and `stylecolor.rbackground()` or `stylecolor.RBACKGROUND` respectively remove the text color and the background color.

````python
import stylecolor as sc
# color
green_text = sc.green('green text')
print(green_text)
print(sc.rcolor(green_text))
# background color
bgreen_text = sc.bgreen('background green text')
print(bgreen_text)
print(sc.rbackground(bgreen_text))
````
**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/reset_colors.png" width=180>

## Built-in Styles

### Apply Styles
In addition to colors, many styles are available: `bold`, `dim`, `italic`, `underline`, `blinking`, `reverse`, `hidden`, and `strikethrough`.  
Just like with colors, styles are accessible via functions (e.g. `stylecolor.bold()`) or constants (e.g. `stylecolor.BOLD`).

```python
import stylecolor as sc
print(sc.bold('bold text'))
print(sc.italic('italic text'))
print(sc.underline('underline text'))
# ...
# AND/OR
print(sc.BOLD, 'constant bold text', sc.RESET, sep='')
print(sc.ITALIC, 'constant italic text', sc.RESET, sep='')
print(sc.UNDERLINE, 'constant underline text', sc.RESET, sep='')
# ...
``` 

**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/apply_styles.png" width=200>

### Reset Styles
You can add the prefix `r` in front of each style to cancel it (including with constants).

````python
import stylecolor as sc
bold = sc.bold('bold text')
print(bold)
print(sc.rbold(bold))

underline = sc.underline('underline text')
print(underline)
print(sc.runderline(underline))
# ...
````

**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/reset_styles.png" width=150>

## Other Styles
It is possible, using the functions `stylecolor.style()` and `stylecolor.styles()`, to apply one or more styles to text.  
You can use textual styles like `red`, `bred`, `underline`, or directly use ANSI codes like `31`, `41`, `4`, for example.

````python
import stylecolor as sc
def func():
    pass
print(sc.style('text1', func, 'other text', style='blue'))
print(sc.styles('unique object', 'white', 'bblack', 'underline'))
````

**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/other_styles.png" width=500>

## Composability

Most functions and constants are composable with each other.

```python
import stylecolor as sc
print(sc.blue(sc.underline('blue underline text'), 'blue text only'), 'normal text')
print(sc.styles('blue underline text', 'blue', 'underline', 'italic'))
# fonctions with constants
print(sc.green(sc.UNDERLINE, 'combined green underline text', sc.RUNDERLINE, ' green text only', sep=''),
      'normal text')
````

**output** \
<img src='https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/composability.png' width=500>

> **NOTE**\
> Foreground colors are not composable with each other, same for background.
>
>````python
>import stylecolor as sc
>print(sc.blue(sc.green('colored text in blue and green which appears blue')))
>print(sc.bblue(sc.bgreen('background colored text in blue and green which appears blue')))
>```` 
>
>**output**
><img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/non_composability.png" width=500>
## Debug Functions

The functions `raw()` and `rprint()` allow you to get the raw version of a styled text.

````python
import stylecolor as sc
colored = sc.blue("raw blue text")
raw = sc.raw(colored) # return raw string
print(raw)
sc.rprint(colored)  # directly print raw result
````
**output**\
<img src="https://raw.githubusercontent.com/CloClo0/stylecolor/main/images/debug_functions.png" width=250>
