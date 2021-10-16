# vuln-web-app

Vulnerable Web Application and Security Assessment Tools.

## Description

This is web application with vulnability.  
Let's try security assessment and recode to secure!!

Also, this web application is written by FastAPI. The reason is that it is being able to write high readability and clean code.

## Setup

#### Setup Web App

```
$ sudo bash install.sh
```

#### Install Burp Suite

```
# file from here: [Link](https://portswigger.net/burp/releases/)  
[Burp Suite Community Edition] [Linux (64-bit)] ***[Download]***

$ sh burpsuite_community_linux_[version].sh
```

#### Install OWASP ZAP

```
$ sudo apt install default-jre openjdk-11-jre-headless

$ wget https://github.com/zaproxy/zaproxy/releases/download/v2.10.0/ZAP_2_10_0_unix.sh

$ sudo sh ZAP_2_10_0_unix.sh
```

## Support Vulnability

* XSS (Stored, Reflected, ...)
* SQL Injection
* CSRF
* OS Injection & Directory Traversal
* ~~Buffer Overflow~~

## LICENSE

[MIT]()

## Quote

* [PAKUTASO](https://www.pakutaso.com/)
