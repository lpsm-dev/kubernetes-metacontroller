```bash
kubectl create ns pocs-kubernetes-metacontroller

kubectl -n pocs-kubernetes-metacontroller delete configmap podservice-controller --ignore-not-found
kubectl -n pocs-kubernetes-metacontroller create configmap podservice-controller --from-file=sync.py 

kubectl delete -n pocs-kubernetes-metacontroller -f controller/podservice-controller.yaml --ignore-not-found
kubectl apply -n pocs-kubernetes-metacontroller -f controller/podservice-controller.yaml

kubectl delete -n pocs-kubernetes-metacontroller -f application/podservice.yaml --ignore-not-found
kubectl apply -n pocs-kubernetes-metacontroller -f application/podservice.yaml
```
