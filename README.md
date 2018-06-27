# Ride-My-Way :car:

Andela Developer Challenge one

[![Build Status](https://travis-ci.org/DerKip/Ride-My-Way.svg?branch=ft-create-endpoints-158523680)](https://travis-ci.org/DerKip/Ride-My-Way) [![Coverage Status](https://coveralls.io/repos/github/DerKip/Ride-My-Way/badge.svg?branch=ft-create-endpoints-158523680)](https://coveralls.io/github/DerKip/Ride-My-Way?branch=ft-create-endpoints-158523680) 
![GitHub last commit](https://img.shields.io/github/last-commit/DerKip/Ride-My-Way/develop.svg)
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
|Endpoint                               | Functionality                                 |HTTP method 
|---------------------------------------|-----------------------------------------------|-------------
|/api/v1/user/register                  |Register user                                  |POST       
|/api/v1/login                          |Logs in a user/driver                          |POST
|/api/v1/user/logout                    |Logs out user                                  |DELETE
|/api/v1/user/user/rides                |Return available ride offers                   |GET
|/api/v1/user/user/rides/*ride_id*/join |User join ride offer                           |GET
|/api/v1/user/user/rides/joined         |Return joined rides                            |GET
|/api/v1/driver/register                |Register driver                                |POST
|/api/v1/driver/logout                  |Logs out a driver                              |DELETE
|/api/v1/driver/create_ride             |Create ride offer                              |POST
|/api/v1/driver/rides                   |Return available rides to driver               |GET
|/api/v1/driver/rides/*ride_id*         |Returns a single ride created                  |GET
|/api/v1/driver/rides/<str:driver>      |Returns all rides created by a specific driver |GET

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
