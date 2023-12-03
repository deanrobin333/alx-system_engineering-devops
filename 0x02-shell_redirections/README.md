# Project 
## **0x02. Shell, I/O Redirections and filters**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. Hello World](#0)
	- [1. Confused smiley](#1)
	- [2. Let's display a file](#2)
	- [3. What about 2?](#3)
	- [4. Last lines of a file](#4)
	- [5. I'd prefer the first ones actually](#5)
	- [6. Line #2](#6)
	- [7. It is a good file that cuts iron without making a noise](#7)
	- [8. Save current state of directory](#8)
	- [9. Duplicate last line](#9)
	- [10. No more javascript](#10)
	- [11. Don't just count your directories, make your directories count](#11)
	- [12. What’s new](#12)
	- [13. Being unique is better than being perfect](#13)
	- [14. It must be in that file](#14)
	- [15. Count that word](#15)
	- [](#16)
	- [](#17)
	- [](#18)
	- [](#19)
	- [](#20)
	- [](#21)
	- [](#22)
	- [](#23)
	- [](#24)
	- [](#25)
	- [](#26)
---
## Author Details
- *Dean Robin Otsyeno - deanrobin777@gmail.com*

## Project Description
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable
- You are not allowed to use `sed` or `awk`
- Read your `/etc/passwd` and `/etc/shadow` files.

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. Hello World**
- Write a script that prints “Hello, World”, followed by a new line to the standard output.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `0-hello_world`
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Confused smiley**
- Write a script that displays a confused smiley `"(Ôo)'`.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `1-confused_smiley`
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Let's display a file**
- Display the content of the `/etc/passwd` file.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `2-hellofile`
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. What about 2?**
- Display the content of `/etc/passwd` and `/etc/hosts`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `3-twofiles`
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Last lines of a file**
- Display the last 10 lines of `/etc/passwd`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `4-lastlines`
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. I'd prefer the first ones actually**
- Display the first 10 lines of `/etc/passwd`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `5-firstlines`
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Line #2**
- Write a script that displays the third line of the file `iacta`.
    - The file `iacta` will be in the working directory
    - You’re not allowed to use `sed`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `6-third_line`
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. It is a good file that cuts iron without making a noise**
- Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `7-file`
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Save current state of directory**
- Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `8-cwd_state`
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Duplicate last line**
- Write a script that duplicates the last line of the file `iacta`
    - The file `iacta` will be in the working directory

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `9-duplicate_last_line`
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. No more javascript**
- Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `10-no_more_js`
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Don't just count your directories, make your directories count**
- Write a script that counts the number of directories and sub-directories in the current directory.
	- The current and parent directories should not be taken into account
	- Hidden directories should be counted


<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `11-directories`
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. What’s new**
- Create a script that displays the 10 newest files in the current directory.
- Requirements:
	- One file per line
	- Sorted from the newest to the oldest

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `12-newest_files`
---
#### 13
###### [Table of Contents](#table-of-contents)
**13. Being unique is better than being perfect**
- Create a script that takes a list of words as input and prints only words that appear exactly once.
    - Input format: One line, one word
    - Output format: One line, one word
    - Words should be sorted

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `13-unique`
---
#### 14
###### [Table of Contents](#table-of-contents)
**14. It must be in that file**
- Display lines containing the pattern “root” from the file `/etc/passwd`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `14-findthatword`
---
#### 15
###### [Table of Contents](#table-of-contents)
**15. Count that word**
- Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: `15-countthatword`
---
#### 16
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 17
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 18
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 19
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 20
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 21
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 22
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 23
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 24
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 25
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---
#### 26
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x02-shell_redirections`
    - File: ``
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
