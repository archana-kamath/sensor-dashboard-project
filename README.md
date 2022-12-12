# CMPE 255: Sensor-dashboard-project
IoT Based Moisture Alerting System for Indoor Plants

* University Name: [San Jose State University](http://www.sjsu.edu/)
* Course: [Data Mining](https://catalog.sjsu.edu/preview_course_nopop.php?catoid=12&coid=58423)
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

* AWS IoT: AWS IoT Core is a managed cloud service that lets connected devices easily and securely interact with cloud applications and other devices.

* Amazon Dynamo DB: A NoSQL DB used to store IoT sensor data coming from AWS IoT. 

* Lambda: A lambda function which gets triggered once set thresholds of temperature, humidity and moisture are dropped. An emails is sent to user. 

* SNS: A notification service which helps user to monitor and respond immediately if plant needs attention.

* Cloud Watch: A monitoring service to keep track of the health and utilization of resources.

* Sage Maker: A service used to build, train and deploy ML models. This application can be further enhanced to help users in identifying trends of plant health based on set thresholds.

## Application Screenshots:

* Login:

![login](https://user-images.githubusercontent.com/27188674/207077158-f888e81b-fe24-4afd-8262-86ffa38117e0.png)

* SignUp:

![SignUp](https://user-images.githubusercontent.com/27188674/207077472-48ede52f-8296-4d0e-9024-9e6808fed7c9.png)

* Dashboard:

![Dashboard1](https://user-images.githubusercontent.com/27188674/207078979-20405f84-c579-46b0-a8b1-266f2a676585.png)

![Dashboard2](https://user-images.githubusercontent.com/27188674/207078919-228b30b1-fe23-461a-8d61-cc7391cff584.png)




### Video Recording 

[video link](https://drive.google.com/drive/folders/1bPJauil4gRWCjdYDO75yfp-Zrq61GjVJ)


Please click on the above link to watch the working demo of the entire application and also learn more about the project implementation.





