import os
import subprocess
import argparse

def run_command(command):
    """Run a shell command."""
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def install_eksctl():
    """Install eksctl."""
    run_command('curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp')
    run_command('sudo mv /tmp/eksctl /usr/local/bin')
    run_command('eksctl version')

def create_iam_policy():
    """Create IAM policy for the AWS Load Balancer Controller."""
    run_command('curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json')
    run_command('aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam-policy.json')

def create_service_account(account_id, region):
    """Create Kubernetes service account for AWS Load Balancer Controller using eksctl."""
    # Associate IAM OIDC provider
    run_command(f"eksctl utils associate-iam-oidc-provider --region {region} --cluster kuberNetes-cluster --approve")

    # Create the service account with the IAM policy
    service_account_cmd = (
        f"eksctl create iamserviceaccount "
        f"--cluster=kuberNetes-cluster "
        f"--namespace=kube-system "
        f"--name=aws-load-balancer-controller "
        f"--attach-policy-arn=arn:aws:iam::{account_id}:policy/AWSLoadBalancerControllerIAMPolicy "
        f"--override-existing-serviceaccounts "
        f"--approve"
    )
    run_command(service_account_cmd)

def install_helm():
    """Install Helm."""
    run_command("curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3")
    run_command("chmod 700 get_helm.sh")
    run_command("./get_helm.sh")

def install_aws_load_balancer_controller(region, vpc_id):
    """Install AWS Load Balancer Controller using Helm."""
    # Add the EKS chart repo to Helm
    run_command("helm repo add eks https://aws.github.io/eks-charts")

    # Install the AWS Load Balancer Controller
    helm_install_cmd = (
        f"helm install aws-load-balancer-controller eks/aws-load-balancer-controller "
        f"-n kube-system "
        f"--set clusterName=kuberNetes-cluster "
        f"--set serviceAccount.create=false "
        f"--set region={region} "
        f"--set vpcId={vpc_id} "
        f"--set serviceAccount.name=aws-load-balancer-controller"
    )
    run_command(helm_install_cmd)

def main():
    parser = argparse.ArgumentParser(description="Install AWS Load Balancer Controller")
    parser.add_argument("--account_id", required=True, help="AWS Account ID")
    parser.add_argument("--region", required=True, help="AWS Region")
    parser.add_argument("--vpc_id", required=True, help="VPC ID")

    args = parser.parse_args()

    # Install eksctl
    install_eksctl()

    # Create IAM policy
    create_iam_policy()

    # Create Kubernetes service account
    create_service_account(args.account_id, args.region)

    # Install Helm
    install_helm()

    # Install AWS Load Balancer Controller
    install_aws_load_balancer_controller(args.region, args.vpc_id)

if __name__ == "__main__":
    main()
