# Exponential Backoff System
## Introduction
This is a Django project template to be used for creating RESTful APIs  with support of exponential backoff for handling
intermittent failures and similar problems.

The template provides an auto retry mechanism for any task that uses the **ExponentialBackoffRetryTask** as the base 
class.

## Tech Stack
**Language**: Python<br />
**Framework**: Django<br />
**Task Worker**: Celery<br />
**Message Queue**: RabbitMQ<br />
**Database**: Postgres<br />
**Containarization**: Docker

## Steps to run the app

* Install Docker Engine
* Install Docker compose
* Clone the repo from github<br />
  `git clone https://github.com/saksham-segra/exponential-backoff-system.git`
  
* Create a `.env` file in the parent directory of the project `agri` wth all the necessary environment variables. A 
  `.sample-env` file for reference is provided in the repo.
* Build the Docker image<br />
    `docker-compose build`
* Run the docker containers<br />
    `docker-compose up`
  
## Steps to create auto retry tasks
* Create a callable task. Preferably, the task should be idempotent i.e. the function won’t cause unintended effects even
  if called multiple times with the same arguments.task.
  ```
  def sample_task(*args, **kwargs):
        # task body
        pass
  ```  
* Decorate the callable using celery provided helper decorator `shared_task` with the base class as 
  ***ExponentialBackoffRetryTask***
  ```
    from celery import shared_task
    from core.tasks import ExponentialBackoffRetryTask
  
    @shared_task(base=ExponentialBackoffRetryTask, 
                 name=<app_name>.<path_to_task>.<task_name>)
    def sample_task(*args, **kwargs):
        # task body
        pass
  
    ```

## Example
The template has a sample app called payments to showcase the working in case of a failing task. For simplicity purpose 
the sample task rasies an exception on being called.<br />

This task can be invoked by calling the following HTTP `POST` endpoint:<br />
    `localhost:8080/payments`
