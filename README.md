## --------------Project Wireguard VPN Keys Generator-----------------------

## The goal of this project
``` 
I created this program because i have to do all the time WG-gen for clients on my VPN,
instead when i put just a username with any ip it will generate automatically public
and privat keys and store everything into database rather than store it in text file,
also i did added some nice features like checking the username and ip if exist,
this will avoid repeating the users and ips, becuase in WG you need a Uniqe IP.
another thing in this program, you don't have to do much becuase it works as an Options,
So you can pick the option you like to make input stuff and output stuff.
```
## What's the options in this program. 
---
* can add users And Ips into database
* can fetch informations about users ips and keys from database
* can search about specific user or ip or keys with ID search or table search
* can delete users with user all data by using the ID.
---

## How the code was designed:
```
* The code written in python language and mixed with Bash and SQL Commands. 
* I tried to make the code simple as possbile for people who likes to change things.
* The Artch build as stand alone functoins in all part of code except searching part is Done with OOP
```
