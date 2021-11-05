## Hackoregon Application Deployment Playbooks

### Prerequisites
-----------------
**These instructions assume NPM is installed on your machine**
#### Install AWS CLI
* Mac OSX
```
 $ sudo pip install awscli --ignore-installed six
 ```
* Ubuntu
```
$ curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
$ unzip awscli-bundle.zip
$ sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
```
Configure AWS CLI, replacing Access ID and Secret key with deployment credentials provided by DevOps team
```
$ aws configure
AWS Access Key ID [None]: XXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXX
Default region name [None]: us-west-2
Default output format [None]: ENTER
```
Ensure you have have access to HackOregon's AWS S3 buckets
```
$ aws s3 ls
```
You should see something like this on the command line:
```
2016-06-14 14:19:22 hacko-fonts
2016-02-08 15:34:51 hackoregon-dst
2016-06-09 18:50:00 plot-pdx
2016-06-09 18:52:02 plotpdx.org
2014-04-11 13:31:16 voter-reg
2016-06-17 11:28:02 www.cropcompass.org
2016-06-09 22:47:36 www.plotpdx.org
2016-06-17 17:28:44 www.programmingforprogress.org
```
#### Install Ansible
* Mac OSX
```
$ sudo easy_install pip
$ sudo pip install ansible
```
* Ubuntu
```
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
```
#### Get the application deployment playbooks

```
git clone https://github.com/hackoregon/application-provisioning
```

#### Create your credential file using ansible-vault
Create your vault credentials.
* For the ***Cropcompass frontend:***
```
ansible-vault create cropcompass-frontend/group_vars/all/vault
```
* For the ***Education frontend:***
```
ansible-vault create education-frontend/group_vars/all/vault
```
* For the ***Hunger frontend:***
```
ansible-vault create hunger-frontend/group_vars/all/vault
```
Edit the file, replacing x's with deployment credentials provided by DevOps team
```
aws_access_key: xxxxxxxxxxxxxxxxxxxx
aws_secret_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
* Note: You can save the vault file outside of the repo directory and just copy the to the appropriate **group/vars/all/vault** directory and skip this step if you need to pull the repo again

Create password file using password used to create the vault file by editing
```
$ vi ~/.vault_pass.txt
```
then:
```
$ chmod 600 ~/.vault_pass.txt
```

### Deploying the static websites
---------------------------------
From your local repo root:

* Cropcompass front end deploy
```
$ cd crompcompass-frontend
./deployCropcompassFrontend.sh
```
* Education front end deploy
```
$ cd education-frontend
./deployEducationFrontend.sh
```

* Hunger front end deploy
```
$ cd hunger-frontend
./deployHungerFrontend.sh
```
