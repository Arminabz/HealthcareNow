# HealthcareNow

## Application Concept:
Once the Affordable Care Act was signed into law in 2010, having health insurance became mandatory. Deciding on a plan can be laborious especially with for those with low levels of health literacy. The target population for our project are young adults looking to find a health plan that fits their needs.


**Team Members:**
```
1. Ian Crueldad
2. Jacquie Rollins
3. Elmira Akbaripourdibazar
4. Monica Montano
5. Farhad Turabi 
```

**Stakeholders:**
```
* Campus represenativies
* Students
* Healthcare agencies and hospitals
* Leaders in the healthcare field
* Health insurance providers
```

#### Requirements:
* User Log In
* Collect User Info
* Make a database
* Provide best healthcare plan


#### User Stories:
```
1. User should be able to log in
2. User should be able to add information to their profile
3. User should be able to input their healthcare needs and health symptoms 
4. Gather data from users to assess their health needs
5. Based on the information we gather about user’s health need; application will provide a system that determines the best health plans  for users
6. Create a public and private key that would indicate what information belongs to what user without showing an obvious public connection of which public keys belong to which private keys. 
```


#### Completion Times for User Stories:
```
1. User should be able to log in: 5 days
2. User should be able to add information to their profile: *5 days*
3. User should be able to select their health symptoms and needs:  *4 days*
4. Gather data from users to assess their health needs:  1 month
5. Based on the information we gather about user’s health need; application will provide a system that determines the best health plans for users:  *1 month*
6. Create a public and private key that would indicate what information belongs to what user without showing an obvious public connection of which public keys belong to which private keys: *3 days*
```


#### Example of User Stories:

    • I am a F1 visa student. I go to the gym a lot. I have noticed occasionally that I tend to strain some of my muscles after a hard work out.  I am looking for the best insurance plan for me in case I injure myself.* 

    • I am a 25-year-old who is about to be dropped from my parent’s health plan. I engage in multiple risky behaviors in addition to  having multiple mental health problems.  I want to have a health plan that will address my needs for the lowest cost.*

    • I am a 23-year-old student who just found out I am pregnant. I still haven’t decided what I want to do so I’d like to know my    different options regarding abortion, adoption, and maternal child health.*

    • I am uninsured and have been recently diagnosed with cervical cancer. I would like to know what services and treatments are      available to me.

    • Currently, I am a 20-year-old student who is in the middle of joining a sorority. I have decided to live in the house owned by my sorority. I blacked out and slept with a guy and did not realize that protection was not used. After being in pain and noticed a      rash, I consulted Web MD. I have realized there is a high chance that I contracted herpes. I hope there is a plan the offers a reduced cost on generic drugs.*

    • I am a 22-year-old transgender female who was recently diagnosed with HIV. This situation prompted me to stop using crystal meth. I need rehabilitation services and long-term HIV care.  In addition, I was diagnosed with borderline personality disorder, therefore I need dialectical behavioral therapy.*

------
## Milestone 1:
------
```
★ Draft of website  
★ Interface and working functional algorithm for collecting user information 
★ Create database for log in and register 
★ Create chat and help server 
```
------
### Allocated Tasks:
------
* *Jackie:	Develop the App, Databases, Log in*
* *Ian:	    Develop the App, Databases, Log in*
* *Elmira:	User Interface Designer*
* *Monica:	Gather data*
* *Farhad:	Security*
------
### User Story and Time Estimates: 

------
#### Milestone 1:
------
* *Velocity: 0.7*
* *Days of work: 14*
* *Days we finish: 14/0.7=20*
* *Each person work days: 20/5= 4*

##### User should be able to log in 
###### Iteration 1: 
1. Data model in Django 
2. Create user interface 
3. Commands for inserting new users in database 
4. Hashing username and password 




##### User should be able to add information to their profile 
###### Iteration 2: 
1. Create user interface
2. Save information to database


------
## Milestone 2:
------
```
★ Gather data from users to assess their health needs and
★ Based on the information we gather about user’s health need; application will provide a system that determines the best health plans for users:  *1 month*
```
------
### Allocated Tasks:
------
* *Ian:	    Write the Algorithm*
* *Elmira:	User Interface Designer*
* *Monica:	Gather data*
* *Farhad:	Security*
------
### User Story and Time Estimates: 

------
#### Milestone 2:
------
* *Velocity: 0.7*
* *Days of work: 30*
* *Days we finish: 30/0.7=42*
* *Each person work days: 42/5=11*


##### Gather data from users to assess their health needs:
###### Iteration 1: 
1. Set up migration system between user interface and database



-----
## How to run the application
------
### Environment to run the application
- Python 3.7.4
- Pip 19.2.3
- Virtual Environment 16.0.0
- Django 2.2.6
- PostGres 12
- SQL Alchemy 1.3
------
## Run Application command
------
**1. from application root activate the virtual environment**
```ruby
* Mac OS
source ./venv/bin/activate 
* Windows OS
 cd healthcarenow 
 venv/scripts/activate
``` 
**2. run Django server from app folder**
```ruby
* use python3 in stead of python if code shows error
cd src
python manage.py runserver
```
**3. Stop server by Ctrl + C**
```ruby
Ctrl + C
```
**4. Deactivate the virtualenv when not in use**
```ruby
Ctrl + Break
```
**5. Access application from http://localhost:8000/**


**6. Sample Application RUN**
```ruby
C:\Users\cruel>cd healthcarenow

C:\Users\cruel\HealthcareNow>venv\scripts\activate

(venv) C:\Users\cruel\HealthcareNow>cd src

(venv) C:\Users\cruel\HealthcareNow\src>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified 1 issue (0 silenced).
November 06, 2019 - 16:51:25
Django version 2.2.6, using settings 'HealthCareNow.settings'
Starting ASGI/Channels version 2.3.0 development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

(venv) C:\Users\cruel\HealthcareNow\src>
```

## The three most important things we learned about software development in our project:
1. We learned that it is crucial to have at least two people understand how to operate each tool that is used in the project in case of complications.
2. It is more advantageous to complete the project if the code is written in an efficient (functional) manner and is applicable to various scenarios.
3. Roles should be established at the beginning of the project based on the expertise of each person. furthermore;  there should be a working document detailing user stories to help find our path at each iteration.






