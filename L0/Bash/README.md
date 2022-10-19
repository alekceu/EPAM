# Repository for home task EPAM DevOps Essentials

## Author 

## Shved Aleksey


## List of task

  - [4 Variables](#task4)
  - [5 Environment Variable](#task5)
  - [6 Special variables](#task6)
  - [7 Conditional Operations](#task7)
  - [8 If Statement](#task8)
  - [9 Case Statement](#task9)
  - [10 Pipelines ](#task10)
  - [10 For loop](#task11)
  - [12 While loop](#task12)
  - [13 Until loop](#task13)
  - [14 Pipelines](#task14)
  - [15 Positional arguments](#task15)
  - [16 Input Output](#task16)
  - [17 Functions](#task17)
  - [18 Python](#ptask1)

### 4 Variables <a name="task4"></a>

Tasks

Goals:
- use variable
- source variables
Tasks:
- in your home folder create a file named vars 
- add a variable called FILE with value new_file to vars file 
- in your home folder create a script that does the following:
  - has NAME variable equal to your Name_Surname
  - sources vars file
  - creates a folder with name from NAME variable
  - creates a file in created folder with name from FILE variable
  - lists the contents of home folder and created folder
- execute the script

Self-check:
- script creates Name_Surname folder, new_file file in the folder and returns the following output:
  - Name_Surname script.sh vars
  - new_file

Commands:
 - touch vars
 - echo "FILE=new_file" > vars
 - touch script4.sh
 - chmod +x script4.sh
 - ./script4.sh

### 5 Environment Variable <a name="task5"></a>

Goals:
- setting and unsetting environment variables
- work with PATH

Tasks:
- create homework folder in your user's home folder
- create SURNAME environment variable equal to your surname
- verify that SURNAME variable is present in the environment using env command
- create a script in homework folder that prints the value of SURNAME variable
- add homework folder to PATH
- verify that you are able to run your script by typing only its name into the terminal

Self-check:
- my_script.sh command gives the following output:
  -Surname

Commands:
 - mkdir homework5
 - export SURNAME="shved"
 - env | grep SURNAME
 - touch ./homework5/script05.sh
 - chmod +x ./homework5/script05.sh
 - PATH="$PATH:/home/shvedav86/homework5"
 - ./script05.sh
 
 ### 6 Special variables <a name="task6"></a>
 
Goals:
	- using reserved variables

Tasks:
- create a script that does the following:
  - prints the name of the script
  - prints all arguments
  - prints the number of arguments passed to the script
  - prints 2nd and 4th argument
  - print the exit code of -eq operation on 1st and 2nd arguments (use [[]])
- execute your script like this: ./my_script.sh 1 2 hello world
- change the script arguments so that the result of the last operation (-eq) would be 0
- run the script again with new arguments

Self-check:
- first script run results:
- ./my_script.sh
  - 1 2 hello world
  - 4
- 2 world
  - 1
- second script run results contain 0 as the last output

### Commands
- touch script06.sh

### 7 Conditional Operations <a name="task7"></a>

Goals:
  - write conditional statements

Tasks:
  - create a script file in your home directory that does the following:
  - checks if 1st and 2nd string arguments are equal and outputs the exit code of this operation
  - checks if 1st string argument is longer than 2nd string argument and outputs the exit code of this operation
  - checks if variable TEST is present in the environment (has non-zero length) and outputs the exit code of this operation
  - checks if 3rd and 4th integer arguments are not equal and outputs the exit code of this operation
  - checks if 3rd integer argument is greater or equal to 4th integer argument and outputs the exit code of this operation
  
  - run your script with "hi world 7 9" arguments
  - add TEST environment variable with "123" value
  - re-run the script with "hello hello 10 7" arguments

Self-check:
  - first script run should return the following values:
  1 1 1 0 1
  - second script run should return the following values:
  0 1 1 0 0
  
### Answer in file script07.sh

### 8 If Statement <a name="task8"></a>
Tasks:
- create a script called odd_even.sh that does the following:
  - takes one argument
  - if the number of letters in the argument is odd, outputs the message "Odd", else if the number of letters is even - outputs "Even"
  
- run the script first with "odd" argument, then with "even" argument
- create a script called my_script.sh that does the following:
  - takes any number of arguments
  - if there are less than 2 arguments, output the values of these arguments
  - if there are more than 2 but less than 4 arguments, output only the last argument else output "Invalid number of arguments" message
- run my_script.sh with the following arguments:
  - hello
  - hello world
  - pie is lie
  - keep calm and procrastinate

Self-check:
- odd_even.sh script outputs:
  - first run: Odd
  - second run: Even
- my_script.sh script outputs:
  - hello
  - Invalid number of arguments
  - lie
  - Invalid number of arguments

### Answer in file script08.sh and odd_even_08.sh

### 9 Case Statement <a name="task9"></a>

Tasks:
- create a script called my_service.sh which does the following:
  - accepts start, stop, restart arguments:
  - start - outputs "Service started" message and sleeps for 9999
  - stop - gets the PID of my_service.sh process and terminates it, then outputs "Service stopped" message
  - restart - stops and then starts the service
  - any other argument outputs script usage information
- add your service to PATH
- run your script with start and restart arguments in background
- run your script with stop and help arguments

Self-check:
- script executions retrun the following:
  - start: 
[1] 45043
Service is started
  - stop:
Service is stopped
[2]  + 44996 terminated  ./my_script.sh start
  - restart:
[1] 45863
Service is stopped
Service is started
  - help:
usage: my_service.sh [start|stop|restart]

### Answer in file script09.sh

### 10 Pipelines <a name="task10"></a>

Tasks:
- write a one line command using || and && operators that does the following:
  - creates a folder named Name_Surname 
  - if folder creation was successful, creates a file inside, called my_file
  - if file creation was successfull, writes "Hello" into the file
  - if previous operation was successful, lists the contents of the file
  - if any of the operations fail, print "Something went wrong"
- run the command two times
- write a command that outputs only users that have /usr/bin/false shell from /etc/passwd file and changes the shell to /bin/bash

### Commands
 - (mkdir alekceu_shved && touch ./alekceu_shved/my_file && echo "Hello" > ./alekceu_shved/my_file && cat ./alekceu_shved/my_file ) || echo "Something went wrong"
 - cat /etc/passwd | grep /sbin/nologin | sed "s/sbin\/nologin/bin\/bash/g"
 
### 10 For loop <a name="task11"></a>

Tasks:
- create a script that does the following:
  - accepts any number of int arguments
  - outputs the sum of all arguments
  - outputs the number of arguments
  - outputs the average of all arguments
- execute your script with the following arguments 1 2 3 4 5

Self-check:
- your script outputs the following:

Sum: 15
Args number: 5
Result: 3

### Answer in file script11.sh

### 12 While loop <a name="task12"></a>

Tasks:
- create console.sh script that does the following:
  - implements console functionality 
  - infinite loop that reads user input on each iteration
  - supports commands:
    - ls [dir] - lists the contents of specified directory
    - pwd - shows the path to current directory
    - hi - outputs "Hello <name of the current user>" 
    - exit - ends the script
- run your script and test implemented commands

### Answer in file script12.sh

### 13 Until loop <a name="task13"></a>

Tasks:
- create a script that does the following:
  - reads a filename from user input
  - combines specifyed file with itself until it reaches a size greater than 1024 KB
  - create a file using head -c 4KB /dev/urandom > file.txt command
- execute your script passing the file you've just created

Self-check:
- script returns the following output:

Filesize: 8
Filesize: 16
Filesize: 32
Filesize: 64
Filesize: 128
Filesize: 256
Filesize: 504
Filesize: 1004
Filesize: 2004

### Answer in file script13.sh

### 14 Pipelines <a name="task14"></a>

### Answer commands
- (mkdir alekceu_shved && touch ./alekceu_shved/my_file && echo "Hello" > ./alekceu_shved/my_file && cat ./alekceu_shved/my_file ) || echo "Something went wrong"
- cat /etc/passwd | grep /sbin/nologin | sed "s/sbin\/nologin/bin\/bash/g"

### 15 Positional arguments <a name="task15"></a>

Tasks:
- create a script that does the following:
- accepts any number of arguments
- prints all arguments in the following format "Arg1: <arg1 value>", "Arg2: <arg2 value>"
- adds the value of the next argument to the previous one and prints it out (for the last argument add the value of the first one)
- run the script with 7 1 5 7 4 3 6 arguments

Self-check:
- script run returns the following results:
  - Arg1: 7
  - Arg2: 1
  - Arg3: 5
  - Arg4: 7
  - Arg5: 4
  - Arg6: 3
  - Arg7: 6
  - 8 6 12 11 7 9 13

### Answer in file script15.sh

### 16 Input Output <a name="task16"></a>
Tasks:
- create a script that does the following:
  - asks the user to input a filename
  - writes the following poem to the file specified by user:
  
An old silent pond...
A frog jumps into the pond,
splash! Silence again.
Autumn moonlight-
a worm digs silently
into the chestnut.
In the twilight rain
these brilliant-hued hibiscus -
A lovely sunset.

  - outputs the poem to the terminal
  - outputs the message "Task finished" to stderr
- run your script, specify output as the file to write the poem to, redirect stdout to /dev/null, redirect stderr to stderr file

Self-check:
- script returns no output
- cat output command returns the poem
- cat stderr command returns: Task finished

### Answer in file script16.sh предварительно нужно создать файл с содержимым поемы poem.txt

### 17 Functions <a name="task17"></a>

Goals:
- learn to use functions
- learn to use nested functions

Tasks:
- create a script that does the following:
  - has a function that multiplies the argument passed to it by itself
  - has a second function that passes each argument passed to the script to the first function and increases the result by 1 and outputs to the console
- run your function with the following arguments: 5 6 1 3 9

Self-check:
- function returns the following output:
26 37 2 10 82

### Answer in file script17.sh

### 18 Python <a name="ptask1"></a>

All task are placed in python directory. Funny game - find_out.py. To run you need
- install python
- run command "python find_out.py"
