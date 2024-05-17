# githide
git hide is a simple tool to hide files in a git repository when the idea of adding them to a public `.gitignore` is unsavory. 

## other resons it might be useful 
- perhaps you want to leave a note to future you, only for your eyes. 
- perhaps you are taking notes in the same directory as your code and you don't want to commit them.
- i suppose you could hide entire files worth of sensitive information? like passwords, secrets, API keys, etc. this is especially relevant if you are too cool for a proper secrets management tool.
- perhaps you are working on a project with a team and you want to hide files from your team. you get the idea.

## under the hood
githide uses `.git/info/exclude` to hide files. This is a git feature that allows you to ignore files without adding them to `.gitignore`. This is a simple way to hide files from the git history. 

## features
- hide files from the git history using a simple command
- create a secondary --local gitignore file: `.gitignore.local`
- unhide files
- list hidden files

## installation
```bash
pip install githide
```
## usage
initialize githide. This command will create a secondary gitignore file: `.gitignore.local` at the root of the git repository. It will also execute `git config core.excludesfile .gitignore.local` and add `.gitignore.local` to the `.git/info/exclude` file. This will ensure that the `.gitignore.local` file, and each file added to it, is not tracked by git.

```bash
githide init
```
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


