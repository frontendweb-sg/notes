# What is shell script?

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


# unset variable
unset name;
echo "${name}"
```

**`Debug mode:`**

```sh
bash -x file_name

# or

set -x # start debug mode from
set +x # end debug mode to

# example

echo "Hi";
name="pradeep"
set -x
echo "Enter name"
var = ${1}
echo "$var"
set +x
```
