# Messaging application

A simple example of using Redis with Python.

## Use Case

This app supports sending a particular user a message, or
sending a message to all users.

Once a user reads a message, it is removed from their queue
of unread messages.

A user is authenticated by providing a password.

We will need the ability for the admin to create users and
set their initial password. Thereafter, a user can change
their password.

## Redis DB structure

```
users = {joe: 13245, jane: mypass}
joe_messages = [message 1, message 2]
jane_messages = [message 5]
```

## Running

```
$ python messengr.py register jane mypassword
$ python messengr.py send jane joe "here is my message..."
$ python messengr.py read jane
```



