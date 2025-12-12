# Bankey - Capstone Project

*( For Code Institute Full Stack Developer Programme)*

## [CHECK THE DEPLOYED SITE HERE!](https://bankey-76bdd08d1577.herokuapp.com/)

(Might take a moment to warm up, the website is dormant while not used)

---

### Here's a full walkthrough of the deployed site

[![Bankey Walkthrough](static/readme/yt%20vid%20template.gif)](https://youtu.be/JMLCL7Gjmak)

# Index

- [Overview](#overview)
- [UX Design](#ux-design)
- [User Stories](#user-stories)
- [ERD](#erd)
- [Colours](#colors)
- [Font](#font)
- [Key Features](#key-features)
- [User Authentication & Management](#user-authentication--management)
- [Data Management](#data-management)
- [Deployment](#deployment)
- [AI Implementation & Orchestration](#ai-implementation)
- [Testing](#testing)
    - [Desktop Lighthouse Reports](#desktop-lighthouse-reports)
    - [Mobile Lighthouse Reports](#mobile-lighthouse-reports)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Manual Testing](#manual-testing)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

---

# Overview

Bankey is a blog disguised as a banking app where you can create your account, make cards and delete them,
send and receive imaginary money, and check your statement. There are no special differences with the different cards,
and the offers in the index page are sadly not met by this Bank. But regardless of the shortcomings in being a
functioning e-Bank, Banky manages to be a good showcase of CRUD and django, in addition to the awesome animations
and designs you can achieve with a bit of html and css. One thing to be aware of is that mobile was not first for this
project, most banks seem to have a totally different app and website. I was careful to have responsiveness for small
screens, but in this case, it was not as important as the main desktop view.

This idea is made up of:

- 1 project
- 2 apps
- 1 css
- 1 main script
- 4 models
- 10 views
- 8 templates + 1 base (9)

<details>
<summary> Read more... </summary>
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

---

# UX Design

The first idea of this simple look came about by remembering my first project, nervous health
which had an easy navigation. The main feature I needed for the index was a CTA that connected to the key features,
and the rest could be filler content.

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
</details>

<details>
<summary>Statement wireframe vs Actual</summary>
<br>

![wireframes statement.png](static/readme/wireframes%20statement.png)
![fl statement.png](static/readme/fl%20statement.png)
</details>

<details>
<summary>Transaction wireframe vs Actual</summary>
<br>

![wireframes transactions.png](static/readme/wireframes%20transactions.png)
![fl transactions.png](static/readme/fl%20transactions.png)
</details>

### Templates reasoning

<details>
<summary>My thought process for the templates was so:</summary>
<br>

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
</details>

---

# User Stories

For my user stories I believed that most of the thought process was focused on the django models so The user stories 
loosely relate to models and to views. THe main focus of these was tracking goals and snapshot-like parts of the 
project. 

An obvious "Must-have" is login and authetification, the first step of the blog idea is to have users who can "post"
and hence track the "authors" of these. In this Bank version of a blog you must be authentificated to trade and 
create cards. This is crucial to the experience.

A "Could-have" story is the transaction detail modal which you can see when selecting a transaction from the statement
template view. Here you will get a detailed view of the transaction. It wasn't necessary, so I added it because there
was a bit of time to spare. It enhances the user's comfort by confirming the details of the transaction. 

---


( ノ ^o^)ノ

---

# ERD

<details>
<summary>The Entity relationship models are essential. Mainly, to plan the look of the site, movement and interactitivity
of the user and the scope of the project.
Hence, they were looked at carefully and laid out from the inception of the project. Read more...</summary>
<br>

## Relationship Summary

| From          | To                     | Relationship | On Delete |
|---------------|------------------------|--------------|-----------|
| User          | BankeyAccount          | One-to-Many  | CASCADE   |
| BankeyAccount | Card                   | One-to-Many  | CASCADE   |
| User          | Transaction (sender)   | One-to-Many  | CASCADE   |
| User          | Transaction (receiver) | One-to-Many  | CASCADE   |
| Card          | Transaction            | One-to-Many  | SET_NULL  |

ERD cardinality Overview:

-User
-├── 0..* BankeyAccount
-│ ├── 0..* Card
-│ │ └── 0..* Transaction
-│
-├── 0..* Transaction (as sender)
-└── 0..* Transaction (as receiver)

<details>
<summary>User (extends Django AbstractUser)</summary>
<br>

| Field Name  | Type          | Constraints               | Description                          |
|-------------|---------------|---------------------------|--------------------------------------|
| id          | AutoField     | PK                        | Unique user identifier               |
| username    | CharField     | unique, required          | Login username                       |
| email       | EmailField    | optional                  | User email address                   |
| first_name  | CharField     | optional                  | User first name                      |
| last_name   | CharField     | optional                  | User last name                       |
| full_name   | CharField     | auto-generated, read-only | Concatenation of first and last name |
| dob         | DateField     | null, blank               | Date of birth                        |
| password    | CharField     | required                  | Hashed password                      |
| is_active   | BooleanField  | default=True              | Account active status                |
| is_staff    | BooleanField  | default=False             | Admin access                         |
| date_joined | DateTimeField | auto                      | Registration timestamp               |

</details>
<details>
<summary>BankeyAccount</summary>
<br>

| Field Name  | Type              | Constraints | Description                |
|-------------|-------------------|-------------|----------------------------|
| id          | AutoField         | PK          | Unique account identifier  |
| user        | ForeignKey → User | CASCADE     | Account owner              |
| acc_balance | DecimalField      | default=0   | Total account balance      |
| acc_type    | IntegerField      | choices     | Personal / Business / None |
| acc_number  | CharField         | unique      | Generated account number   |
| currency    | CharField         | choices     | Account currency           |
| created_on  | DateTimeField     | auto        | Account creation timestamp |

</details>

<details>
<summary>Card</summary>
<br>

| Field Name      | Type                       | Constraints | Description               |
|-----------------|----------------------------|-------------|---------------------------|
| id              | AutoField                  | PK          | Unique card identifier    |
| account         | ForeignKey → BankeyAccount | CASCADE     | Owning account            |
| card_balance    | DecimalField               | default=0   | Card balance              |
| card_number     | CharField                  | unique      | Generated card number     |
| expiration_date | DateField                  | default     | Expiry date               |
| card_type       | IntegerField               | choices     | Debit / Credit / Business |
| created_on      | DateTimeField              | auto        | Card creation timestamp   |

</details>

<details>
<summary>Transaction</summary>
<br>

| Field Name | Type              | Constraints    | Description                    |
|------------|-------------------|----------------|--------------------------------|
| id         | AutoField         | PK             | Unique transaction identifier  |
| reference  | CharField         | blank          | Optional transaction reference |
| sender     | ForeignKey → User | CASCADE        | User sending funds             |
| receiver   | ForeignKey → User | CASCADE        | User receiving funds           |
| card       | ForeignKey → Card | NULL, SET_NULL | Card used (can be deleted)     |
| amount     | DecimalField      | required       | Transaction amount             |
| timestamp  | DateTimeField     | auto           | Transaction timestamp          |

</details>


This was the first sketch for the ERDs:
![ERD.png](static/readme/ERD.png)

</details>

---

## Colors

<details>
<summary>The color palette was chosen very early on and stayed mostly unchanged throughout the project. I wanted something that
felt slightly artificial and glossy, closer to a “concept bank” than a real one...</summary>
<br>

...With gradients doing most of the heavy lifting. Dark backgrounds help the cards and UI elements pop, while the warmer
gradients give the illusion of something
friendly and premium, even if the functionality underneath is deliberately simple.

Most colours are defined as CSS variables in a single file, which made it easier to tweak contrast and visibility late
in the project without breaking layouts. This was especially useful when adjusting accessibility issues and making sure
that important information, such as balances and transaction states, remained readable across different screen sizes.

![Colors.png](static/readme/Colors.png)

</details>

---

## Font

<details>
<summary>The two fonts are BIZ UDPMincho and Google Sans Code</summary>
<br>

Basically I looked for business fonts in google fonts and these two came up, I liked them, so I used them.
I chose BIZ serif for headings and identity, and a Google sans font for numbers and technical content
like card numbers and balances. This was done to subtly separate
“human” content from “system” content, even if most users would never consciously notice it.

The fonts are imported globally and referenced via CSS variables, which allowed consistent usage across templates. Font
sizes were adjusted several times during responsive testing, particularly for the card number display, which proved to
be more fragile than expected on smaller screens.

![fonts.png](static/readme/fonts.png)

</details>

---

## Agile Development

Bankey was developed using Agile principles, embracing iterative development, continuous feedback, and incremental
delivery throughout the project lifecycle. Rather than planning all functionality in a single upfront phase, the project
evolved through short development cycles focused on delivering usable features early and improving them based on real
progress and testing outcomes.

All development tasks, user stories, and enhancements were tracked using the GitHub Project Board,
which provided a real-time snapshot of progress and helped prioritize what needed attention next. You can explore the
live board here: https://github.com/users/RH1945/projects/7

On this board, tasks moved across the columns:
- Backlog — Features and ideas yet to be worked on
- To Do — Items planned for the next development cycle
- In Progress — Currently being implemented
- Done — Fully implemented and tested features
This structure ensured that development remained flexible, transparent, and focused on achievable goals.

The project was broken into meaningful chunks that could be delivered and demonstrated independently. A sample
progression of deliverable waves included:

User Authentication & Management — First vertical slice of core functionality
Account & Card Creation — Enabling CRUD operations for crucial models
Transaction System — Allowing send/receive flows with feedback UX
Statement & Pagination — Data listing with filtering and AJAX enhancements
Enhanced UX Features — Color coding, modals, banners, animations
Polish and Deployment — Refinement, responsive fixes, and live deployment

For example, pagination was initially planned as a simple page navigation but evolved into an AJAX-driven “Load More”
feature once the UI patterns demanded smoother interaction.

Continuous Integration of Learning:
Agile here wasn’t just about task tracking: it became a process of learning by doing. Bankey’s development integrated:
classroom concepts, real-world design patterns, collaborative refinement (by asking tutors and peers for feedback)

This made the project both a technical exercise and a practical lesson in flexible delivery under evolving requirements.

---

# Key Features

<details>
<summary>Creating cards and performing transactions are the focus of this app.</summary>
<br>

At its core, Bankey supports basic CRUD operations disguised as banking actions: users can create accounts, issue cards,
perform transactions, and review statements. None of these actions involve real money or real banking logic,
but they mimic the structure and flow of an online banking experience closely enough to serve the project’s goals.

The most visually prominent features are the animated cards, modal dialogs, and interactive tables. While these are not
strictly necessary for functionality, they help demonstrate how far HTML, CSS, and a small amount of JavaScript can go
when carefully combined with Django templates.
</details>

<details>
<summary>This short video goes through signing up, making an account and card. We create a transaction, send a few bucks
and checking a statement. We delete a card and log out... enjoy</summary>
<br>

[![Bankey Walktrhough](static/readme/yt%20vid%20template.gif)](https://youtu.be/JMLCL7Gjmak)
</details>

---

# User Authentication & Management

<details>
<summary>Authentication is handled using Django’s built-in tools, with a custom User model added early on to support a
date of birth field. This added some complexity but allowed tighter control over account generation and
future expansion ideas, such as identity-based account numbers.</summary>
<br>

Login, signup, and logout flows are simple by design. Feedback to the user is provided through message banners rather
than page redirects wherever possible, keeping the experience fluid and reducing friction. While security is
intentionally lightweight for a demo app, the structure mirrors real-world patterns closely.

![login.png](static/readme/login.png)

</details>

---

# Data Management

All models in the project are custom and interconnected: users own accounts, accounts own cards, and transactions
reference users and cards. Special care was taken to ensure that deleting a card does not destroy transaction history,
which is handled through nullable foreign keys and clear fallback states in the UI.

Balances are derived rather than blindly trusted, and account totals are recalculated from card balances to keep data
consistent, (see utils.py). While this is not a production-ready financial system, it demonstrates sound relational
thinking and
defensive data design.

---

# Deployment

<details>
<summary>Using the Code institute plan for the students, I deployed the project to Heroku. Thanks to their eco dynos We are able
to host for free. The server is asleep until requested, it might need a moment to warm up.</summary>
<br>

Deployment proved to be one of the most time-consuming parts of the project. Issues with environment variables, database
configuration, and settings mismatches caused delays that reshaped the original timeline. Eventually, the application
was successfully deployed after rebuilding the settings configuration and re-connecting dependencies from scratch.

The experience highlighted how fragile deployment pipelines can be when even small configuration details are overlooked.
It also reinforced the importance of testing deployment early, not just functionality.
</details>

---

# AI Implementation

AI was not directly embedded into the application’s runtime logic, but it played a role during development. It was used
primarily as a reasoning partner for debugging, refactoring, and validating architectural decisions rather than as a
code generator.

This approach helped clarify problems instead of obscuring them. Rather than relying on AI to “solve” the project, it
was used to ask better questions, especially when dealing with Django relationships, asynchronous behaviour, and UI edge
cases.

---

# Testing

## Desktop Lighthouse Reports

<details>
<summary></summary>
<br>

![desk light.png](static/readme/desk%20light.png)
![desk light 2.png](static/readme/desk%20light%202.png)

</details>


---

## Mobile Lighthouse Reports

<details>
<summary></summary>
<br>

![mobile light.png](static/readme/mobile%20light.png)
![mobile light 2.png](static/readme/mobile%20light%202.png)

</details>


---

## HTML Validation

<details>
<summary>
The html validation was taken from the page source of the heroku deployed site. Two main templates were used for the
readme, but all were tested.
Below find accounts and dashboard template links and screenshot of their validation.
</summary>
<br>

![html accounts](view-source:https://bankey-76bdd08d1577.herokuapp.com/account/)

![html 1.png](static/readme/html%201.png)

![html index](view-source:https://bankey-76bdd08d1577.herokuapp.com/)

![html 2.png](static/readme/html%202.png)
</details>


---

## CSS Validation

I was very happy to see no issues at all with the Cascading Style Sheets ! :)

![WC3 CSS validation.png](static/readme/WC3%20CSS%20validation.png)
ez w


---

## Python Validation

I ran all my created python files through a linter called ![Pyrfecter](erhttps://pyrfecter.com/format-python-code/), it
basically lints, formats, and modernizes python files to make the code positively perfect! No issues, only small
changes to lists that were one-liners.

---

## JavaScript Validation

During the validation of both script.js and statement.js, a number of warnings were raised by the linting tool. These
warnings mainly relate to ES6 syntax (e.g., const, let, arrow functions, and template literals).
No warnings described logical, functional, or structural issues in the code.
They were not errors, just compatibility reminders for environments older than 2015.

<details>
<summary>
The metrics for script.js are
</summary>
<br>

Metrics

- There is only one function in this file.
- It takes no arguments.
- This function contains 2 statements.
- Cyclomatic complexity number for this function is 1.

</details>

<details>
<summary>
The metrics for statement.js are
</summary>
<br>

Metrics

- There are 8 functions in this file.
- Function with the largest signature take 1 argument, while the median is 1.
- Largest function has 17 statements in it, while the median is 3.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.

- 18 warnings
- 14    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 15    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 19    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 20    'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 22    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 23    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 25    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 26    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 27    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 28    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 29    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 33    'template literal syntax' is only available in ES6 (use 'esversion: 6').
- 36    'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
- 37    'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
- 39    'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
- 40    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 49    'template literal syntax' is only available in ES6 (use 'esversion: 6').
- 72    'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

</details>

Given the time constraints and the stability of current functionality:
- All features were working as intended
- No runtime errors existed
- Refactoring ES6 -> older syntax risked introducing regressions
Therefore, addressing these warnings would have jeopardised the stability of the working project just before submission.

---

## Manual Testing

I sent links to tutors and CS graduate friends who had a good look and gave some tips... Overall there were no
issues with the user POV. All my colleagues queried enjoyed the experience and encountered no issues.

---

# Future Enhancements

I will try to add a function to print the statement as a PDF soon, and change the models of different accounts and 
card types to add interest rates, exchange fees and overdrafts.
Hopefully at one point this can serve as an inspiration for a real banking project. It would be interesting.

---

# Tech stack

For development:
- Pycharm
- Sublime text

<details>
<summary>Libs and Frameworks:</summary>
<br>

- asgiref==3.10.0
- bleach==6.3.0
- brotli==1.2.0
- certifi==2025.11.12
- cffi==2.0.0
- charset-normalizer==3.4.4
- cloudinary==1.36.0
- crispy-bootstrap5==0.7
- cryptography==46.0.3
- cssselect2==0.8.0
- defusedxml==0.7.1
- dj-database-url==3.0.1
- dj3-cloudinary-storage==0.0.6
- Django==4.2.26
- django-allauth==0.57.2
- django-crispy-forms==2.5
- django-summernote==0.8.20.0
- fonttools==4.61.0
- gunicorn==23.0.0
- idna==3.11
- oauthlib==3.3.1
- packaging==25.0
- pillow==12.0.0
- psycopg2-binary==2.9.11
- pycparser==2.23
- pydyf==0.12.1
- PyJWT==2.10.1
- pyphen==0.17.2
- python-dateutil==2.9.0.post0
- python3-openid==3.2.0
- requests==2.32.5
- requests-oauthlib==2.0.0
- six==1.17.0
- sqlparse==0.5.3
- tinycss2==1.5.1
- tinyhtml5==2.0.0
- typing_extensions==4.15.0
- tzdata==2025.2
- urllib3==1.26.20
- webencodings==0.5.1
- whitenoise==6.11.0
- zopfli==0.4.0

</details>

For ideation and design:
- Apple FreeForm for design
- Lucid Chart for ERD and some structured planning
- Past work also helped in layout design

Deployment and database:
- Neon DB through CI student logins for data storage
- Heroku with student eco dynos for hosting

---

# Credits

**Thank you, Dillon, Mark and Tom for bringing me a big step closer to your world of Software engineering, I learn too 
much!**

- Stock photos were taken from ![Pexels](https://www.pexels.com/), a web library that stores a wide variety of
  images that are free to use for my purposes.

- Most of my corrections were a 70/30 of ![django manpages](https://docs.djangoproject.com/en/6.0/) and "sanity checks"
  from chatGPT, mainly to corroborate something was likely to work or written with good practices,
  especially because my database was broken for the first week I was stuck with local hosting.

- Apart from the Django guides from ![NetNinja](https://www.youtube.com/@NetNinja/playlists) I 
did not use any specific resource to copy or source blocks of content, code or other part for this project.  
but a couple of videos about gradients and animating in css.  



_This project is dedicated to my unfinished degree in Economics and Finance in Portugal._
