# What is shell script?

**`Variables`**
There is two types of variables

1. System defined variable
2. User defined variables

`Example: system defined`

```sh
# will display all system define variable in command line
echo $(env)
or
env in command line

echo ${PATH}
echo ${OSTYPE}
echo ${HOSTNAME}
echo ${USER}
```

`Example: User defined variable`

```sh

name=Pradeep
age=40

echo "my name is ${name} and age is ${age}"

# assign system define variable to user defined variable

ostype=${OSTYPE}
```

**`Access input from user:`**

you can use "read" command to accept input from user

```sh
read name

echo "name is ${name}"

# display input with message
read -p "Enter name" name

# -p for prompt

# provide secure input
read -p "Enter password" -s password

# -s for secure
```

**`Read only variable:`**

```sh
# read only variable declare

name=pradeep
readonly name
echo ${name}

```
