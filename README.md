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