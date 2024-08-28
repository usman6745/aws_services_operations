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

############ Creation of backup_Plan in given region #############
def aws_backup_plan(aws_BackUp_PlanName, Region, aws_target_backup_vault_name):
    try:
        #Region = 'ca-central-1'
        client = boto3.client('backup', region_name=Region)
        #aws_BackUp_PlanName = "test_backup_plan"
        RecoveryPointTags_key = "test_recovery_key"
        RecoveryPointTags_value = "test_recovery_value"
        aws_backup_plan_ScheduleExpressionTimezone = "Etc/UTC"
        aws_backup_TargetBackupVaultName = aws_target_backup_vault_name

        aws_Backup_Plan_RuleName_Daily = "Daily"
        aws_backup_rule_ScheduleExpression_Daily_rule = "cron(0 2 * * ? *)"
        aws_backup_rule_StartWindowMinutes_Daily_rule = "60"
        aws_backup_rule_CompletionWindowMinutes_Daily_rule = "180"
        aws_backup_rule_DeleteAfterDays_Daily = "7"

        aws_Backup_Plan_RuleName_Weekly = "Weekly"
        aws_backup_rule_ScheduleExpression_Weekly_rule = "cron(00 03 ? * 1 *)"
        aws_backup_rule_StartWindowMinutes_Weekly_rule = "60"
        aws_backup_rule_CompletionWindowMinutes_Weekly_rule = "180"
        aws_backup_rule_DeleteAfterDays_Weekly = "28"


        aws_Backup_Plan_RuleName_Monthly = "Monthly"
        aws_backup_rule_ScheduleExpression_Monthly_rule = "cron(0 04 1 * ? *)"
        aws_backup_rule_StartWindowMinutes_Monthly_rule = "60"
        aws_backup_rule_CompletionWindowMinutes_Monthly_rule = "240"
        aws_backup_rule_DeleteAfterDays_Monthly = "60"

        response = client.create_backup_plan(
            BackupPlan={
                'BackupPlanName': aws_BackUp_PlanName,
                'Rules': [
                    {
                        'RuleName': aws_Backup_Plan_RuleName_Daily,
                        'TargetBackupVaultName': aws_backup_TargetBackupVaultName,
                        'ScheduleExpression': aws_backup_rule_ScheduleExpression_Daily_rule,
                        'StartWindowMinutes': int(aws_backup_rule_StartWindowMinutes_Daily_rule),
                        'CompletionWindowMinutes': int(aws_backup_rule_CompletionWindowMinutes_Daily_rule),
                        'Lifecycle': {
                            #'MoveToColdStorageAfterDays': 123,
                            #'OptInToArchiveForSupportedResources': True|False,
                            'DeleteAfterDays': int(aws_backup_rule_DeleteAfterDays_Daily)
                        },
                        'RecoveryPointTags': {
                            RecoveryPointTags_key: RecoveryPointTags_value
                        },
                        #'EnableContinuousBackup': True|False,
                        'ScheduleExpressionTimezone': aws_backup_plan_ScheduleExpressionTimezone
                    },
                    {
                        'RuleName': aws_Backup_Plan_RuleName_Weekly,
                        'TargetBackupVaultName': aws_backup_TargetBackupVaultName,
                        'ScheduleExpression': aws_backup_rule_ScheduleExpression_Weekly_rule,
                        'StartWindowMinutes': int(aws_backup_rule_StartWindowMinutes_Weekly_rule),
                        'CompletionWindowMinutes': int(aws_backup_rule_CompletionWindowMinutes_Weekly_rule),
                        'Lifecycle': {
                            #'MoveToColdStorageAfterDays': 123,
                            #'OptInToArchiveForSupportedResources': True|False,
                            'DeleteAfterDays': int(aws_backup_rule_DeleteAfterDays_Weekly)
                        },
                        'RecoveryPointTags': {
                            RecoveryPointTags_key: RecoveryPointTags_value
                        },
                        #'EnableContinuousBackup': True|False,
                        'ScheduleExpressionTimezone': aws_backup_plan_ScheduleExpressionTimezone
                    },
                    {
                        'RuleName': aws_Backup_Plan_RuleName_Monthly,
                        'TargetBackupVaultName': aws_backup_TargetBackupVaultName,
                        'ScheduleExpression': aws_backup_rule_ScheduleExpression_Monthly_rule,
                        'StartWindowMinutes': int(aws_backup_rule_StartWindowMinutes_Monthly_rule),
                        'CompletionWindowMinutes': int(aws_backup_rule_CompletionWindowMinutes_Monthly_rule),
                        'Lifecycle': {
                            #'MoveToColdStorageAfterDays': 123,
                            #'OptInToArchiveForSupportedResources': True|False,
                            'DeleteAfterDays': int(aws_backup_rule_DeleteAfterDays_Monthly)
                        },
                        'RecoveryPointTags': {
                            RecoveryPointTags_key: RecoveryPointTags_value
                        },
                        #'EnableContinuousBackup': True|False,
                        'ScheduleExpressionTimezone': aws_backup_plan_ScheduleExpressionTimezone
                    },
                ],
            }
            #BackupPlanTags={
            #    'string': 'string'
            #},
            #CreatorRequestId='string'
        )
        logging.info("Response : "+" "+ str(response))
        return response

    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))

aws_backup_plan(aws_BackUp_PlanName="test_backup_plan", Region="ca-central-1", aws_target_backup_vault_name="test_backup_vault")