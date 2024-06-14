# Loops

**`For loop:`**

`Syntax:`

```sh
# range {START..END..INCREMENT}
for variable in range
do
    # commands
done

#  or

for variable in file1 file2 file3 ...etc
do
    # commands
done

# or

for variable in $(linux-commands)
do
    # commands
done

#  three expression bash for loop
for (( EXP1; EXP2; EXP3 ))
do
    command1
    command2
    command3
done

# infinite loop
for (( ; ; ))
do
   echo "infinite loops [ hit CTRL+C to stop]"
done

# conditional exit with break
for i in {1..50}
do
    if condition
    then
        break
    fi

# continuation with continue statement
for i in {1..50}
do
    statements
    if condition
    then
        continue #Go to next iteration of i in the loop and skip statement last
    fi
    statement last
done
```

`Example:`

```sh
# print 1 to 10
for i in {1..10} # range from {1..10}
do
    echo "number: $i";
done

# print 2 to 20 increment by 2
for i in {2..20..2}
do
    echo "value: $i";
done

# print all odd number from 1 to 50
for i in {1..50}
do
    if [[ $(( i % 2 )) != 0 ]]
    then
        echo "odd value: $i"
    fi
done

# print all password file
cat /etc/passwd | while read line
do
    echo "$line";
done

#  or
while read line
do
    echo "$line";
done < /etc/passwd

#  or
INPUT=/etc/passwd
while read line
do
    echo "$line";
done < "$INPUT"


#  sequence command
for i in $(seq 1 2 20)
do
   echo "Welcome $i times"
done

# three expression bash for loop
for (( c=1; c<=5; c++ ))
do
   echo "Welcome $c times"
done



```

**`Select:`**

`Syntax:`

```sh
PS3="put message here it will replce default message"
select varName in list
do
    command1
    command2
    ....
    ......
    commandN
done
```

`Example:`

```sh
# skill select
PS3="Please select skill: "
select option in html css js react
do
    echo "$option"
done

# exit select with case

PS3="Please select skill: "
select option in html css js react
do
    case ${option} in
        html)
            echo "You have selected ${option}"
            break
            ;;
        css)
            echo "You have selected ${option}"
            break
            ;;
        js)
            echo "You have selected ${option}"
            break
            ;;
        react)
            echo "You have selected ${option}"
            break
            ;;
        *)
            break
            ;;
    esac
done
```
