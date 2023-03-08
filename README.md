# argocd-applications

# What this repo does

1) Uses git action pipeline to build and deploy a dockerfile

Instructions

1) Go to the argocd-applications --> applications --> helloworld folder and run the command 'kubectl apply -f . -n argocd' this will deploy the helloworld helm chart in the manifest folder.
2) Go to the argocd-applications --> devops --> (all devops folders) and run the command 'kubectl apply -f -n argocd' this will deploy all devops utilities helm and kustomize such as external dns, k8 certmanager, prometheus etc.
