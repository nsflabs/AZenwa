#!/usr/env python

import subprocess

print("="*30)
print("AZenwa - Azure Post Exploitation Enumeration")
print('\n')
print("by Github: @nsfLabs")
print("="*30)

azLogin = {
    "Login Command":{
        "cmd":"az login --allow-no-subscriptions",
        "message":"Logging into Azure CLI. Your browser will open in some minutes and then you can login manually"
        }
    }

azUserInfo = {
    "All Azure AD Users":{
        "cmd":"az ad user list --output=table --query='[].{Created:createdDateTime,UPN:userPrincipalName,Name:displayName,Title:jobTitle,Department:department,Email:mail,UserId:mailNickname,Phone:telephoneNumber,Mobile:mobile,Enabled:accountEnabled}'",
        "message":"Azure AD Users"
        }
    }

azGroupInfo = {
    "ADGROUP":{
        "cmd":"az ad group list --output=table --query='[].displayName'",
        "message":"Below is a list of Azure AD Groups"
        }
    }


# Execute command module
def execCmd(cmdDict):
    for item in cmdDict:
        cmd = cmdDict[item]["cmd"].split(' ')
        display_message = cmdDict[item]["message"]
        stdout, stderr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()
        stdout = stdout.decode("utf-8")
        outputResult(display_message,stdout)

# Output result on stdout
def outputResult(message,output):
    print("[+] " + message)
    print(output)

# Write result to file
def writeResults(msg, results):
    f = open("result.txt", "a");
    f.write("[+] " + str(len(results)-1) + " " + msg)
    for result in results:
        if result.strip() != "":
            f.write("    " + result.strip())
    f.close()


if __name__ == "__main__":
    print("[*] Logging into Azure CLI...\n")
    execCmd(azLogin)

    print("[*] Getting USER details ...\n")
    azUserInfo = execCmd(azUserInfo)

    print("[*] Getting Azure AD Group Information...\n")
    azGroupInfo = execCmd(azGroupInfo)

    print("Finished")
    print("="*30)
