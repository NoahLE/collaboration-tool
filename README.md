# Project Collaboration Mockup

- [Project Collaboration Mockup](#project-collaboration-mockup)
  - [Installation](#installation)
  - [Pages](#pages)
  - [Sample Images](#sample-images)
    - [Login](#login)
    - [Dashboard](#dashboard)
    - [Notifications](#notifications)
    - [Chat - Single Person](#chat---single-person)
    - [Chatroom](#chatroom)
    - [Kanban](#kanban)
    - [Editing Kanban Card](#editing-kanban-card)
    - [All Kanban Issues](#all-kanban-issues)
    - [Wiki](#wiki)
    - [Calendar](#calendar)

## Installation

1. Set up virtualenv (this can be done when creating a new project if you're using Pycharm)
2. Install project libraries with `pip3 install -r requirements.txt`
3. Run migrations with `python manage.py migrate`
4. Run project with `python manage.py runserver`

## Running the project

All you need to do is run `python manage.py runserver` 

## Pages

| Page                   | URL                  | Balsamiq Name                                | Description                        |
| ---------------------- | -------------------- | -------------------------------------------- | ---------------------------------- |
| Login                  | /gui/                | Login screen                                 | The default landing and login page |
| Index                  | /gui/index           | Main app screen                              | The landing page after logging in  |
| Alerts                 | /gui/alerts          | Alert switcher                               | Shows the pending notifications    |
| Wiki Main              | /gui/wiki-main       | Different wikis                              | The main wiki landing page         |
| Kanban                 | /gui/kanban          | Kanban-UI                                    | Landing page                       |
| Kanban - Item selected | /gui/kanban/selected | Kanban-card-selected / Kanban-task-submitted | Item selected                      |
| Kanban - Editing item  | /gui/kanban/edit     | Kanban-card-selected / Kanban-task-submitted | Editing item                       |
| Profile - Public       | /gui/profile/public  | Profile - public                             | Public profile page                |
| Profile - Private      | /gui/profile/private | Profile - private                            | Private profile page               |
| Chat - 1-on-1          | /gui/chat/single     | Chat-open-1-on-1                             | Private individual chats           |
| Chat - Group           | /gui/chat/multiple   | Chat-open-rooms                              | Group chat rooms                   |
| Event calendar         | /gui/calendar        | Event calendar                               | Calendar                           |

## Sample Images

### Login
![login](/docs/login.png)

### Dashboard
![dashboard](/docs/dashboard.png)

### Notifications
![notifications](/docs/notifications.png)

### Chat - Single Person
![chat-single](/docs/chat-single.png)

### Chatroom
![chat-multiple](/docs/chat-multiple.png)

### Kanban
![kanban](/docs/kanban.png)

### Editing Kanban Card
![kanban-edit](/docs/kanban-edit.png)

### All Kanban Issues
![kanban-issues](/docs/kanban-issues.png)

### Wiki
![wiki](/docs/wiki.png)

### Calendar
![calendar](/docs/calendar.png)
