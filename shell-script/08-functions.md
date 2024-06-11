# Functions

`Syntax:`

```sh

# defination of function
function_name(){
    # list of commands
}


# invocation
function_name

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
