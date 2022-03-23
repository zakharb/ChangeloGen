![logo](logo.png)

## _Simple Changelog Generator for Github Log_ 

![](https://img.shields.io/badge/version-1.1-blue)
![](https://img.shields.io/badge/python-3.9-blue)

## Content  
[Info](#info)  
[Install](#install)
[Usage](#usage)

<a name="info"/>

## Info
</a>  

> The software is designed to create a Changelog from a Github log  
> It uses commit and tag history  
> A file of the Markdown, TXT or PDF format is created  

<a name="info"/>

## Install
</a>  

- download `.whl` file
- install via `pip`
```sh
pip install zlog-xxx.whl  
```
 
<a name="usage"/>

## Usage
</a>  

```sh
CHANGELOGEN 1.1 Simple Changelog Generator for Github Log
Copyright (C) 2021 Bengart Zakhar
This program comes with ABSOLUTELY NO WARRANTY
This is free software, and you are welcome to redistribute it
under certain conditions; type `--license` for details.

   ________  _____    _   ________________    ____  _____________   __
  / ____/ / / /   |  / | / / ____/ ____/ /   / __ \/ ____/ ____/ | / /
 / /   / /_/ / /| | /  |/ / / __/ __/ / /   / / / / / __/ __/ /  |/ / 
/ /___/ __  / ___ |/ /|  / /_/ / /___/ /___/ /_/ / /_/ / /___/ /|  /  
\____/_/ /_/_/  |_/_/ |_/\____/_____/_____/\____/\____/_____/_/ |_/   

usage: changelogen [options]

optional arguments:
  -h, --help      show this help message and exit
  -g, --generate  Generate Changelog file from git logs
  -o, --output    Save to file
  -f, --format    Choose format md, txt
  ```

- Use the following format when make commits
```
<type>: short message

update: update Readme.md
add: export to PDF format
```

- move to `git` folder

- create `changelog.md`
```sh
python3 -m logen -g
```