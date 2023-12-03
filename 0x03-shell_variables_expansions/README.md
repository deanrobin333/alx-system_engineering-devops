# Project 
## **0x03. Shell, init files, variables and expansions**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. <o>](#0)
	- [1. Hello you](#1)
	- [2. The path to success is to take massive, determined action](#2)
	- [3. If the path be beautiful, let us not ask where it leads](#3)
	- [4. Global variables](#4)
	- [5. Local variables](#5)
	- [6. Local variable](#6)
	- [7. Global variable](#7)
	- [8. Every addition to true knowledge is an addition to human power](#8)
	- [9. Divide and rule](#9)
	- [10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](#10)
	- [11. There are 10 types of people in the world -- Those who understand binary, and those who don't](#11)
	- [12. Combination](#12)
	- [](#13)
	- [](#14)
	- [](#15)
	- [](#16)
	- [](#17)
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
- You are not allowed to use `&&`, `||` or `;`
- You are not allowed to use `bc`, `sed` or `awk`
- All your files must be executable
- Read your `/etc/profile`, `/etc/inputrc` and `~/.bashrc` files.    
 - Look at some files in the `/etc/profile.d` directory.

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. <o>**
- Create a script that creates an alias.
    - Name: `ls`
    - Value: `rm *`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `0-alias`
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Hello you**
- Create a script that prints `hello user`, where user is the current Linux user.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `1-hello_you`
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. The path to success is to take massive, determined action**
- Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `2-path`
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. If the path be beautiful, let us not ask where it leads**
- Create a script that counts the number of directories in the `PATH`.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `3-paths`
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Global variables**
- Create a script that lists environment variables.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `4-global_variables`
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Local variables**
- Create a script that lists all local variables and environment variables, and functions.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `5-local_variables`
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Local variable**
- Create a script that creates a new local variable.
    - Name: `BEST`
    - Value: `School`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `6-create_local_variable`
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Global variable**
- Create a script that creates a new global variable.    
    - Name: `BEST`
    - Value: `School`

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `7-create_global_variable`
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. Every addition to true knowledge is an addition to human power**
- Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `8-true_knowledge`
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. Divide and rule**
- Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
    - `POWER` and `DIVIDE` are environment variables

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `9-divide_and_rule`
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath**
- Write a script that displays the result of `BREATH` to the power `LOVE`
    - `BREATH` and `LOVE` are environment variables
    - The script should display the result, followed by a new line

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `10-love_exponent_breath`
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. There are 10 types of people in the world -- Those who understand binary, and those who don't**
- Write a script that converts a number from base 2 to base 10.
    - The number in base 2 is stored in the environment variable `BINARY`
    - The script should display the number in base 10, followed by a new line

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `11-binary_to_decimal`
---
#### 12
###### [Table of Contents](#table-of-contents)
**12. Combination**
- Create a script that prints all possible combinations of two letters, except `oo`.
    - Letters are lower cases, from `a` to `z`
    - One combination per line
    - The output should be alpha ordered, starting with `aa`
    - Do not print `oo`
    - Your script file should contain maximum 64 characters

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: `12-combinations`
---
#### 13
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: ``
---
#### 14
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: ``
---
#### 15
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: ``
---
#### 16
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: ``
---
#### 17
###### [Table of Contents](#table-of-contents)
**t**

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x03-shell_variables_expansions`
    - File: ``
---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
