---
layout: post
date: 2016-11-19 09:38
title: "The Importance of TDD and Utilising Tooling as a Solo Developer"
description:
comments: false
category:
- uni
- fyp
tags:
- SDLC
- tooling
- TDD
- testing
---

Undertaking a project of this magnitude as a sole developer poses a
number of challenges. I am assumign the role of the developer, the
project manager, the product owner and the tester. I am going to have
to make good use of tooling if I am going to succeed in all of these roles.
I must be diligent in my application of best practices and be careful not to
undertake any unnecessary work.

I will make effective use of existing modules which will help me to avoid
reinventing the wheel. I do not want to spend my time fixing bugs so I know 
that I need to invest time in preventitive measures. I am going to employ test
driven development to help me to stay focused on the task in hand. Test driven
development ties in with the mantra of "start with the end in mind". I should
know exactly how I expect a functioning piece of software to act in certain
defined situations. Developing microservices should help me in this aspect as I
strive to produce small, easy to reason about components.

As beneficial as testing can be, it can be just as time consuming without the
assistance of automation. I will integrate with testing automation tools such as
the continuous integration platform provided by GitLab where my project is being
hosted. This will provide real time feedback about the build status of the project
after each of commit.