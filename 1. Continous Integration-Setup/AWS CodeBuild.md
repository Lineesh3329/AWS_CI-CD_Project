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

6. To allow access to AWS Systems Manager Parameter Store by AWS CodeBuild **Attach an IAM policy** to that service role
   - Go to IAM Role Used by CodeBuild

   - Search your role: **codebuild-sample-python-project-service-role**

   - Click the role

   - Add permissions → Attach policies

   - Give: **AmazonSSMfullAccess** which gives access to Parameter Store
-----

7. Again go back to AWS CodeBuild. Click **Create Build Project**

<img width="1335" height="367" alt="2  Buildproject crested" src="https://github.com/user-attachments/assets/711ef9c7-8dd0-4923-8a73-910d72d6ab2d" />

-------

8. Click **Start Build**

<img width="1142" height="377" alt="3  Build started" src="https://github.com/user-attachments/assets/b36e2660-6b6d-41fa-a468-8e106caf23ff" />

<img width="686" height="108" alt="4  build code succed" src="https://github.com/user-attachments/assets/b94b97c9-5e9d-42bc-baf3-eaae6603a079" />

-----

9. Image pushed from CodeBuild to our **Docker Hub repo** confirmed successfully.

<img width="1354" height="374" alt="5 docker confirmed" src="https://github.com/user-attachments/assets/217e1d4d-cde4-4c56-a4d1-cbbf62c383bc" />
 
