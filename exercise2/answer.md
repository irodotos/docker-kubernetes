# Exercise 1
## a)
The yaml file is ex2_1.yaml
`kubectl apply -f ex2_1.yaml`

!["](images/1a.png)

## b)
`kubectl port-forward pod/nginx-pod 8080:80`

!["](images/1b.png)

## c)
`kubectl logs nginx-pod`

!["](images/1c.png)

## d)
`kubectl exec -it nginx-pod -- /bin/sh`

`echo "Welcome to MY nginx!" > /usr/share/nginx/html/index.html`

![](images/1d.png)

## e)
`kubectl cp nginx-pod:/usr/share/nginx/html/index.html index.html`

i change it to have welcome to MY NEW NGINX

`kubectl cp index.html nginx-pod:/usr/share/nginx/html/index.html`

![](images/1e.png)

## f)
`kubectl delete -f ex2_1.yaml`

