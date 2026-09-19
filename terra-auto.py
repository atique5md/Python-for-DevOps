import subprocess

def terraform_run(command):
    subprocess.run(command, shell=True, check=True)

dir = r"D:\phyton\Devops\terraform" 

#command = f"terraform -chdir={dir} init"
#command = f"terraform -chdir={dir} plan"
# command = f"terraform -chdir={dir} apply -auto-approve"
command = f"terraform -chdir={dir} destroy -auto-approve"


terraform_run(command)
