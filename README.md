# Repository for home task EPAM DevOps Essentials

## Author 

## Shved Aleksey

### 4 Variable

Tasks 
Goals:
- use variable
- source variables
Tasks:
- in your home folder create a file named vars 
- add a variable called FILE with value new_file to vars file 
- in your home folder create a script that does the following:

has NAME variable equal to your Name_Surname
sources vars file
creates a folder with name from NAME variable
creates a file in created folder with name from FILE variable
lists the contents of home folder and created folder
- execute the script

Self-check:
- script creates Name_Surname folder, new_file file in the folder and returns the following output:
Name_Surname script.sh vars
new_file

Command
touch vars
echo "FILE=new_file" > vars
touch script4.sh
chmod +x script4.sh
./script4.sh
