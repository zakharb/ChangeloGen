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