#!/bin/bash
# add .env file to the projects
cp email/configs/.env.conf  email/.env &&
cp media/configs/.env.conf  media/.env &&
cp mqm/configs/.env.conf  mqm/.env &&
cp payment/configs/.env.conf  payment/.env &&
cp doctor/configs/.env.conf  doctor/.env 

input="$1"
if [ "$input" = "development" ]; then
	echo "develpment mode..." &&
	echo "DO NOT USE IN ANY SERVER" &&
	echo "PROJECT ROOT DIR:" &&
	echo $(pwd) &&
	cp configs/docker-compose-development.conf docker-compose.yml &&
	cp email/configs/Dockerfile-develop.conf email/Dockerfile &&
	cp media/configs/Dockerfile-develop.conf media/Dockerfile &&
	cp mqm/configs/Dockerfile-develop.conf mqm/Dockerfile &&
	cp payment/configs/Dockerfile-develop.conf payment/Dockerfile &&
	cp portal/configs/Dockerfile-develop.conf portal/Dockerfile &&
	cp doctor/configs/Dockerfile-develop.conf doctor/Dockerfile &&
	echo "DONE"
elif  [ "$input" = "testing" ]; then
	echo "testing mode..." &&
	cp configs/docker-compose-testing.conf docker-compose.yml &&
	cp email/configs/Dockerfile-test.conf email/Dockerfile &&
	cp media/configs/Dockerfile-test.conf media/Dockerfile &&
	cp mqm/configs/Dockerfile-test.conf mqm/Dockerfile &&
	cp payment/configs/Dockerfile-test.conf payment/Dockerfile &&
	cp portal/configs/Dockerfile-testing.conf portal/Dockerfile &&
	cp doctor/configs/Dockerfile-testing.conf doctor/Dockerfile &&
	echo "DONE"	
else
	echo "production mode" &&
	cp configs/docker-compose-production.conf docker-compose.yml &&
	cp email/configs/Dockerfile-deploy.conf email/Dockerfile &&
	cp media/configs/Dockerfile-deploy.conf media/Dockerfile &&
	cp mqm/configs/Dockerfile-deploy.conf mqm/Dockerfile &&
	cp payment/configs/Dockerfile-deploy.conf payment/Dockerfile &&
	cp portal/configs/Dockerfile-production.conf portal/Dockerfile &&
	cp doctor/configs/Dockerfile-production.conf doctor/Dockerfile &&
	echo "DONE"
fi 

sudo docker-compose build &&
sudo docker-compose up --remove-orphans

