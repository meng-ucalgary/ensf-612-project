# ninja-sso-um
Mobile friendly Single Sign-On and User management application template for [Ninja Framework](http://www.ninjaframework.org/).

# Features
* Sign up page with detailed information, captcha and email verification
* Sign in page with captcha
* User roles: administrator, moderator, user
* User management by administrator
    * Search/list of users with an optional query and pagination
    * Edit personal information
    * Edit contact information
    * Edit access permissions and levels
    * View access log and detailed access events
    * Send email
    * Reset password
* Multiple language support: English, German, Spanish, French, Portuguese, Russian
* Backed with Hibernate: tested on Postgres and MySQL
* Bootstrap design/CSS
* Ability to authenticate in web and mobile applications
    * Access token in cookies for web application
    * Access token for mobile application (see mobile app scheme in configuration)
* No open passwords stored
* Exclusion lists (brands, domains, bad words) to avoid particular username selection/impersonation
* Predefined list of countries with phone codes and flags

# Usage
1. Clone this project to your machine
2. Change artifactId, groupId and version to desired values in **pom.xml**
3. Change *.sh startup shortcut files (dev with debug, prod or prod with debug) to reflect changes in pom.xml
4. Develop and use it like you would use any other [Ninja Framework](http://www.ninjaframework.org/) application

# Screenshots


## Sign Up
#### Web
![Sign Up](docs/images/sign-up-web.png)
![Sign Up with country selector](docs/images/sign-up-web-country-selector.png)
#### Mobile
![Sign Up](docs/images/sign-up-mobile.png)




## Sign In
#### Web
![Sign In](docs/images/sign-in-web.png)
#### Mobile
![Sign In mobile](docs/images/sign-in-mobile-small.png)




## Language selector
![Language selector](docs/images/sign-in-mobile-small-language-selector.png)




## User management
#### List of users: web
![List of users](docs/images/admin-users-web.png)
#### List of users: mobile
![Sign In mobile](docs/images/admin-users-mobile.png)
#### Edit personal data
![Personal data](docs/images/admin-users-personal-data-e.png)
#### Edit contact data
![Edit contact data](docs/images/admin-users-contact-data.png)
#### Access management
![Access management](docs/images/admin-users-access.png)
#### Access log
![Access log](docs/images/admin-users-access-log-web-e.png)
#### View access log event
![View access log event](docs/images/admin-users-access-log-event-web.png)
#### Send email to a user
![Send email to a user](docs/images/admin-users-send-email.png)
#### Reset user's password
![Send email to a user](docs/images/admin-users-reset-password.png)
