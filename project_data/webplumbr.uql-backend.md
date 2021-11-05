# UQ Library API - test implementation

## Sample demo
---

[Fetch library details](http://uql-backend.webplumbr.com/api/library/101202)

[Fetch the smallest leaf](http://uql-backend.webplumbr.com/api/findSmallestLeaf?tree=%7B%0D%0A++%22root%22%3A+1%2C%0D%0A++%22left%22%3A+%7B%0D%0A++++%22root%22%3A+7%2C%0D%0A++++%22left%22%3A+%7B%0D%0A++++++%22root%22%3A+2%0D%0A++++%7D%2C%0D%0A++++%22right%22%3A+%7B%0D%0A++++++%22root%22%3A+6%0D%0A++++%7D%0D%0A++%7D%2C%0D%0A++%22right%22%3A+%7B%0D%0A++++%22root%22%3A+5%2C%0D%0A++++%22left%22%3A+%7B%0D%0A++++++%22root%22%3A+9%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D)

```
curl -X GET http://uql-backend.webplumbr.com/api/library/14837

curl -X POST --data url-encoded-library-JSON-object --header "X-VALID-USER: jdoe" http://uql-backend.webplumbr.com/api/library --data url-encoded-JSON-data

curl -X GET http://uql-backend.webplumbr.com/api/findSmallestLeaf?tree=url-encoded-JSON-binary-tree

```

Alternatively, you may use a [Chrome browser App][2] that allows you to test API services by simulating a POST request and supplying additional header information (like the X-VALID-USER).

## Requirements
---

* Laravel 5.1 Framework
* PHP 5.5 or above (and related modules)
* MySQL 5.5 or above
* Apache 2.4 or above
* Linux (Debian) Operating System

## Setup
---

### Composer

For Laravel 5.1 installation, refer to the [Laravel documentation][1].

Make sure you have composer installed on your system. 

```
wget https://getcomposer.org/installer
chmod -v 0755 installer
php installer
sudo mv composer.phar /usr/local/bin/composer
```

After you have cloned this repository, please switch in to the folder and run the following:

```
composer install
```

Then, remove the following file:

```
rm -f vendor/compiled.php
```

Run,

```
composer update
```

### MySQL

Setup MySQL database. Make sure you set the credentials accordingly on your application specific 
environment file `.env`. Here is an example based on credentials available in `.env.example`

```
create database uql;

grant all privileges on uql.* to 'uql'@'localhost' identified by 'sha1-hash-or-whatever';

flush privileges
```

Setup `library` table and seed with dummy data by running the following command in the command-line.

```
php artisan migrate:refresh --seed
```

### Apache2

Use the following apache 2.4 configuration to inform the web server about your virtual host.

```
<VirtualHost *:80>

  ServerName uql-backend.localhost
  DocumentRoot /srv/uql-backend/public

  <Directory /srv/uql-backend>
    AllowOverride All
    Require all granted
  </Directory>

</VirtualHost>
```
Once you have added the above configuration the `/etc/apache2/sites-available/` folder please enable the site and restart the Server.

```
sudo a2ensite uql-backend.conf
sudo service apache2 restart
```
## Testing

To execute default set of test cases, please run the following:

```
phpunit -c phpunit.xml
```

## Troubleshooting
---

If you run in to folder permissions error or 500 Internal Server Error, ensure your Web Server User has appropriate 
write permissions on `storage/` folder

```
sudo chown -R www-data:www-data storage/
sudo chmod -R 0755 storage/
```
**NOTE:** `www-data` is the user and group of your apache2 process. In some linux distributions this could vary.

If you run in to Laravel artisan command's failed to open `bootstrap/cache/services.json` error message, try creating 
the following cache directory under `bootstrap` folder.

```
mkdir bootstrap/cache
```

If you run in to `Command "make:test" is not defined` issue, it is a [known issue in version 5.1][3]. Try creating test
Class manually.

[1]: https://laravel.com/docs/5.1/installation
[2]: https://github.com/postmanlabs/postman-app-support/wiki
[3]: https://github.com/laravel/framework/issues/10224

