# passwordgen
Generate secure passwords to your liking!

# Features
## You can set the number of passwords you would like to generate
## If you would like to change the number of characters for the password update the 21 (default)
```
password = ''.join(secrets.choice(characters) for _ in range(21))
```
# Installation & Running

```
git clone https://github.com/MarbleDevs/passwordgen
pip install secrets
py passwordgen.py
```
Make sure you are running your console as administrator or pip might not work
## Attention!
### If you use the create passwords infinitely option you computer might run out of space easily
### This program runs at ~1000 kbps of passwords
