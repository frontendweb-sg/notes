# Shell string string

**`String method:`**

```sh
name=pradeep;
text="hello world";
echo "${text}"

# first letter capital
echo "${text^}"

# uppercase
echo "${text^^}"

# length of string
echo "${#text}"

# concatenation of string
echo ${text}${name}

# substring
# ${string:position:length}
echo "${text:0:5}"

# lowercase
 # first letter in lower
echo "${text,}"
 # all in lower
echo "${text,,}"

# substring match


```

**`Substring match:`**

In Bash, the shortest and longest possible match of a substring can be found and deleted from either front or back.

- To `delete` the shortest substring match from front of `$string:`

`Example:`

```sh
text='my name is pradeep my kumar'
${string#my}

```

- To `delete` the longest substring match from front of `$string:`

`Example:`

```sh
text='my name is pradeep my kumar'
${string##my}
```

- To `delete` shortest substring match from back of $string:

`Example:`

```sh
text='my name is pradeep my kumar'
${string%my}

```

- To `delete` the shortest substring match from back of $string of `$string:`

`Example:`

```sh
text='my name is pradeep my kumar'
${string%%my}
```

`Note:` use `*` from to

`example:`

```sh
echo "${text##my*my}"
```
