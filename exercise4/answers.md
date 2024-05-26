### Exercise 1

#### i) 
``` kubevtl apply -f fruits-crd.yaml```

#### ii)
```kubectl apply -f apple.yaml```

#### iii)
``` kubectl get fruit apple -o yaml```

```
apiVersion: hy548.csd.uoc.gr/v1
kind: Fruit
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"hy548.csd.uoc.gr/v1","kind":"Fruit","metadata":{"annotations":{},"name":"apple","namespace":"default"},"spec":{"count":3,"grams":980,"origin":"Krousonas"}}
  creationTimestamp: "2024-05-25T15:02:35Z"
  generation: 1
  name: apple
  namespace: default
  resourceVersion: "109776"
  uid: e43a56b6-6af5-48e1-9b44-711213564302
spec:
  count: 3
  grams: 980
  origin: Krousonas
```

#### iv)
```kubectl get fruits```

```
NAME    AGE
apple   2m13s
```

### Ecercise 2

all the nessecary files for the exercise are in the folder ex4.2

#### a)
```docker build -t irodotos/hy548:ass4-2 .```

#### b)
```kubectl get pods```
if status is running they are working