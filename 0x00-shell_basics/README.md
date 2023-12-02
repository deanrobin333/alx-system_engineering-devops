# Project 
## **0x00. Shell, basics**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Where am I?](#0)
	- [1. What’s in there?](#1)
	- [2. There is no place like home](#2)
	- [3. The long format](#3)
	- [4. Hidden files](#4)
	- [5. I love numbers](#5)
	- [6. Welcome](#6)
	- [7. Betty in my first directory](#7)
	- [8. Bye bye Betty](#8)
	- [9. Bye bye My first directory](#9)
	- [10. Back to the future](#10)
	- [11. Lists](#11)
	- [12. File type](#12)
	- [13. We are symbols, and inhabit symbols](#13)
	- [14. Copy HTML files](#14)
	- [15. Let’s move](#15)
	- [16. Clean Emacs](#16)
	- [](#17)
	- [](#18)
	- [](#19)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of *this* project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we’ll learn more about how to utilize this command.

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. Where am I?**
- Write a script that prints the absolute path name of the current working directory.
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `0-current_working_directory`
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. What’s in there?**
- Display the contents list of your current directory.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `1-listit`

---
#### 2
###### [Table of Contents](#table-of-contents)
**2. There is no place like home**
- Write a script that changes the working directory to the user’s home directory.
	- You are not allowed to use any shell variables

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `2-bring_me_home`
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. The long format**
- Display current directory contents in a long format

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `3-listfiles`
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Hidden files**
- Display current directory contents, including hidden files (starting with .). Use the long format.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `4-listmorefiles`

---
#### 5
###### [Table of Contents](#table-of-contents)
**5. I love numbers**
- Display current directory contents.
	- Long format
	- with user and group IDs displayed numerically
	- And hidden files (starting with .)

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `5-listfilesdigitonly`
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Welcome**
- Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `6-firstdirectory`
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Betty in my first directory**
- Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `7-movethatfile`
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Bye bye Betty**
- Delete the file `betty`.
	- The file `betty` is in `/tmp/my_first_directory`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `8-firstdelete`
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Bye bye My first directory**
- Delete the directory `my_first_directory` that is in the `/tmp` directory.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `9-firstdirdeletion`
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Back to the future**
- Write a script that changes the working directory to the previous one.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `10-back`
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Lists**
- Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `11-lists`
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. File type**
- Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `12-file_type`
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. We are symbols, and inhabit symbols**
- Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `13-symbolic_link`
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. Copy HTML files**
- Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
- You can consider that all HTML files have the extension `.html`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `14-copy_html`
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. Let’s move**
- Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- You can assume that the directory `/tmp/u` will exist when we will run your script

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `100-lets_move`
---
#### 16
###### [Table of Contents](#table-of-contents)
**16. Clean Emacs**
- Create a script that deletes all files in the current working directory that end with the character `~`.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x00-shell_basics`
    - File: `101-clean_emacs`
---
#### 17
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 18
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 19
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---

<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
