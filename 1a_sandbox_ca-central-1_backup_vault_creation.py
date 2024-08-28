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



############ Creation of backup Vault in given region #############
def aws_backup_vault(Region, aws_backup_BackupVaultName):
    #Region = 'ca-central-1'
    #aws_backup_BackupVaultName = 'test_backup_vault'
    try:
        client = boto3.client('kms', region_name=Region)
        key_aliases = client.list_aliases()
        for alias in key_aliases['Aliases']:
            if alias['AliasName'] == 'alias/aws/backup':
                print(alias['TargetKeyId'])
                aws_backup_TargetKeyId = alias['TargetKeyId']
        #print(aws_backup_TargetKeyId)
        logging.info("aws_backup_TargetKeyId : " + " " + aws_backup_TargetKeyId)
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))

    try:
        for alias in key_aliases['Aliases']:
            if alias['AliasName'] == 'alias/aws/backup':
                print(alias['AliasArn'])
                aws_backup_AliasArn = alias['AliasArn']
        #print(aws_backup_AliasArn)
        logging.info("aws_backup_AliasArn : " + " " + aws_backup_AliasArn)
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))

    EncryptionKeyArn_subtract = aws_backup_AliasArn.replace("alias/aws/backup", "")
    EncryptionKeyArn_default_aws_backup = EncryptionKeyArn_subtract+ "key/"+aws_backup_TargetKeyId

    try:
        client = boto3.client('backup', region_name=Region)
        response = client.create_backup_vault(
            BackupVaultName=aws_backup_BackupVaultName,
            EncryptionKeyArn=EncryptionKeyArn_default_aws_backup
        )
        #print(response)
        logging.info(response)
        return response
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))

aws_backup_vault(Region="ca-central-1", aws_backup_BackupVaultName="test_backup_vault")