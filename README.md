# twisted-log
A simplistic twisted log

THIS IS ONLY A PROOF OF CONCEPT !!!

The project showcases a simple approach to adding a real time logging to a server.
The logging takes place when an exception in any of the twistd applications occurs.
It is predefined to log only exceptions that the user wants to look out for.
It then sends predefined information to be logged to a simple database.

The project contains also an Ansible solution to deploy the server and 5 applications to two hosts, 
one for the logging server and one for the 5 applications.
If the hosts configuration is different, the code needs to be changed.

The project contains very simple tests and was tested manually most of the time.
