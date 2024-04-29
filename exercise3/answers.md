# Exercise 1
## a)
`docker build -t irodotos/hy548:helloEnv`

`docker run -p 8080:8080 irodotos/hy548:helloEnv`

`curl 127.0.0.2:8080`

and output is 

`hello from environment variable`

everything is okay

`docker push irodotos/hy548:helloEnv`

`https://hub.docker.com/layers/irodotos/hy548/helloEnv/images/sha256-241b49e39133000e296f02baf97f6d49f88e3c9aaf9f8eb8362274447f90f788?context=repo`
## b)
i created 3 yaml files
`first.yaml`
`second.yaml`
`ingress.yaml`
## c)
`minibube start`

`minikube addons enable ingress`

`kubectl apply -f first.yaml -f second.yaml -f ingress.yaml`

`minikube ip`

The response for the ip is `192.168.49.2`

`curl 192.168.49.2/first`

`curl 192.168.49.2/second`

# Exercise 2

## a)

I change the previus yaml to have the limits, so its the same file with exercise 1

## b)

### 1 client
![alt text](/exercise3/screenshots/1client.png)

we can see each time the svc need to scale 1 by 1. The max scale is 5 replicas beacuse of the 20% cpu means that 5 * 20 = 100% of the cpu

### 100 clients
![alt text](/exercise3/screenshots/100clients.png)

with 100 client we see something different. BEcuse the requests are too much the svc scale to 4 replicas and not 1 by 1

in both examples the second-svc beacuse it not scale it just accept a fix number of request every time

# Exercise 3

The only thing you need to change is the annotation on ingress in the yaml `kubernetes.io/ingress.class: nginx` or to add `ingressClassName: nginx` in the spec of the ingress. Beacuse we change the ingress we need to specify the new to the yaml

# Exercise 4

`helm create third`

i change the files as needed for the exercise

`helm install trird ./third`

![alt text](/exercise3/screenshots/ex4install.png)

![alt text](/exercise3/screenshots/ex4getAll.png)
