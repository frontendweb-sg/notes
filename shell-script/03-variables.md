# Variables

There are two types of variables.

1. System defined variable
2. User defined variables

`System defined:`

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

`User defined:`

```sh
name=Pradeep
age=40

echo "my name is ${name} and age is ${age}"

# assign system define variable to user defined variable
ostype=${OSTYPE}
```

**`User input variable`**

```sh
read -p "enter name" name;
echo "${name}"

# secure input use -s
read -p "enter password" -s password;
echo "${password}"

# default value to input variable
read -p "enter name" name;
name=${name:-Pradeep}
    # or
name=${unsetvariable-Pradeep}
echo "${name}"
```
