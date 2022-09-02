# Repository for home task EPAM DevOps Essentials

## Author 

## Shved Aleksey

### 4 Variables

Tasks

Goals:
- use variable
- source variables
Tasks:
- in your home folder create a file named vars 
- add a variable called FILE with value new_file to vars file 
- in your home folder create a script that does the following:
  -- has NAME variable equal to your Name_Surname
  -- sources vars file
  -- creates a folder with name from NAME variable
  -- creates a file in created folder with name from FILE variable
  -- lists the contents of home folder and created folder
- execute the script

Self-check:
- script creates Name_Surname folder, new_file file in the folder and returns the following output:
  - - Name_Surname script.sh vars
  - - new_file

Commands:
 - touch vars
 - echo "FILE=new_file" > vars
 - touch script4.sh
 - chmod +x script4.sh
 - ./script4.sh

### 5 Environment Variable

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
  -- Surname

Commands:
 - mkdir homework5
 - export SURNAME="shved"
 - env | grep SURNAME
 - touch ./homework5/script05.sh
 - chmod +x ./homework5/script05.sh
 - PATH="$PATH:/home/shvedav86/homework5"
 - ./script05.sh
 
 ### 6 Special variables
 
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

### 7 Conditional Operations
 
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

### 8 If Statement
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

### Answer in file script08.sh
 