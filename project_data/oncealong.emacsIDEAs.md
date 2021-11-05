emacsIDEAs
==========

Porting some great extensions of emacs to Intellij IDEA. 
Such as AceJump, CopyWithoutSelection, 
And new created EditWithoutSelection (Cut/Move/Replace without selection). 

plugin page: http://plugins.jetbrains.com/plugin/?idea_ce&pluginId=7163


---

![usage sample](https://plugins.jetbrains.com/files/7163/screenshot_16138.png)


---
```
AceJump

C-L 't' 'm' : Basic Word Jump | Type C-L, then type target char (eg. 't') to jump to, then type marker char (eg. 'm') to move caret.
C-J 't' 'm' : Basic Char Jump
```
![basic word jump gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/1_basic_word_jump.gif?raw=true)


```
AceJump, jump to special place

C-L ' ' 'm' : Jump to line end or start. | To show marker on line end and line start, type space ' ' as target char
C-L ',' 'm' : Jump to symbol key | Show markers on .{}(|`/\;.{}()[]?_=-+'"!@#$%^&*)_=
```

---
```
Copy without selection:

C-c w : Copy word
C-c s : Copy string, begin and end by whitespaces
C-c l : Copy line
C-c b : Copy block between balanced { and }
C-c q : Copy quoted, such as abcd in "abcd"
C-c a : Copy to line beginning
C-c A : Copy to file beginning
C-c e : Copy to line end
C-c E : Copy to file end
C-c p : Copy paragraph
C-c g : Copy paragraph group (e.g.: entire function including white lines)
C-c u : Copy to paragraph begining
C-c d : Copy to paragraph end
```
![Copy without selection gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/2_copy_without_selection.gif?raw=true)


```
Cut without selection:

C-c ' ' (w | s | l | q | a | A | e | E | p | g | u | d | b) : Type one space to cut related area
```



```
Selection:

C-c ' ' ' ' (w | s | l | q | a | A | e | E | p | g | u | d | b) : Type two space to select related area
```


---
```
Replace target (word | line | paragraph) with text at current caret:
*Tips: Consider i in C-i means "input to target" or "replace into" or "invade". *

C-i C-w 't' 'm' : replace target word                 | C-i C-w means type C-i then continue type C-w
C-i C-s 't' 'm' : replace target string
C-i C-l 't' 'm' : replace target line
C-i C-b 't' 'm' : replace target block
C-i C-q 't' 'm' : replace target quote
C-i C-a 't' 'm' : replace target to line begining
C-i C-e 't' 'm' : replace target char to line end
C-i C-p 't' 'm' : replace target paragraph
C-i C-g 't' 'm' : replace target paragraph group
C-i C-u 't' 'm' : replace target to paragraph beginning
C-i C-d 't' 'm' : replace target to paragraph end
```
![Replace target range gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/3_replace_target_range.gif?raw=true)

---
```
Obtain target (word | line | paragraph), then replace text at current caret:
*Tips: Consider o in C-o means "output from target" or "obtain from target". *

C-o C-w 't' 'm' : obtain target word, then replace current word
C-o C-s 't' 'm' : obtain target string, then replace current string
C-o C-l 't' 'm' : obtain target line, then replace current line
C-o C-b 't' 'm' : obtain target block
C-o C-q 't' 'm' : obtain target quote
C-o C-a 't' 'm' : obtain target to line beginning
C-o C-e 't' 'm' : obtain target char to line end
C-o C-p 't' 'm' : obtain target paragraph
C-o C-g 't' 'm' : obtain target paragraph group
C-o C-u 't' 'm' : obtain target to paragraph beginning
C-o C-d 't' 'm' : obtain target to paragraph end
```
![Obtain target range gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/4_obtain_target_range.gif?raw=true)

---
```
Copy target (word | line | paragraph), then insert text at current caret:
*Tips: Consider w in C-w  follows emacs' command "Alt-w" as copy, or "with target". *

C-w C-w 't' 'm' : Copy target word, then insert at current caret
C-w C-s 't' 'm' : Copy target string, then insert at current caret
C-w C-l 't' 'm' : Copy target line, then insert at current caret
C-w C-b 't' 'm' : Copy target block
C-w C-q 't' 'm' : Copy target quote
C-w C-a 't' 'm' : Copy target to line beginning
C-w C-e 't' 'm' : Copy target char to line end
C-w C-p 't' 'm' : Copy target paragraph
C-w C-g 't' 'm' : Copy target paragraph group
C-w C-u 't' 'm' : Copy target to paragraph beginning
C-w C-d 't' 'm' : Copy target to paragraph end
```
![Copy target range gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/5_copy_target_range.gif?raw=true)


---
```
Cut target (word | line | paragraph), then insert text at current caret:

C-x C-w 't' 'm' : Cut target word, then insert at current caret
C-x C-s 't' 'm' : Cut target string, then insert at current caret
C-x C-l 't' 'm' : Cut target line, then insert at current caret
C-x C-b 't' 'm' : Cut target block
C-x C-q 't' 'm' : Cut target quote
C-x C-a 't' 'm' : Cut target to line beginning
C-x C-e 't' 'm' : Cut target char to line end
C-x C-p 't' 'm' : Cut target paragraph
C-x C-g 't' 'm' : Cut target paragraph group
C-x C-u 't' 'm' : Cut target to paragraph beginning
C-x C-d 't' 'm' : Cut target to paragraph end
```
![Cut target range gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/6_cut_target_range.gif?raw=true)


---
```
Delete target (word | line | paragraph...)

C-d C-w 't' 'm' : delete target word
C-d C-s 't' 'm' : delete target string
C-d C-l 't' 'm' : delete target line
C-d C-b 't' 'm' : delete target block
C-d C-q 't' 'm' : delete target quote
C-d C-a 't' 'm' : delete target to line beginning
C-d C-e 't' 'm' : delete target char to line end
C-d C-p 't' 'm' : delete target paragraph
C-d C-g 't' 'm' : delete target paragraph group
C-d C-u 't' 'm' : delete target to paragraph beginning
C-d C-d 't' 'm' : delete target to paragraph end
```
![Delete target range gif](https://github.com/whunmr/emacsIDEAs/blob/master/tutorials/7_delete_target_range.gif?raw=true)


---
```
Highlight symbol:

C-, : hightlight-symbol-prev | Jump to prev occurrence of symbol that around caret
C-. : hightlight-symbol-next | Jump to next occurrence of symbol that around caret
```

---
```
Just one space:

C-M-Space : Make just one space around caret by Ctrl-Cmd-Space.
```

---
```
Separate AceJump copy,cut,select command:

C-i C-c 't' 'm' : Copy jump area
C-i C-x 't' 'm' : Cut jump area
C-i C-i 't' 'm' : Select jump area
C-i C-f 't' 'm' : Basic Jump alias
```




