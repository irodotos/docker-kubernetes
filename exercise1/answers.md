<h2>Exercise1</h2>
<h5>a) Download the images tagged 1.23.3 and 1.23.3-alpine locally</h5>
<code> sudo docker pull nginx:1.23.3</code><br>
<code> sudo docker pull nginx:1.23.3-alpine</code>
<h5>b) Compare the sizes of the two images</h5>
<code> sudo docker images </code>
<p>REPOSITORY   TAG             IMAGE ID       CREATED       SIZE<br>
nginx        1.23.3          904b8cb13b93   2 weeks ago      142MB<br>
nginx        1.23.3-alpine   2bc7edbc3cf2   4 weeks ago     40.7MB<br></p>
<h5>c) Start one of the two images in the background, with the appropriate network
settings to forward port 80 locally and use a browser (or curl or wget) to see that
calls are answered. What is the answer?</h5>
<code> sudo docker run -d -p 8080:80 nginx:1.23.3</code><br>
<code> culr localhost:8080</code>
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
<h5>d) Confirm that the container is running in Docker</h5>
<code> sudo docker ps </code>
<p>CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES<br>
01c2b85ce367   nginx:1.23.3   "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   charming_mcclintock</p>
<h5> e) Get the logs of the running container </h5>
<code> sudo docker logs 01c2b85ce367 </code><br>

```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/03/17 09:50:09 [notice] 1#1: using the "epoll" event method
2023/03/17 09:50:09 [notice] 1#1: nginx/1.23.3
2023/03/17 09:50:09 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/03/17 09:50:09 [notice] 1#1: OS: Linux 5.15.0-58-generic
2023/03/17 09:50:09 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
2023/03/17 09:50:09 [notice] 1#1: start worker processes
2023/03/17 09:50:09 [notice] 1#1: start worker process 29
2023/03/17 09:50:09 [notice] 1#1: start worker process 30
2023/03/17 09:50:09 [notice] 1#1: start worker process 31
2023/03/17 09:50:09 [notice] 1#1: start worker process 32
2023/03/17 09:50:09 [notice] 1#1: start worker process 33
2023/03/17 09:50:09 [notice] 1#1: start worker process 34
2023/03/17 09:50:09 [notice] 1#1: start worker process 35
2023/03/17 09:50:09 [notice] 1#1: start worker process 36
2023/03/17 09:50:09 [notice] 1#1: start worker process 37
2023/03/17 09:50:09 [notice] 1#1: start worker process 38
2023/03/17 09:50:09 [notice] 1#1: start worker process 39
2023/03/17 09:50:09 [notice] 1#1: start worker process 40
2023/03/17 09:50:09 [notice] 1#1: start worker process 41
2023/03/17 09:50:09 [notice] 1#1: start worker process 42
2023/03/17 09:50:09 [notice] 1#1: start worker process 43
2023/03/17 09:50:09 [notice] 1#1: start worker process 44
172.17.0.1 - - [17/Mar/2023:09:56:19 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
2023/03/17 09:56:19 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [17/Mar/2023:09:56:19 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [17/Mar/2023:09:56:58 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/7.87.0" "-"
```
<h5>f) Stop the running container.</h5>
<code> sudo docker stop 01c2b85ce367</code>
<h5> g) Start the stopped container</h5>
<code> sudo docker start 01c2b85ce367</code>
<h5>h) Stop the container and remove it from Docker</h5>
<code> sudo docker stop 01c2b85ce367 </code><br>
<code> sudo docker rm 01c2b85ce367 </code>

<h2>Exercise 2</h2>

<h5>a) Open a shell session inside the running container and change the first sentence
of the default page to "Welcome to MY nginx!". Close the session</h5>
<code> sudo docker start gifted_tereshkova </code>start the container<br>
<code> sudo exec -it gifted_tereshkova /bin/bash</code>start bash in iteractive way<br>
<code> apt update && apt install nano</code>intsall nano<br>
<code> nano /usr/share/nginx/html/index.html</code> edit the file<br>
<h5>b) From your computer's terminal (outside the container) download the default
page locally and upload another one in its place</h5>
i dont know what i have to download but the command to copy an html to the container is <code> sudo docker cp test.html goofy_ptolemy:/usr/share/nginx/html/index.html</code><br>
<h5>Close the container, delete it and start another instance.
c) Do you see the changes? Why;</h5>
We cant see the changes. The changes was on the deleted instance and the new one have the default beacuse this is what we downloaded

<h2> Exercise 3</h2>
<h5>The code that produces the course's website is available on GitHub
(https://github.com/chazapis/hy548). Write down the commands needed to download
the repository (and submodules) and hugo (the tool that builds the website), build the
website locally, and start an Nginx container to serve the CS-548 website instead of the
default page</h5>
1.  we need to install git , make , hugo<br>
2.  git clone https://github.com/chazapis/hy548<br>
3.  cd hy548<br>
4.  make all<br>
5.  cd ..<br>
6.  sudo docker cp hy548/html/public/index.html goofy_ptolemy:/usr/share/nginx/html<br>
For some reason the index.html is just blank
<h2> Exercise 4</h2>
<h5>ollowing the previous exercise, create your own container image, based on Nginx, that
will contain the CS-548 website instead of the default page. Downloading the CS-548
repository (and submodules), hugo and building the site should be done in the
Dockerfile. Create a Docker Hub account and upload the image. Provide</h5>
<h5>a) The Dockerfile</h5>
<h5>b) The command needed to upload the image to Docker Hub</h5>
1. i create a public repository in dockerhub (name: irodotos/nginx-hy548)<br>
2. i need to tag the image with the repository name<br>
   <code>sudo docker tag nginx:1.23.3-alpine irodotos/nginx-hy548:latest</code><br>
3. i need to login in the dockerhub<br>
   <code> sudo docker login</code><br>
4. need to push the image to the hub <br>
   <code> sudo docker push irodotos/nginx-hy548:latest</code><br>
<h5>Explain:
c) How much bigger is your own image than the image you were based on. Why;</h5>
the initial image was 40.7MB but after the build the new image is 115MB. This is beacuse i install some tools (git , make , hugo)
<h5>d) What have you done in the Dockerfile to keep the image as small as possible?</h5>
i remove all the unescessary files that install with the apt update
<h5>5. Upload the Dockerfile from the previous exercise to your GitHub repository. Create a
GitHub Action that will automatically build and push the image to your Docker Hub
account (the workflow should be initiated by the user). Provide the YAML of the
workflow you made</h5>
in the file .github/workflows
