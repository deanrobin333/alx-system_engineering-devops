# Project 
## **0x01. Shell, permissions**
---
## Table of Contents
- [Author Details](#author-details)
- [Project Description](#project-description)
- [Tasks](#tasks)
	- [0. My name is Betty](#0)
	- [1. Who am I](#1)
	- [2. Groups](#2)
	- [3. New owner](#3)
	- [4. Empty!](#4)
	- [5. Execute](#5)
	- [6. Multiple permissions](#6)
	- [7. Everybody!](#7)
	- [8. James Bond](#8)
	- [9. John Doe](#9)
	- [10. Look in the mirror](#10)
	- [11. Directories](#11)
	- [](#12)
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
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable

## Tasks
#### 0
###### [Table of Contents](#table-of-contents)
**0. My name is Betty**
- Create a script that switches the current user to the user `betty`.
	- You should use exactly 8 characters for your command (+1 character for the new line)
	- You can assume that the user `betty` will exist when we will run your script
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `0-iam_betty`
---
#### 1
###### [Table of Contents](#table-of-contents)
**1. Who am I**
- Write a script that prints the effective username of the current user.
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `1-who_am_i`
---
#### 2
###### [Table of Contents](#table-of-contents)
**2. Groups**
- Write a script that prints all the groups the current user is part of.
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `2-groups`
---
#### 3
###### [Table of Contents](#table-of-contents)
**3. New owner**
- Write a script that changes the owner of the file `hello` to the user `betty`.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `3-new_owner`
---
#### 4
###### [Table of Contents](#table-of-contents)
**4. Empty!**
- Write a script that creates an empty file called `hello`.
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `4-empty`
---
#### 5
###### [Table of Contents](#table-of-contents)
**5. Execute**
- Write a script that adds execute permission to the owner of the file `hello`.
	- The file `hello` will be in the working directory
<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `5-execute`
---
#### 6
###### [Table of Contents](#table-of-contents)
**6. Multiple permissions**
- Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.    
    - The file `hello` will be in the working directory

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `6-multiple_permissions`
---
#### 7
###### [Table of Contents](#table-of-contents)
**7. Everybody!**
- Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
    - The file `hello` will be in the working directory
    - You are not allowed to use commas for this script

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `7-everybody`
---
#### 8
###### [Table of Contents](#table-of-contents)
**8. James Bond**
- Write a script that sets the permission to the file `hello` as follows:
    - Owner: no permission at all
    - Group: no permission at all
    - Other users: all the permissions
- The file `hello` will be in the working directory You are not allowed to use commas for this script

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `8-James_Bond`
---
#### 9
###### [Table of Contents](#table-of-contents)
**9. John Doe**
- Write a script that sets the mode of the file `hello` to this:
    ```
    -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
    ```
    - The file `hello` will be in the working directory
    - You are not allowed to use commas for this script

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `9-John_Doe`
---
#### 10
###### [Table of Contents](#table-of-contents)
**10. Look in the mirror**
- Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.
    - The file `hello` will be in the working directory
    - The file `olleh` will be in the working directory
	- Note: the mode of `olleh` will not always be 664. Make sure your script works for any mode.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `10-mirror_permissions`
---
#### 11
###### [Table of Contents](#table-of-contents)
**11. Directories**
- Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
- Regular files should not be changed.

<br></br>
- Repo
    - GitHub repository: `alx-system_engineering-devops`
    - Directory: `0x01-shell_permissions`
    - File: `11-directories_permissions`
---
#### 12
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 13
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 14
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 15
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 16
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---
#### 17
###### [Table of Contents](#table-of-contents)
**t**

<br></br>

---


<br></br>
<div align="right">
  <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>
