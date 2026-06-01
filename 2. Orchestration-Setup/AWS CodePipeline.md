## Orchestration- AWS CodePipeline
Orchestration - CodePipeline: The conductor. It links all the tools together, managing the flow from code commit through the build and deployment stages

1. Goto AWS Console

2. Choose → **CodePipeline**

3. Click → **Create pipeline**

4. Choose Creation Option - **Build Custom Pipeline**

5. **Pipeline Configuration**

        Pipeline Name  - sample-python-project

        Execution Mode - Queued
   
        Service Role   - Auto created new service role
   
        Role Name	    - AWSCodePipelineServiceRole-us-east-1-sample-python-project

6. **Attach an IAM policy** to AWS Codepipeline service role to allow access to AWS CodeBuild and AWS CodeDeploy.

7. **Source Stage Configuration**

        Source Provider	- GitHub (via GitHub Outh)
   
        Configure GitHub connection
   
        Repository Name	- lineesh3329/AWS_CI-CD_Project
   
        Default Branch	- main
   
        Output Artifact Format as	CodePipeline default
   
        Change Detection	to be Enabled (Webhook trigger)

8. **Build Stage Configuration**

        Build Provider  - Other build providers
   
        Provider Type	 -  AWS CodeBuild
   
        Project Name   -	sample-python-project
   
        Environment Variables	Not configured (optional)
   
        Build Type	- Single build

        Note: Skipped Test stage and Deployment stage here.

9. Click - **Create CodePipeline**

   <img width="1252" height="492" alt="6  pipeline" src="https://github.com/user-attachments/assets/59ad8d26-c2e8-4969-8440-5b1a45c11e2d" />

----

