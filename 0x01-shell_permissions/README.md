#### Contains scripts that manipulates permission and they include: ####
***0-iam_betty** - switches the current user to the user betty assuming there is a user called betty.*

***1-who_am_i** - prints the effective username of the current user*

***2-groups** - prints all the groups the current user is part of*

***3-new_owner** - changes the owner of the file `hello` to the user `betty`.*

***4-empty** - creates an empty file.*

***5-execute** - adds execute permission to the owner of the file.*

***6-multiple_permissions** - adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.*

***7-everybody** - adds execution permission to the owner, the group owner and the other users, to the file `hello`.*

***8-James_Bond** - sets the permission to the file hello as follows:*
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions.

***9-John_Doe** - sets the mode of the file hello to this:*

> -rwxr-x-wx 1 ovecjoe ovecjoe 23 Sep 20 14:25 hello

***10-mirror_permissions** - sets the mode of the file hello the same as olleh’s mode.*

***11-directories_permissions** - adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files are not changed.*

***12-directory_permissions** - creates a directory called dir_holberton with permissions 751 in the working directory.*

***13-change_group** - changes the group owner to holberton for the file hello.*
