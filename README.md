# SWE-573
This is for the SWE 573 project. Story sharing social network platform.

# Dependencies
Docker, docker-compose and python are enough to run this project on your local. But to install the repisotory, you might also want to install git to your computer.

# How to run the project
- Clone the repository into your local using "**git clone**" command. 
- Open the SWE-573 directory
- Run command "**docker-compose -f docker-compose-deploy.yml build**" 
- After everything is done run command "**docker-compose -f docker-compose-yml up -d**". This will start the application in your device. You can the status from Docker desktop too.
- Afterwards you cna reach the side from your local machine using 127.0.0.1 (the system is using port 80 so if any other application is using that port you might encounter an issue only thing needs to be done in that case is change the 80:8000 line to **any free port**:8000 in docker-compose-deploy.yml file and will start the server on that port)
 
