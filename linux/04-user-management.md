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

**`Changing Ownership with chown:`**

Use the `chown` command to change the `owner` and `group` of a file or directory.

- `Change owner:` chown user file
- `Change group:` chown :group file
- `Change both owner and group:` chown user:group file

```sh
# change user and group of file or directory
sudo chown john:developers /path/to/file_or_directory
```

<br />

**`Special Permissions:`**

Setuid (Set User ID) and Setgid (Set Group ID)

- `Setuid:` When set on an executable file, it allows the file to be executed with the permissions of the file owner. Symbolically represented as `s` in the user’s execute field.

- `Setgid:` When set on a file, it allows the file to be executed with the permissions of the file's group. When set on a directory, new files created in the directory inherit the group of the directory. Symbolically represented as `s` in the group's execute field.

- `Sticky Bit:` When set on a directory, it allows only the file owner or root to delete or rename the files within the directory. Symbolically represented as `t` in the others' execute field.

```sh
# add permission

# setuid
chmod u+s file

# setgid
chmod g+s file


# remove permission

# remove setuid
chmod u-s file

# remove setgid
chmod g-s file


# set sticky bit
chmod +t directory

# remove sticky bit
chmod -t directory
```

<br />

**`Access control lists (ACLs):`**

ACLs provide a more flexible permission mechanism for file systems by allowing permissions to be set for any user or group.

```sh
# installation
sudo apt-get install acl

# grant ACL permission syntax
setfacl -m u:username:permission file
setfacl -m g:group:permission file

# remove ACL permission syntax
setfacl -x u:username file

# view acl
getfacl file


# grant read and write permission to user [jhon] on `file.txt`
setfacl -m u:jhon:rw file.txt

# remove permission
setfacl -x u:jhon file.txt
```

<br />

**`Administrative privileges:`**

Administrative privileges in Linux allow users to perform system-level tasks that are restricted to regular users. These tasks include installing software, modifying system configurations, and managing other users. The primary ways to grant and manage administrative privileges are through the use of the `sudo` command and the `root` user.

`sudo:` (short for `"superuser do"`) allows a permitted user to execute a command as the superuser (root) or another user, as specified by the security policy.

```sh
# granting sudo Access to a User (syntax)
sudo usermod -aG sudo username

# grant sudo permission to [paddy] user
sudo usermod -aG sudo paddy

# Verify sudo Access
su - username
sudo whomai

```

`Editing the Sudoers File:`

The `/etc/sudoers` file controls who can run `sudo` and what commands they can run. It should be edited with the `visudo` command to prevent syntax errors.

```sh
# open the sudoers file
sudo visudo

# add user specific permission
# To grant full sudo access to a specific user, add the following line:
username ALL=(ALL:ALL) ALL # Replace username with the actual username.


# grant specific command permissions
username ALL=(ALL:ALL) /usr/bin/apt-get, /bin/systemctl
# You can also restrict the user to only run specific commands. For example, to allow username to run apt-get and systemctl:
```

<br />

**`The root user:`**

The `root` user has unrestricted access to the entire system. While using the root account directly is less common and considered less secure, it is sometimes necessary for certain tasks.

```sh
# switching to the root user
sudo -i
# or
sudo -s

# switch to the root user if you know the password
su -
```

`Note:` security considerations

- `Limit sudo Access:` Only grant `sudo` access to users who need it.
- `Use visudo:` Always use `visudo` to edit the `/etc/sudoers` file to avoid syntax errors that could lock you out of `sudo`.
- `Monitor sudo Usage:` Regularly review `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (Red Hat/CentOS) for suspicious sudo activity.
