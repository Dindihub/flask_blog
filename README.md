# KELELE NEWS

## Built By Sandra

## Description
KELELE NEWS is a web application that displays a list of various news sources.Allows users to choose a News source,read articles from the source and get a brief of headlining news content from around the world. 

You can view the site at:[Heroku]()

## User Stories
As a user I would like to:
* See various News sources
* Select the ones they prefer
* See the top headline articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed in a list |
| Display tabs with news by category | **On Tab link click** | Clickable links to open news based on category |
| Display articles from a news source | **Click a news source** | Redirected to a page with articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image,description and publication date |
| To Read an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Dindihub/flask_blog.git
        $ cd flask-blog

## Running the Application
* Creating the virtual environment

        $ python3 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python
        $ source virtual/bin/activate

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-Bootstrap
        $ python3.8 -m pip install Flask-Script

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3  manage.py tests

## Technologies Used
* Python3.8
* Flask

## Known Bugs
No known bugs

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/flask_blog.git)**
