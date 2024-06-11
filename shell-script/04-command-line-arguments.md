# Command line arguments

```sh
echo ${0} # will print filename
echo ${1} # will firnt second argument
```

**`conditional check`**

```sh
:${1:?"Error"} # if no command line argument then will display Error
echo "I am here"
```
