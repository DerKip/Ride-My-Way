# Ride-My-Way :car:

Andela Developer Challenge one

[![Build Status](https://travis-ci.org/DerKip/Ride-My-Way.svg?branch=develop)](https://travis-ci.org/DerKip/Ride-My-Way) [![Coverage Status](https://coveralls.io/repos/github/DerKip/Ride-My-Way/badge.svg?branch=develop)](https://coveralls.io/github/DerKip/Ride-My-Way?branch=develop) 
![GitHub last commit](https://img.shields.io/github/last-commit/DerKip/Ride-My-Way/develop.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Introduction

## Project Overview
-Ride-My-Way  App is a carpooling  application that provides 
 drivers with the ability to create ride offers and passengers to join available ride offers

## Required Features
1. Users can create an account and log in.
2. Drivers can add ride offers..
3. Passengers can view all available ride offers.
4. Passengers can see the details of a ride offer and request to join the ride. E.g What time the ride leaves, where it is headed e.t.c
5. Drivers can view the requests to the ride offer they created.
6. Drivers can either accept or reject a ride request.

 # API Endpoints
|Endpoint                                           | Functionality                     |HTTP method 
|---------------------------------------------------|-----------------------------------|-------------
|/api/v2/auth/signup                                |Register user                      |POST       
|/api/v2/auth/login                                 |Logs in a user                     |POST
|/api/v2/users/rides                                |Fetch all available rides          |GET 
|/api/v2/users/rides/*ride_id*                      |Fetch the details of a single ride |GET
|/api/v2/users/rides/*ride_id*/requests             |Make a ride request                |POST
|/api/v2/users/rides                                |Create a ride offer                |POST
|/api/v2/users/rides/*ride_id*/requests             |Fetch all ride requests            |GET
|/api/v2/users/rides/*ride_id*/requests/*requestId* |Accept or Reject a request         |PUT

# Installing the App and Running it 

   Clone the repo:   https://github.com/DerKip/Ride-My-Way.git
   
   Install a virtual environment and activate it : 
   on windows ```py -3 -m venv venv
               .\venv\Scripts\activate```
             
   on linux  ```$ python3 -m venv venv;
                $ source venv/bin/activate```

   Cd to the directory of the application  `cd Ride-My-Way`  
   
   Install all the dependencies through: `pip install -r requirements.txt`
   
   create a PostgreSQL database: ```ride_my_way```
   Run the schema file to initialize the tables ```python schema.py```
   Run application: `python run.py`
   
# Running tests
   
   Cd to the directory of either apiv1 or apiv2 : `cd apiv1` or `cd apiv2`
   
   Run the test: `- nosetests --with-coverage --cover-package=routes `
   
# API doccumentation Link
   Link: https://ridemyway1.docs.apiary.io/#
   
# UI Templates
You can view the UI templates on  :point_right: [Github Pages](https://derkip.github.io/Ride-My-Way/)

# Pivotal Tracker Project
You can view the pivotal tracker stories :point_right: [here](https://www.pivotaltracker.com/n/projects/2177670)

## login and Sign up Page
New users can Register as passengers or Driver
![login](https://user-images.githubusercontent.com/28872296/41493309-997b4b2c-710e-11e8-85ea-12baffdcf8ae.gif)

## Drivers can make ride offers
![create](https://user-images.githubusercontent.com/28872296/41493394-7aef6e94-710f-11e8-8589-89764779bae8.gif)

## users can view ride details
![details](https://user-images.githubusercontent.com/28872296/41493633-eb1907fa-7111-11e8-8be9-ec617c647d9c.gif)

## Drivers can respond to requests
![response](https://user-images.githubusercontent.com/28872296/41493699-8f4df600-7112-11e8-8a9d-6eb444e70959.gif)


## User can view profile
![driver profile](https://user-images.githubusercontent.com/28872296/41493445-06a73c1e-7110-11e8-8eef-8b2de0d4573d.png)


## Contribution
If you want to contribute to this project:
 - Fork it! :fork_and_knife:
 - Create your feature branch: git checkout -b my-new-feature
 - Commit your changes: git commit -m 'Add some feature'
 - Push to the branch: git push origin my-new-feature
 - Create a pull request. 
