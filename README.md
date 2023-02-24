# Day24

## Lessons learned today

- reading a file
```
with open('file') as file:
    data = file.read()
    print(data)

```
- writing to a file
```
with open('file',mode='w') as file:
    data = file.write("Hello world")
```


## Project to solidify material learned: 

### working_with_local_files

> Using the open function to read and update files... Here it is used to automate invitation letters to be sent to friends.


#### Preview:

![letters](./letters.png)

## How to run this on your device

- Clone this repository
```
git clone https://github.com/kingdreamerr/Day24_working_with_local_files.git
```
- cd into the repo
```
cd Day24_working_with_local_files
```

- Paste the following in the terminal 
```
python3 main.py
```