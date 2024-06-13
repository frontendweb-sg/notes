# Linux user management

**`Add new user:`**

To add new user user `adduser` command.

`Syntax:`

```sh
# logged in as root user
sudo adduser username

# verify the new user
cat /etc/passwd | grep username

# user's home directory
ls -la /home/username
```

You will be prompted to enter and confirm a password for the new user.

<br />

**`Modifying a User:`**

To change the user information.

```sh
# change username
sudo usermod -l new_username old_username

# change user home directory
sudo usermod -d new_directory username

# add user to a new group
sudo usermod -aG group_name username

# give user to administrative group
sudo usermod -aG sudo username
```

<br/>

**`Delete User:`**

```sh
# syntax
sudo deluser username

# to delete user and their home directory
sudo deluser --remove-home username
```

<br/>

**`Creating and managing groups:`**

```sh
# syntax
sudo addgroup group_name

# example
sudo addgroup developers

# add a user to a group
sudo usermod -aG developers username

# remove a user from a group
sudo deluser username group_name
```

**`Viewing user and group information:`**

```sh
# view user detail
id username

# list all users
cat /etc/password

# list groups
cat /etc/group

# change own passord
passwd

# change user password
passwd username

# verify the user's groups
groups username

# switch to the new user
su - username

# after switching you can verify the current user
whoami
```

<br />

**`Users and group permission:`**

- `users:` Individual accounts that can log into the system. each user has a unique user id (UID)
- `groups:` Collections of users. each group has a unique group id (GID). users can belong to multiple group.

**`File and directory permissions:`**

Each file and directory in Linux has an associated set of permissions and an owner. Permissions are divided into three sets:

- `user (owner):` Permission for the file's owner.
- `groups:` Permission for the group that the file belong.
- `others:` Permission for all others user.

Permissions are represented as a combination of `read (r)`, `write (w)`, and `execute (x)` permissions:

- `Read (r):` Permission to read the file or list the directory contents.
- `Write (w):` Permission to modify the file or directory contents.
- `Execute (x):` Permission to execute the file or traverse the directory.

```sh
# view permissions
ls -l /path/to/file_or_directory
```

- The first character indicates the type (`-` for a file, `d` for a directory).
- `-rwxr-xr--`
  - `rws:` for the user
  - `r-x:` for the group
  - `r--:` for the others

<br />

**`Changing permission with chmod:`**

Use the `chmod` command to change file and directory `permissions`. There are two methods: symbolic and numeric.

`Symbolic Method:`

- `Add permission:` chmod u+x file (add execute permission for the user)
- `Remove permission:` chmod g-w file (remove write permission for the group)
- `Set specific permission:` chmod o=r file (set read-only permission for others)

`Numeric Method:` Permissions can also be represented using octal numbers:

- `Read (r)` = 4
- `Write (w)` = 2
- `Execute (x)` = 1

<br />

\*`Changing Ownership with chown:`\*\*
