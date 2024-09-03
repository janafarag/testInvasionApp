
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run: {command}")
        sys.exit(1)

def main(account_id):
    cluster_name = "kuberNetes-cluster"
    role_name = "WSParticipantRole"
    principal_arn = f"arn:aws:iam::{account_id}:role/WSParticipantRole"

    # AWS EKS Commands
    create_access_entry_command = (
        f"aws eks create-access-entry --cluster-name {cluster_name} "
        f"--principal-arn {principal_arn} --type STANDARD --username wsadmin"
    )

    associate_access_policy_command = (
        f"aws eks associate-access-policy --cluster-name {cluster_name} "
        f"--principal-arn {principal_arn} --access-scope type=cluster "
        f"--policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"
    )

    # Run the commands
    run_command(create_access_entry_command)
    run_command(associate_access_policy_command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <ACCOUNT_ID>")
        sys.exit(1)

    account_id = sys.argv[1]
    main(account_id)