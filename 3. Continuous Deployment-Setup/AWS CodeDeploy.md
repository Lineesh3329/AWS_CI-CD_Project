## Configuring Continuous Deployment
Continuous Deployment (CD) - CodeDeploy: Automatically deploys the tested, packaged application to servers (like EC2, ECS, or Lambda).

1. Create **EC2 Instance**

          1. Goto Amazon EC2
          2. click Launch Instances
          3. Give Instance Name	as Simple-pytho-project
          4. Choose AMI	Ubuntu 22.04 LTS (Jammy) 
          5. Instance Type	t3.micro
          6. Key Pair	Existing key pair
          7. Launch Instance

<img width="1351" height="266" alt="8  ec2instance" src="https://github.com/user-attachments/assets/0cb5115e-2f1e-46df-b549-297a66d66e92" />

-----
2. Create **Tag**

              1. Select your instance             
              2. Go to Tags tab             
              3. Goto Manage tags → Add tag           
              4. Key: Name | Value: sample-python-project

------
3. **CodeDeploy Agent** Installation
- We install the CodeDeploy Agent because it is required to act as the communication bridge between your AWS CodeDeploy service and your target servers(EC2 here).
- It polls AWS to fetch deployment instructions and executes the exact lifecycle hooks defined in our AppSpec.yml file.

          1. In terminal SSH to EC2 instance
  
          The below commands executed for agent installation in EC2 Instance
  
          2. Update system	              - sudo apt update -y
          3. Install dependencies           - (Ruby & wget)	sudo apt install ruby-full wget -y
          4.	Navigate to home directory    - cd /home/ubuntu
          5.	Download CodeDeploy installer - wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install
          6.	Give execute permission	      - chmod +x ./install
          7.	Install CodeDeploy agent      -	sudo ./install auto
          8.	Start CodeDeploy agent        -	sudo service codedeploy-agent start
          9.	Check agent status	          - sudo service codedeploy-agent status
          10. Restart CodeDeploy agent      - sudo service codedeploy-agent status

<img width="1296" height="264" alt="9  codeagent" src="https://github.com/user-attachments/assets/d158943e-57a6-40a5-b72a-97ebc0164438" />

- **active (running)** status shows agent installed successfully.
----

4. Create an **IAM role** & attach it to EC2 Instance

            1. Open AWS Console → IAM → Roles
            2.	Click Create role → Select AWS service → Choose EC2   
            3.	Attach Policies	Add: AmazonEC2RoleforAWSCodeDeploy   
            4.	Give role name -EC2-CodersDeploy-Role

            *Attach this role to creared EC2 instance*

            5.	Click Create role   
            6.  Goto to EC2 → created Instance  
            7.	Choose Instance
            8.	Click Actions → Security → Modify IAM role   
            9.	Select EC2-CodersDeploy-Role   
           10.	Click Update IAM role

<img width="1187" height="286" alt="10  attached iam role" src="https://github.com/user-attachments/assets/d61633d3-287a-4ae7-a52b-d0c1a75407d6" />

----

After Attaching the Role Restart the agent in EC2 Instances by using sudo service codedeploy-agent restart

5. Create **CodeDeploy Application**

            1. Go to → AWS CodeDeploy         
            2. Click → Create application          
            3. Name as sample-python-project           
            4. Compute platform: EC2/On-premises
----

6. Create **Deployment Group**

            1. Deployment Group Name - sample-python-project
            2. Create new role with policy AWSCodeDeployRole
            3. Deployment Type	     - In-place
            4. Environment           - Amazon EC2 instances
            5. Tag key:              - Name
            6. Tag Value:            - sample-python-project


<img width="1358" height="349" alt="11  depgroup" src="https://github.com/user-attachments/assets/b4ce06df-af0d-489a-82e7-c4b6a32ff224" />

-----

7. Create **Deployment**

- **appspec.yml** defines lifecycle events like ApplicationStop and AfterInstall, enabling zero-manual deployments for CodeDeploy.
- This file must be placed inside root of the repo.
- Install Docker in EC2 Instances - `sudo apt install docker.io -y` else it'll show error.

          1	Go to Deployments
          2	Click Create deployment
          3	Deployment Group → Select simple-python-app
          4	Revision Type:	 Source - GitHub
          5	Specify Revision:	lineesh3329/AWS_CI-CD_Project
          7	Click Create deployment

<img width="1138" height="273" alt="12  Deployment succedd" src="https://github.com/user-attachments/assets/0c60defa-ec91-4902-af71-57b1abb67c66" />

-
<img width="1123" height="527" alt="13  deployment succeed" src="https://github.com/user-attachments/assets/66e6c396-0eec-44a6-8d63-f3ae99ec017e" />



   
