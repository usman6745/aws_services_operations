## Configuring AWS Creds Locally SSO Method
#####  Open the AWS_SSO startup URL Page and select the account that you have access. Here is a reference attached below : 

![Get_URL_From_AWS_SSO_Startup_Page](reference_images/Get_URL_From_AWS_SSO_Startup_Page.png)

- Configure the credentials as shown in the below image :
```
aws configure sso
```

![Configure_AWS_CLI_SSO](reference_images/Configure_AWS_CLI_SSO.png)


![Code_Entry_From_CLI_in_AWS_Authentication_Console](reference_images/Code_Entry_From_CLI_in_AWS_Authentication_Console.png)

##### once authenciation made, Export the profile you have set
```
#export AWS_PROFILE=<test_profile>
```
Test the AWS CLI Access
Ex commands :
```
aws backup get-backup-plan --backup-plan-id <aws_somename_*****-99c3-e69*****ad> --region ap-northeast-1 --profile <Profile_Name>

aws backup list-backup-jobs --by-backup-vault-name <aws_backup_vault_name> --region ap-northeast-1 --profile <Profile_Name>

aws backup list-backup-selections --backup-plan-id <_*****-99c3-e69*****ad1> --region ap-northeast-1 --profile <Profiile_Name>

```
