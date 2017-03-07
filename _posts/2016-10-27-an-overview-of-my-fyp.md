---
layout: post
date: 2016-10-27 14:31
title: "An Overview of my FYP"
description:
comments: false
category:
- uni
- fyp
tags:
- microservices
- Seneca
- serverless
- lambda
---

I am building a serverless platform for Node.js microservices
built using Seneca.js. Seneca is a microservices toolkit for Node.js
which provides mechanisms for clear and concise microservice
interacitons.

Developers who build microservices using Seneca will be able to upload
them to the platform and these microservices will be executed when the
platform receives messages which match the pin of the microservice. The
pin is simply a JSON object with string keys and values such as "role" and
"cmd".

When you split an application into various microservices you will generally
find that some microservices are running much more frequently than
others. Some microservices may be used so infrequently that they do not
warrant the provisioning of a dedicated server so their functionality is
often bundled into other microservices where it does not belong. This is
where the serverless microservices platform steps in. It will handle the
deployment and execution of microservice code in real-time as messages
are sent to the microservice. Multiple microservices can be hosted on the
platform and will appear as though they are operating on discrete servers.

It is similar in many ways to AWS Lambda and Google cloud functions but
it is specifically for Seneca microservices as opposed to standalone
functions. It will also operate seamlessly within a Seneca microservice
architecture, without the need for external API requests.