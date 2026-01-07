Docker Documentation 

Project 1: Application Containerization 

------------Static HTML ---------------
STEP1: Make the directory  
       => sudo mkdir –p /var/www/html 

STEP2: Change the current directory
       => cd /var/www/html

STEP3: Create HTML file inside the directory
       => sudo nano /var/www/html/index.html

STEP4: Paste the code in the index.html
       <h1>Hello Srinithi</h1>
       <h4>Welcome to DevOps Team</h4>

STEP5: Configuration of Static HTML website
       => sudo nano /etc/nginx/sites-available/html

STEP6: Paste it
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

STEP9: Restart the nginx
        => sudo systemctl restart nginx

STEP10: Go to the Browser
        <img width="1356" height="726" alt="image" src="https://github.com/user-attachments/assets/29723cb5-98c3-4717-9ec6-7771cfcf7c5f" />

       


       
