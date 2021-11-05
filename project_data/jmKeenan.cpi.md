# Quickstart

## backend setup

1. `cd backend`
2. `pip install -r requirements.txt`
3. `ln -s <path_to_cpi_secrets> devops/secret_files`
4. `ln -s devops/secret_files/local_env.json env.json`

## frontend setup

1. `cd frontend`
2. `npm install`


## how to run

1. In one terminal window run the Flask backend:

`./backend/bash/run.sh`


2. In another terminal window run the webpack frontend:

`cd frontend; ./run.sh`


# Documentation

The backend uses a Flask web app deployed to AWS with Ansible, using Postgres as a database.

The frontend uses React, webpack, CSS-Modules. 

## Flask

The entry point into the flask app is hello_webapp/app.py

Flask blueprints are used to handle routes. The routes for the API used by the frontend are contained within
 hello_webapp/api

hello_webapp/helper_routes.py contains non-essential routes for debugging 

hello_webapp/flask_admin_routes.py contains configuration for the Flask admin. A pre-built admin interface which allows Julian to access the database (https://flask-admin.readthedocs.io/en/latest/)

hello_webapp/extensions.py initializes extensions which are then configured in create_app() based on the Flask factory pattern (http://flask.pocoo.org/docs/0.12/patterns/appfactories/)

## SQL-Alchemy

The models for sql-alchemy are contained within hello_models/models.py

The configuration for which database is accessed is configured by hello_settings.py (see more about this below)


## Alembic

Alembic is used for database migrations: http://alembic.zzzcomputing.com/en/latest/tutorial.html
This code is contained within backend/alembic

You can create migrations by running `alembic revision --autogenerate -m "migration name"`

Then editing the new migration in alembic/versions

Then to run migrations on staging, you can locally run this:
`HELLO_FORCE_USE_ENVIRON=STAGING alembic upgrade head`

And to run migrations on prod, you can locally run this:
`HELLO_FORCE_USE_ENVIRON=PROD alembic upgrade head`


## hello_settings.py

hello_settings.py looks for an env.json file in the root of backend which determines many configuration properties for the app, such as which database to connect to, and supplying secrets. 

Ansible ensures that prod and staging having a different env.json file to allow them to work differently.

If you would like to locally simulate the environment of staging or prod, you can set the environmental variable HELLO_FORCE_USE_ENVIRON

This will cause hello_settings.py to look in a different location for env.json (see FORCE_ENVIRON in hello_settings.py to see how this works)


## Deployment

Deployment is configured by Ansible. All deployment code lives in `backend/devops` folder.

There is a staging deployment accessible by `https://staging.cpi-partners.com` 
and prod deployment accessible by `https://cpi-partners.com` 

Staging and production run on independent EC2 machines and have independent databases.

Which database connection is configured by env.json &mdash; this file is stored outside of git so that it can be configured differently on different machines. 

Ansible is used to copy the correct env.json file to the remote machine for the DEV and PROD deployments.

The environment can also be overriden by setting HELLO_FORCE_USE_ENVIRON as an environment variable with one of the three possible values (PROD, STAGING, or TEST).

### server setup

There is a setup Ansible playbook which does some configuration and installs some key dependencies on the server.

This setup script need only be run once on a new machine, and after that you can simply use the deploy scripts to deploy new code to the servers (as well as perform the other tasks in deploy_tasks.yml)

`./backend/bash/setup_server.sh` runs the Ansible setup script on staging and prod (all Ansible scripts are idempotent).

### deploying to staging

1. `git push origin master:staging`
2. `./backend/bash/staging_deploy.sh`

### deploying to prod

1. `git push origin master:prod`
2. `./backend/bash/prod_deploy.sh`


## secret_files

For security, app secrets are stored outside of git. Ansible expects there to be a backend/devops/secret_files folder which is present but not stored in Git. 
Ansible copies over files from this secret_files folder to the severs during deployment (such as API keys and SSL certificates).

To allow for easily syncing secrets between team members, secrets can be stored in a dropbox folder and symlinked to backend/devops/secret_files as desribed in the Quickstart section of this Readme.

## Tests

`./backend/bash/test.sh` - runs a set of test which test the Flask endpoints, using a local test database. 
The connection to this test database is configured in backend/devops/secret_files/test_env.json

These tests are also run whenever you run `./backend/bash/staging_deploy.sh`

## React 

For local development, webpack-dev-server with hot reloading is used.

For staging and production, a bundle is built in frontend/build/staging and frontend/build/prod respectively. 

There are two separate bundles because there are a couple different settings which are configured differently based on the environment. See VarsPlugin in webpack.config.babel.js to see how this works. 

During deployment, Ansible copies over the bundle from your local build to the server.
staging_deploy.sh copies over frontend/build/staging and prod_deploy.sh copies over frontend/build/prod, this is configured by the frontend_dir variable in staging_vars.yml and prod_vars.yml respectively. 

On the server, nginx passes any requests to any url behind /api to Flask,
and serves all other requests from /srv/public directly (this is where the frontend bundle is copied to).

## sending emails

we use amazon SES email service to send emails. SES is currently in sandbox mode, meaning any email 
address we send to needs to be verified through the SES console. 

in the future, we could move SES out of sandbox mode to allow for sending to any email address: move SES email service out of sandbox mode so it can send to any email address: http://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html


## Future



