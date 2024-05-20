# githide
git hide is a simple tool to hide files in a git repository when the idea of adding them to a public `.gitignore` is unsavory. githide allows you to manipulate the `.git/info/exclude` file from the command line, which bypasses the .gitignore shared by the repo.

## introduction
### why githide exists
- too lazy to manually adjust `.git/info/exclude` manually.

### usecases
- write a note in the context of your current working directory:
  - in an open source project  
  - a note to future you
  - personal documentation about a repo you are exploring.
  - spicy code, for your eyes only
- another (albiet unnessesary) `git stash`

### other resons it might be useful 
- i suppose you could hide anyhting you want from git.
  - [x] an entire file worth of sensitive information? it is probably not a good idea to hide passwords, secrets, or API keys in plain text, but you sure could hide it from the prying eyes of the git history. this is especially relevant if you are too cool for a proper secrets management tool.
  - [x] perhaps you are working on a project with a team and you want to hide files from your team because you are up to some hyjinks. the rascal that you are, you `githide` those forbidden fruits. you get it, ya scallywag.
- any other reason you don't want to commit a file.

### under the hood
githide uses `.git/info/exclude` to hide files. groundbreaking, i know. if you didn't alreay know, or didn't read the introduction, it is a git feature that allows you to ignore files without adding them to `.gitignore`.

## features, installation, and usage
### features
- hide files from the git history using a simple command
- a private `.gitignore`: create a secondary --local gitignore file: `.gitignore.local` that you can easily manage from the root of the project
- unhide files
- list hidden files

### installation and initialization
#### install via pip
```bash
pip install githide
```
#### initialize githide. 
```bash
githide init
```
This command will create a secondary gitignore file: `.gitignore.local` at the root of the git repository. It will also execute `git config core.excludesfile .gitignore.local` and add `.gitignore.local` to the `.git/info/exclude` file. This will ensure that the `.gitignore.local` file, and each file added to it, is not tracked by git.

### usage
hide a file or directory
```bash
githide add <file>
```
unhide/remove a file or directory from the hidden list
```bash
githide remove <file>
```
list hidden files
```bash
githide list
```
undo the last hidden file
```bash
githide undo
```
or
```bash
githide pop
```

## note
- githide does not encrypt files. It simply hides them from the git history. 
- githide is a simple tool and does not provide any security. It is a convenience tool to hide files from the git history. 
- the hidden files are stored in a secondary gitignore file: `.gitignore.local`
- the hidden files are not tracked by git. They are ignored by git. 
- githide is not a replacement for a proper secrets management tool. It is a simple tool for hiding files. 
- did i mention that you can use `githide` to hide files from the git history?

that's all. have a nice day. 


