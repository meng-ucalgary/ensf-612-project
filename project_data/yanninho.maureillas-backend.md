FORMAT: 1A

# Maureillas Backend API REST V1

This document describes API REST Services for Mobile Maureillas Application 

## Group Users 

## List all [/v1/users]

+ Headers 

			Authorization : Basic key=[SECURITY KEY]

### retrieve all users [GET]

+ Request 

+ Response 200 (application/json)

+ Body
  
			[
			    {
			        "_id": "EEFDCG",
			        "platform": "IOS",
			        "active": false,
			        "__v": 0,
			        "feeds": []
			    },
			    {
			        "_id": "T6Y890OK",
			        "platform": "GOOGLE",
			        "active": true,
			        "__v": 0,
			        "feeds": [
			            {
			                "name": "feed fake",
			                "suscriber": false,
			                "_id": "557bfc23dfcd9956011be8e0"
			            }
			        ]
			    },
			    {
			        "_id": "APA91bFhAvNWQCNPdVHP6vOyv_IdQ4FBKeYe0VEUeXUeYjFqxwuDLKfWnNWPGVmHvNeW-0HWw68LW0vaO6CATGWkYVwuZgQ58BJGXxG3ikn1TpPNLXw6O2KDygsxbNOYyVelS5aXQB5gfisMa0yNOspSML4xFxupGA",
			        "platform": "GOOGLE",
			        "active": true,
			        "__v": 0,
			        "feeds": [
			            {
			                "name": "other",
			                "suscriber": true,
			                "_id": "557bfc23dfcd9956011be8e1"
			            }
			        ]
			    },
			    {
			        "_id": "RDGH78",
			        "platform": "IOS",
			        "active": true,
			        "__v": 0,
			        "feeds": [
			            {
			                "name": "feed fake",
			                "suscriber": false,
			                "_id": "557bfc23dfcd9956011be8e2"
			            }
			        ]
			    }
			]

### create a new user [PUT]

+ Request (application/json)

		{
			"user" : {
				"id" : "AZ34RT5Y",
				"platform" : "IOS"
			}
		}

+ Response 200 (application/json)
			{
			    "__v": 0,
			    "_id": "AZ34RT5Y",
			    "platform": "IOS",
			    "active": true,
			    "feeds": [
			        {
			            "name": "agenda",
			            "suscriber": true,
			            "_id": "5582e935efd5132f0005b655"
			        },
			        {
			            "name": "animals",
			            "suscriber": true,
			            "_id": "5582e935efd5132f0005b654"
			        },
			        {
			            "name": "news",
			            "suscriber": true,
			            "_id": "5582e935efd5132f0005b653"
			        }
			    ]
			}

## specific user by ID [/v1/users/{ID}]
+ Headers 

			Authorization : Basic key=[SECURITY KEY]

+ Parameters
	
	+ ID: T6Y890OK (required, string) - The user ID

### return user by id [GET]

+ Request 

+ Response 200 (application/json)
			{
			    "_id": "T6Y890OK",
			    "platform": "GOOGLE",
			    "active": true,
			    "__v": 0,
			    "feeds": [
			        {
			            "name": "feed fake",
			            "suscriber": false,
			            "_id": "557bfc23dfcd9956011be8e0"
			        }
			    ]
			}		 		

### unregister a user [DELETE]

+ Request 

+ Response 200 (text/plain)
OK

+ Response 0 

### update user datas [POST]

+ Request 

+ Body		{
				"feeds" : 
						[
						     {
						      "name" : "agenda",
						      "suscriber" : false
						    },
						    {
						      "name" : "infos",
						      "suscriber" : false
						    },
						    {
						      "name" : "lostAnimals", 
						      "suscriber" : true
						    }
						]			
		} 

+ Response 200 (text/plain)
OK

+ Response 400 (text/plain)
Invalid request, missing POST parameter feeds

## Group Platforms 

## List all [/v1/platforms]

+ Headers 

			Authorization : Basic key=[SECURITY KEY]

### retrieve all platforms [GET]

+ Request 

+ Response 200 (application/json)
			[
			    {
			        "name": "IOS"
			    },
			    {
			        "name": "GOOGLE"
			    }
			]

## specific platform by PLATFORM ID [/v1/platforms/{PLATFORM}]
+ Headers 

			Authorization : Basic key=[SECURITY KEY]

+ Parameters
	
	+ PLATFORM: windowsPhone (required, string) - The platform name

### create a new platform [PUT]

+ Request

+ Response 200 (text/plain)
OK

### delete a platform [DELETE]

+ Request

+ Response 200 (text/plain)
OK

## Group Feeds 

## List all [/v1/feeds]

+ Headers 

			Authorization : Basic key=[SECURITY KEY]

### retrieve all feeds [GET]

+ Request 

+ Response 200 (application/json)
			[
			    {
			        "name": "agenda"
			    },
			    {
			        "name": "animals"
			    },
			    {
			        "name": "news"
			    }
			]

## specific feed by FEED ID [/v1/feeds/{FEED}]
+ Headers 

			Authorization : Basic key=[SECURITY KEY]

+ Parameters
	
	+ FEED: animations (required, string) - The feed name

### create a new feed [PUT]

+ Request

+ Response 200 (text/plain)
OK

### delete a feed [DELETE]

+ Request

+ Response 200 (text/plain)
OK

## Group Messages 

## List all [/v1/messages]

+ Headers 

			Authorization : Basic key=[SECURITY KEY]

### retrieve all messages scheduled [GET]

+ Request 

+ Response 200 (application/json)

### send a message to all active users [PUT]

+ Request 
			{
				"text" : "message to send"	
			}

+ Response 200 (text/plain)
OK

### check stored messages [POST]
if date equal today, send message and delete from database

+ Request 

+ Response 200 (text/plain)
OK

## specific feed by FEED ID [/v1/feeds/{FEED}/{DATE}]
+ Headers 

			Authorization : Basic key=[SECURITY KEY]

+ Parameters
	
	+ FEED: animations (required, string) - Only send the message to users who activated this feed name
	+ DATE: 2014-05-27 (required, string) - date for schedule message 


### send a message [PUT]
if date exist and is in the future, the message is stored and send at this date.

+ Request

+ Response 200 (text/plain)
OK
