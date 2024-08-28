import boto3
import json
import logging
# Create and configure logging
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
'''                    
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
############ Creation of backup plan resource selection in given region #############

def aws_backup_plan_dual_resource_selection_creation(Region, aws_created_backup_plan_name, aws_backup_SelectionName_ec2_ebs):

    try:
        ### Get BackupPlan details using BackupPlanId ###
        client = boto3.client('backup', region_name=Region)
        response = client.list_backup_plans(
            MaxResults=123
        )
        print(response['BackupPlansList'])
        aws_backup_plans_list = (response['BackupPlansList'])
        for get_backup_plan_id in aws_backup_plans_list:
            if get_backup_plan_id["BackupPlanName"] == aws_created_backup_plan_name:
                aws_BackupPlanId = get_backup_plan_id['BackupPlanId']
                print(aws_BackupPlanId)
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))

    try:
        ### Get the default IAM Role with name AWSBackupDefaultServiceRole ###       
        client = boto3.client('iam', region_name = Region)
        response = client.get_role(
            RoleName='AWSBackupDefaultServiceRole'
        )
        aws_backup_Default_ServiceRole = (response['Role']['Arn'])
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))   

    try:
        ### Creation of backup_selection - Resource Assignments ###
        #Assuming we have EC2 Instances with tags ec2_test_key:ec2_test_value
        #EBS Volumes with tags ebs_test_key:ebs_test_value
        client = boto3.client('backup', region_name=Region)
        response = client.create_backup_selection(
            BackupPlanId = aws_BackupPlanId,
            BackupSelection={
                'SelectionName': aws_backup_SelectionName_ec2_ebs,
                'IamRoleArn': aws_backup_Default_ServiceRole,
                'Resources': [],
                'ListOfTags': [
                    # Condition for EC2 instances
                    {
                        'ConditionType': 'STRINGEQUALS',
                        'ConditionKey': 'ec2_test_key',
                        'ConditionValue': 'ec2_test_value'
                    },
                    # Condition for EBS volumes
                    {
                        'ConditionType': 'STRINGEQUALS',
                        'ConditionKey': 'ebs_test_key',
                        'ConditionValue': 'ebs_test_value'
                    }
                ],
                'Resources': [],
            }
            #CreatorRequestId='string'
        )
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))   

aws_backup_plan_dual_resource_selection_creation(Region="ca-central-1", aws_created_backup_plan_name="test_backup_plan", aws_backup_SelectionName_ec2_ebs="test_backup_selections_ec2_ebs")