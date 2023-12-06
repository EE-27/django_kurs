# django_kurs
My Django kurs (skypro)
# Assignment
Coursework consists of two parts. The first part "Service Development" is opened to you in the middle of the course. If you have already completed this part, then immediately proceed to the second part - "Refinement of the service".

If you have not yet started working on a coursework project, then perform the first part, and then proceed to the second.

__Good luck!__

# Criteria for acceptance of the term paper
- The interface of the system contains the following screens: list of mailings, report of mailings made separately, creating a mailing, deleting a mailing, creating a user, deleting a user, editing a user.
- Realised all the required logic of the system.
- The interface is clear and meets the basic requirements of the system.
- All interfaces for changing and creating entities that are not related to the standard admin, implemented using Django-forms.
- All access rights settings were implemented correctly.
- At least two types of caching were used.
- The solution was posted on GitHub.

1. Develop a service
` Context To retain current customers, auxiliary or "warming" mailings are often used to inform and attract customers.`
Develop __a service for mailing list management, administration and statistics.__

# Task Description 
1. Implement a mailing list completion interface, that is, a CRUD mechanism for managing mailings. 
1. Implement a mailing list script that runs both from a line command and on a schedule. 
1. Add configuration settings to run the task periodically.

- Entities of the system
  - Client of the service:
    - contact email,
    - full name,
    - comment.
  - Mailing list (settings):
    - mailing time;
    - periodicity: once a day, once a week, once a month;
    - mailing status: completed, created, started.
  - Mailing message:
    - subject line,
    - body of the mail.
  - Mailing logs:
    - date and time of the last attempt;
    - status of the attempt;
    - mail server response, if any.

` Don't forget about the relationships between entities. You can extend models for entities in any number of fields or add auxiliary models. `

# System Logic
- After creating a new mailing, if the current time is greater than the start time and less than the end time, then all clients that are specified in the mailing settings should be selected from the directory and the mailing should be started for all these clients.
- If a mailing is created with a start time in the future, the sending should start automatically when this time comes without any additional actions from the system user.
- As messages are sent, statistics (see the description of the "message" and "logs" entity above) should be collected for each message for further reporting.
- An external service that receives messages may take a long time to process a request, respond with incorrect data, or not accept requests at all for some time. We need correct processing of such errors. Problems with the external service should not affect the stability of the developed mailing service.

## Recommendations

You can implement the interface using Bootstrap UI kit. 
To work with periodic tasks you can use either crontab-tasks in their pure form, or study the library: https://pypi.org/project/django-crontab/.

__Periodic tasks__ - tasks that are repeated with a certain frequency, which is set by a schedule.

‍__crontab__ is a classic daemon that is used to execute tasks periodically at a certain time. Regular actions are described by instructions placed in crontab files and special directories.

` The crontab service is not supported in Windows, but can be started via WSL. Therefore, if you work on this OS, solve the task of running periodic tasks using the apscheduler library: https://pypi.org/project/django-apscheduler/. `
Find detailed information on what crontab tasks are on your own.

2. Refine the __Context__ Service
   A mailing list management service is popular, but the MVP you are running no longer meets the needs of the business.
   Refine your web application. Specifically: separate access rights for different users and add a blog section to develop the popularity of the service on the web.

# Task Description
1. Extend the user model for mail registration as well as verification.
2. Add an interface for mailbox login, registration and verification.
3. Implement mailing list access restriction for different users.
4. Implement a manager interface.
5. Create a blog to promote the service.

Use the `AbstractUser model` for inheritance.

# Manager functionality 
- Can view any mailings.
- Can view the list of service users.
- Can block service users.
- Can disable mailings.
* Cannot edit mailings.
* Cannot manage the mailing list.
* Cannot modify mailings and messages.

# User functionality
All the functionality is duplicated from the first part of the coursework. But now we need to make sure that the user cannot accidentally change someone else's mailing list and can only work with his own client list and his own mailing list.

# Blog Promotion

Implement an application for blogging. You do not need to implement a separate interface, but you need to set up an administrative panel for the content manager.

Add the following fields to the blog entity:
- Title,
- article content,
- image,
- number of views,
- publication date.

# Home Page

Implement the home page in any format, but be sure to display the following information:
- number of newsletters total,
- number of active newsletters,
- number of unique customers for newsletters,
- 3 random blog articles.

# Caching

For the blog and homepage, select which data should be cached and how caching should be done.
