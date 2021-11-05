Basic-Python-RESTful-Server
===========================

A basic python RESTful Server in Flask integrated with Luminoso Python Client

## Problem to solve

We had an issue in that our web application was developed in PHP and that we had a new requirement in interfacing our web application with the Luminoso API. Luminoso have a Python Client to do the authentication with their server.

## How we solved it

We decide to create a basic python RESTful server and include the Luminoso Python client library in the calls.

## Requirements

1. Flask micro framework - http://flask.pocoo.org/
2. Luminoso python client - https://github.com/LuminosoInsight/luminoso-api-client-python

## How to setup

During development we setup an virtual environment, here is how we did that.

If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

$ sudo easy_install virtualenv
or even better:

$ sudo pip install virtualenv

Once you have virtualenv installed, just fire up a shell and create your own environment. We created a project folder and a venv folder within:

$ mkdir myproject

$ cd myproject

$ virtualenv env

New python executable in env/bin/python

Installing distribute............done.

Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

$ . env/bin/activate

If you are a Windows user, the following command is for you:

$ env\scripts\activate

Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).

Now you can just enter the following command to get Flask activated in your virtualenv:

$ pip install Flask

A few seconds later and you are good to go.

As I'm going to use the Luminoso Python client, I need to install it

$ pip install luminoso_api

## Run the rest-server

$ python rest-server.py &

You can test it from a browser or a RESTful client

http://127.0.0.1:5000/api/v1.0/test

## PHP Code

The web application is built on codeigniter, here is how we code the call i PHP to call the basic python RESTful server

	public function get_luminoso_score($project_name, $article_text) 
	{
		// Load the rest client spark
		$this->load->spark('restclient/2.1.0');
		// Load the library
		$this->load->library('rest');
		
		// Set config options (only 'server' is required to work)
		$config = array('server' =>	'http://localhost:5000/');
		// Run some setup
		$this->rest->initialize($config);
		
		$this->rest->format('application/json');
		
		$param = array('project_name' => $project_name,
						'article_text' => $article_text,
						'luminoso_account' => Settings::get('luminoso_account'), 
						'luminoso_account_name' => Settings::get('luminoso_account_name'),
						'luminoso_password' => Settings::get('luminoso_password'));
		
		$json = json_decode($this->rest->get('api/v1.0/get_correlation', $param), true);
		
		if ($json) 
		{
			return $json;
		}
		else {
			log_message('error', 'Bad response from Luminoso');
			return false;
		}
	}


## How to adopt for other python clients

It is easy to adopt for other python clients - just replace the Luminoso python client details with the python client that you need to use.

