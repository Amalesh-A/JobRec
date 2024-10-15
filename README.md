# Job Recommendation Chatbot

This repository contains a Job Recommendation Chatbot built using Python and Gradio. The chatbot allows users to input job preferences such as job title, location, work model, urgency, and visa sponsorship requirements to receive job recommendations from a dataset of US software engineering jobs.

## Features

- **Job Filtering**: Filter jobs based on job title, location, remote work preference, urgency of hiring, and visa sponsorship requirements.
- **Pagination**: View job recommendations in a paginated format, with 5 results per page.
- **Interactive Interface**: A Gradio-powered web interface for easy user interaction.
- **Job Dataset**: Utilizes a dataset of US software engineering jobs (`us-software-engineer-jobs-updated-links-replaced.csv`).

## Requirements

- Python 3.7+
- Gradio 2.9.0+
- Pandas 1.2.0+

Install the necessary Python libraries using:

```bash
pip install gradio pandas

How to Use

    Run the chatbot: Launch the Gradio interface by running the job.py file.

    bash

    python job.py

    Input Your Job Preferences:
        Enter your desired job title (e.g., Engineer, Developer).
        Enter a location (e.g., Remote, California).
        Specify a work model (e.g., 100% Remote, Hybrid).
        Indicate whether the company is urgently hiring (Yes/No).
        Specify if you need visa sponsorship (Yes/No).

    Get Job Recommendations:
        Click "Get Recommendations" to view job recommendations based on the entered criteria.
        Use the "Next" button to paginate through the results.

Dataset

The chatbot uses a pre-loaded dataset of US software engineering jobs (us-software-engineer-jobs-updated-links-replaced.csv). The dataset includes columns such as:

    title: Job Title
    company: Company Name
    location: Job Location
    types: Job Type
    remote_work_model: Work Model (Remote, Hybrid, etc.)
    urgently_hiring: Indicates if the company is urgently hiring
    sponsored: Indicates if visa sponsorship is available
    link: Job application link

Future Improvements

    Integrating OpenAI's GPT model for more dynamic conversational responses.
    Enhancing the job filtering options to include more criteria.
    Expanding the dataset to cover jobs beyond software engineering.
