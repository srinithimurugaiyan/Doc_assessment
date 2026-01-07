Docker Documentation 

Project 1: Application Containerization 

------------STATIC HTML ---------------
STEP1: Make the directory  
       => sudo mkdir –p /var/www/html 

STEP2: Change the current directory
       => cd /var/www/html

STEP3: Create HTML file inside the directory
       => sudo nano /var/www/html/index.html

STEP4: Type the code in the index.html
       <h1>Hello Srinithi</h1>
       <h4>Welcome to DevOps Team</h4>

STEP5: Configuration of Static HTML website
       => sudo nano /etc/nginx/sites-available/html

STEP6: Type it
       server {
       listen 8009;
       root /var/www/html;
       index index.html;
       location / {
       try_files $uri $uri/ =404;
       }
       }

      Then click ctrl + o, Enter and ctrl + x

 STEP7: Enable a site
        => sudo ln -s /etc/nginx/sites-available/html /etc/nginx/sites-enabled/

 STEP8: Test the configuration
        => sudo nginx -t

STEP9: Allow the port number using ufw
       => sudo ufw allow 8009

STEP10: Restart the nginx
        => sudo systemctl restart nginx

STEP11: Go to the Browser
        <img width="1356" height="726" alt="image" src="https://github.com/user-attachments/assets/29723cb5-98c3-4717-9ec6-7771cfcf7c5f" />


-------------DOCKER--------------
STEP1: Create Dockerfile inside the directory
       => sudo nano Dockerfile

STEP2: Type it
       FROM nginx:latest
       COPY . /usr/share/nginx/html
       EXPOSE 80

       Then click ctrl + o, Enter and ctrl + x

STEP3: Build the image 
       => docker build -t image_name .

STEP4: Run the container with the image 
       => docker run -d -p 8009:80 --name container_name image_name

STEP5: To the container and images which was created
       => docker ps


------------DOCKER HUB-------------
STEP1: Login the docker hub
       => docker login -u username

STEP2: Docker tagging the image-name
       => docker tag image_name username/image_name:latest

STEP3: Push the image in the docker hub
       => docker push username/image_name:latest

STEP4: Go to the docker hub website
       <img width="1361" height="725" alt="image" src="https://github.com/user-attachments/assets/43aaead0-d5f9-4857-92da-b17536d71230" />


------------GITHUB-------------
STEP1: Create a new public repository 

STEP2: Go to the git bash and put the commands

STEP3: Initialize the git
       => git init

STEP4: Clone the repository
       => git clone <url>

STEP5: Check the current changes of repo
       => git status

STEP6: Stage all changes
       => git add .

STEP7: Check status
       => git status

STEP8: Committing changes
       => git commit -m "message"

STEP9: Push it in local commits
       => git push




       
