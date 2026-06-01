# Continous Integration-Setup
## AWS CodeBuild Setup:
1. Go to AWS Console

2. Search → **CodeBuild**

3. Click Create **Build Project**

4. **Project Configuration**

    - Project name: sample-python-project

    - Project Type: Default Project

    - Source Provider: **GitHub** - Click Connect to GitHub and Authorize AWS

    - Environment Settings: Give the Settings value as mentioned below in table

    - Buildspec Configuration - Use a buildspec file ( pre configured ) or Insert build Commands ( give commands )

------
   **Environment Settings**
      
      1. Environment Image as Managed Image
      
      2. Operating System	as Ubuntu
      
      3. Runtime as Standard
      
      4. Image as aws/codebuild/standard:latest

      5. Service Role	as automatically created service role
  
  -------
  5. To store secure data **AWS System Manager** used
      1. AWS console → System Manager
      
      2. Search: Systems Manager
      
      3. Click → Parameter Store
      
      4. Click → Create parameter       
      
      5. Give the values mentioned as below      
      
                Name  -	/myapp/docker/username
                Type  -	SecureString
                Value -	Your Docker username (or any sensitive credential)
                KMS   - Key	Default

                Note:  Can create multiple parameters for password, registry url as required

<img width="1340" height="530" alt="1paramater store" src="https://github.com/user-attachments/assets/c6adba75-c907-441a-a9e7-8ca5ff32a61d" />

---
