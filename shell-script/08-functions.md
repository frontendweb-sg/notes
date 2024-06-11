# Functions

`Syntax:`

```sh

# defination of function with or without function keyword
function function_name(){
    # list of commands
}


# invocation
function_name


# ${FUNCNAME} is used to print function name
```

`Example:`

```sh
# function defination (declaration)
run () {
   echo "Hello World"
}

# Invoke your function
run
```

**`Parameters:`**

These parameters would be represented by `$1, $2` and so on.

`Example:`

```sh
# function defination  (declaration)
run () {
   echo "Hello World $1 $2"
}

# Invoke your function
run pradeep kumar
```

**`Return value from function:`**

You can return any value from your function using the `return` command

`Example:`

```sh
# function defination  (declaration)
run () {
   echo "Hello World $1 $2"
   return 10
}

# Invoke your function
run Pradeep Kumar

# hold value in variable
value=$?

echo "Run return value is $value"
```

**`Nested function:`**

`Example:`

```sh
# Calling one function from another
run () {
   echo "Parent function"
   nested
}

nested () {
   echo "nested function invoking from paretn"
}

# Calling function one.
run
```

**`Function local variable`**

To declare `local` variable use `local` keyword

`Example:`

```sh
function run(){
    local myname=Arun  # local variable, only work inside the function
    echo "This is my first function $1"
    return 10
}

run pradeep

echo "${myname}" # will not display

```
