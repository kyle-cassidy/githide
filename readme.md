# githide
git hide is a simple tool to hide files in a git repository. It is useful for hiding sensitive information like passwords, API keys, etc. from the git history. Or perhaps you want to leave a note to future you, only for your eyes. 

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


