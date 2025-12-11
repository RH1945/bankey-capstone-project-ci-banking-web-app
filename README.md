# Bankey - Capstone Project

*(Code Institute Full Stack Developer Programme)*

---

# Index

- [Overview](#overview)
- [UX Design](#ux-design)
- [User Stories](#user-stories)
- [Must Haves](#must-haves)
- [Should Haves](#should-haves)
- [Could Haves](#could-haves)
- [Wireframes](#wireframes)
- [ERD](#erd)
- [Colours](#colors)
- [Font](#font)
- [Key Features](#key-features)
- [User Authentication & Management](#user-authentication--management)
- [Dashboard Overview](#dashboard-overview)
- [Data Management](#data-management)
- [Deployment](#deployment)
- [AI Implementation & Orchestration](#ai-implementation--orchestration)
- [Testing](#testing)
    - [Desktop Lighthouse Reports](#desktop-lighthouse-reports)
    - [Mobile Lighthouse Reports](#mobile-lighthouse-reports)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

---
![]()

# Overview

Bankey is a blog disguised as a banking app where you can create your account, make cards and delete them,
send and receive imaginary money, and check your statement. There are no special differences with the different cards,
and the offers in the index page are sadly not met by this Bank. But regardless of the shortcomings in being a
functioning e-Bank, Banky manages to be a good showcase of CRUD and django, in addition to the awesome animations
and designs you can achieve with a bit of html and css.

This idea is made up of:
1 project
2 apps
1 css
1 main script
4 models
10 views
8 templates + 1 base (9)


<details>
<summary>Read more...</summary>
<br>
I came into this project expecting the functionality of a bank app to be very similar to a blog, which was the aim 
of the capstone, "make your own version of a blog". With a custom model, CRUD functionality and a using the
Object Oriented paradigms. But I actually thought I would be able to add commissions and timed charges for interest and
such things. I have to play with heroku and how it manages cron or other time managers. Maybe there is other
libraries for setting up a regular payment, or a date to charge a cardholder if they owe money on their credit card.

I really think it works fine for what it ended up being, but it's not something I'm happy with. Although
the idea of the project is "banking", it would require a lot more knowledge about security, pipelines,
and other aspects I currently ignore.

In general, I had thought of making a banking app because it appeared to me that it was a more math-demanding subject
for the capstone project. I like that. In the end, I didn't have time to add the functionality to charge transaction
fees, interest rates or other common calculations that happen during the banking experience, but perhaps in the future.

the timeline of the project basically was 3 weeks to get it to a more than "should have" level, but the couple of
issues I encountered in the first two weeks rendered models and deployment a longer task than anticipated. I spent
the first two weeks building most of the back end and the last week in designing and polishing what you end up
seeing now. the styles and templates.

Models were all custom, the User model was a bit more demanding given that the standard Django models don't have
a date of birth, and I was a bit stubborn in having it be part of the (utils.py) account number function.
The other problem I faced was databases, it seemed that my neon database was not set up properly somehow in settings.py,
this made it impossible to have a deployed version with a global database. The settings were for some reason just not
working in general, when trying to deploy in a local server the templates refused to connect, this was fixed by
rebooting the settings file and just connecting the dependencies and apps again. Aside from that, small problems like
styling and some bad pagination were fixed in the last couple of days.

All in all, the project's MVP felt finished, and I am happy to submit after sharing the heroku site with some CS friends
and my CI tutors and facilitators, having made improvements after hearing their comments. I hope to make many more, and
better apps in future hackathons, expanding on this idea and related subjects :)

</details>

![Overview Image Placeholder]()



---

# UX Design

<details>
<summary>Dashboard wireframe vs Actual</summary>
<br>

![wireframes index.png](static/readme/wireframes%20index.png)
![fl index.png](static/readme/fl%20index.png)

</details>
<details>
<summary>Cards wireframe vs Actual</summary>
<br>

![wireframes cards.png](static/readme/wireframes%20cards.png)
![fl cards.png](static/readme/fl%20cards.png)

</details><details>
<summary>wireframe vs Actual</summary>
<br>

![]()
![]()
</details><details>
<summary></summary>
<br>

![]()
![]()
</details>wireframe vs Actual<details>
<summary></summary>
<br>

![]()
![]()

</details>

### Reasoning

<details>
<summary></summary>
<br>

</details>
My thought process for the templates was so:

I need to be able to display the "base" everywhere, this includes
the navbar and the footer only. So, I needed **base.html**.

I need to display a main page that informs the user of steps to take to sign up / log in, just as
important, we want to create an inviting feeling by communicating the value of joining the bank and the
advantages of different accounts and cards. So, I used **index.html**.

I wanted a feel of ease and brevity for the sign-up and log-in, so I use a different file for each. There is *
*log_in.html** and **sign_up.html**.

I took inspiration from my own (real) banking app and wanted to be able to show the customer's profile
in a way that was easy to use, and that only showed the most important data/information for the user's convenience.
Hence, I need **account.html**.

I also knew I needed a secure feel for the transactions, I wanted the look to help the user
focus more on their transaction so they could feel confident in typing and having the right info.
So I made **transactions.html**.
---

# User Stories

<details>
<summary></summary>
<br>

</details>

---

# Must Haves

<details>
<summary></summary>
<br>

</details>


---

# Should Haves

<details>
<summary></summary>
<br>

</details>


---

# Could Haves

<details>
<summary></summary>
<br>

</details>


---

# Wireframes

![Wireframe Placeholder]()

<details>
<summary></summary>
<br>

</details>

---

# ERD

<details>
<summary></summary>
<br>

</details>

![ERD Placeholder]()



---

# Colors

<details>
<summary></summary>
<br>

</details>
![Colours Placeholder]()



---

# Font

<details>
<summary></summary>
<br>

</details>
![Font Placeholder]()




---

# Key Features

<details>
<summary></summary>
<br>

</details>


---

# User Authentication & Management

<details>
<summary></summary>
<br>

</details>
![Authentication Placeholder]()







---

# Dashboard Overview

![Dashboard Placeholder]()




---

# Data Management

![Data Management Placeholder]()




---

# Deployment

---

# AI Implementation & Orchestration

![AI Diagram Placeholder]()




---

# Testing

## Desktop Lighthouse Reports

![Desktop Lighthouse Report]()




---

## Mobile Lighthouse Reports

![Mobile Lighthouse Report]()




---

## HTML Validation

![HTML Validation Screenshot]()




---

## CSS Validation

![CSS Validation Screenshot]()




---

## Python Validation

![Python Validation Screenshot]()




---

## JavaScript Validation

markdown
![JS Validation Screenshot]()




---

## Manual Testing

---

## Automated Testing

<details>
<summary></summary>
<br>

</details>

---

# Future Enhancements

---

# Credits

_This project is dedicated to my unfinished degree in Economics and Finance in Portugal._
