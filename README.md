# CMPE 255: Sensor-dashboard-project
IoT Based Smart Moisture Monitoring System

* University Name: [San Jose State University](http://www.sjsu.edu/)
* Course: [Cloud Technologies](https://catalog.sjsu.edu/preview_course_nopop.php?catoid=12&coid=58423)
* Professor: [Kaikai Liu](https://cmpe.sjsu.edu/profile/kaikai-liu)
* Students: [Archana Miyar Kamath](https://www.linkedin.com/in/archana-kamath-018/), [Aakanksha Gupta](https://www.linkedin.com/in/aakanksha-gupta-739ab993?originalSubdomain=in), [Mounica Kamireddy](https://www.linkedin.com/in/mounica-kamireddy/), [Limeka Dabre](https://www.linkedin.com/in/limekadabre/)

## Project Introduction

Climate change and farmers' limited technological knowledge makes it necessary to create an IoT based intelligent farming system.Utilizing IoT sensors makes it possible to handle environmental conditions with ease. With the help of sensor information, essential aspects, such as pH, temperature, and humidity, can be monitored. This helps farmers monitor the health of the plants. The sensor readings collected over time are used to train machine learning models. The models help predict the future health of the plant. The data can be analyzed and can be used as one of the important requirements for controlling the irrigation or the other needs of the plants.

## Architecture Diagram:

![arch_dgm](https://user-images.githubusercontent.com/27188674/207071902-9c14de83-0e15-430e-a38e-5c1e6b9f7223.png)

## Requirements to run the project locally:

* A free tier AWS account with IAM user access.
* AWS Components required are as mentioned in the following section.
* Softwares Required: Node JS, React JS
* Clone this git repository using ```git clone https://github.com/archana-kamath/sensor-dashboard-project.git```
* Install frontend dependencies using ```npm install```
* Then install amplify dependencies using ```npm install aws-amplify```
* Now run ```amplify init``` to initailize amplify
* Run ```npm start``` and now the application starts running at ```localhost:3000```
* Note: Helper lambda functions can be used from ```IoT sensor - SNS Notification.py```
* To analyze the health of the plat using machine learning classification and regression algorithms, refer ```CMPE255_Project.ipynb```

## AWS Components Required:

* Amplify: Amplify Auth helped us to achieve a secure authentication and authorization flow. With the help of Cognito as its main authentication provider, it enables in                  building a  robust user directory service that handles user registration, authentication, account verification and other operations.   

* Cognito: Cognito was used to authorize users by validating the token with the federated identity providers like Facebook and Google received upon login. It creates user                pools to store the registered and logged in users from both, amplify login as well as social providers login.

* API Gateway: This service is used to receive user details from the frontend and act as a integration endpoint for backend resource. It invokes the custom Lambda authorizer                 and passes the token for further validation.

* CloudFormation:  CloudFormation helped us in creating a template of all the resources and its properties generated via Amplify. 

* Amazon Dynamo DB: A NoSQL DB used to store user details and corresponding image uploads. 

* Lambda: A lambda function which gets triggered once user uploads images to S3 bucket and sends emails to application owner. 

* SNS: A notification service which helps application owner to monitor and track users activity.

* Cloud Watch: A monitoring service to keep track of the health and utilization of resources.

* Sage Maker: A service used to build, train and deploy ML models. This application can be further enhanced to help users in recommending hotels based on location and                       customer reviews.

* Code Pipeline: A CI/CD service which enables continuous integration and delivery when ever a code commit occurs in github and gets uploaded to S3. An updated deployed version is delivered to Elastic bean stalk application.


## Application Screenshots:

* AWS Login/Signup:

<img width="1337" alt="web aws login" src="https://user-images.githubusercontent.com/27188674/143164299-0d6320a0-ba1c-4346-aed9-8beaf8b04f4f.png">

* Google Login:

![image](https://user-images.githubusercontent.com/27188674/143182922-d594a854-bf4a-4529-8ef1-aeab3dde8bf9.png)

* Facebook Login:

![FbLogin](https://user-images.githubusercontent.com/27188674/143182941-624eefd9-66f1-4351-ac91-1abd757730ef.PNG)

* Weather Page:

<img width="1281" alt="weather" src="https://user-images.githubusercontent.com/27188674/143172280-7a641670-87b0-4916-9c7f-6abceb8f0d7b.png">

* Upload Image Page:

<img width="1337" alt="Upload picture" src="https://user-images.githubusercontent.com/27188674/143172340-16657c06-0792-4f31-a9a9-4bd35097e088.png">

* FB Sharing:

![FbShare](https://user-images.githubusercontent.com/27188674/143172957-25e792ca-4684-473d-8e9e-d5467487f1dd.PNG)

* Search Image Page:

<img width="1424" alt="search picture" src="https://user-images.githubusercontent.com/27188674/143172533-df848c20-3e7b-4155-b534-c3317959d127.png">

* Chat Bot:

<img width="1440" alt="chat-voice" src="https://user-images.githubusercontent.com/27188674/143172762-e6abc7e9-2dd2-404c-aa8d-9260c1bf823d.png">

<img width="1316" alt="Chatbot" src="https://user-images.githubusercontent.com/27188674/143172809-72473e81-6d0e-43d9-82c3-a26347ea22a0.png">

* Hotel Recommendations:

![Hotel recommendations](https://user-images.githubusercontent.com/27188674/143172863-1401182b-f7b6-4486-8ec5-831be70f0567.PNG)





