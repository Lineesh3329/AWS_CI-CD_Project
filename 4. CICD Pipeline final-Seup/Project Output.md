## Configuring CI/CD AWS Pipeline
                        
  Here we add CodeDeploy to the pipeline and run to confirm the output success.
  
            1. Go to Code pipeline         
            2. Click Code pipeline Application - sample-python-project      
            
            3. Click edit - Add stages
            4. Stage Name - Deploy
            5. Click - Add action Group
            
               - Action Group Name : Codedeploy
               - Action Provider :awscodedeploy
               - Input Artifacts : source
               - Application Name : sample-python-project
               - Deployment Group : sample-python-project1
            
            6. Save the Changes
            7. Click Release Changes

<img width="1362" height="401" alt="14 codedeploydone" src="https://github.com/user-attachments/assets/9d2e1b9d-d0ca-4456-ad79-a2f5deeb0c94" />

## Connecting to EC2 instance

              8. Goto EC2 Instance
              9. Add security Groups ( inbound rule : 5000 )            
              10.In Browser - http://publicip:5000             

###  Success Output : 
<img width="1366" height="691" alt="15  output" src="https://github.com/user-attachments/assets/f1bf0cdd-8c51-4388-af84-72714526bd33" />

-----------
