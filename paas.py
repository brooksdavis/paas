#!/usr/bin/env python3

import boto3
import socket
import time

ec2 = boto3.resource('ec2')


def create_userdata():
    # TODO: create userdata directory
    # TODO: tar up userdata
    with open("userdata.tgz", mode='rb') as file:
        user_data = file.read()
    return user_data


def wait_for_ssh(ip):
    retries = 10
    retry_delay = 10
    retry_count = 0
    while retry_count <= retries:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, 22))
        if result == 0:
            print("", ip)
            break
        else:
            print("instance is still down retrying . . . ")
            time.sleep(retry_delay)


def create_instance(user_data=b'', dry_run=False):
    instances = ec2.create_instances(
        #ImageId='ami-0b70180a3819f0abc',
        ImageId='ami-08cee4c5125dfffac',
        MinCount=1,
        MaxCount=1,
        #InstanceType='t2.micro',
	InstanceType='c6gd.xlarge',
        KeyName='brooks_iam-us-west-2',
        SecurityGroups=['paas-dev'],
        UserData=user_data,
        DryRun=dry_run
    )
    print(instances)
    return instances[0]


def main():
    # TODO: parse args/config file
    user_data = create_userdata()
    instance = create_instance(user_data=user_data)
    print(instance)
    print(f'instance created {instance.id}')
    print("waiting for instance to run")
    instance.wait_until_running()
    instance.reload()
    print(f'instance started at {instance.public_ip_address}')
    print("waiting for ssh to start")
    wait_for_ssh(instance.public_ip_address)

    # TODO: watch s3 for status updates and for the system to shutdown

    # If the instance has shutdown, terminate it
    # instance.terminate()


if __name__ == "__main__":
    main()
