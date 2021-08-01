
# Music Recommendation System

This is a basic machine learning project which asks the user to enter a song's name and when clicked on submit button, it shows the genre of the song that was provided by the user.

### Requirements

* Pandas
* numpy
* sklearn
* Django






## Installation

Install the above mentioned libraries by using the following:

```bash
  pip install pandas
```
```bash
  pip install numpy
```
```bash
  pip install scikit-learn
```
```bash
  pip install django
```

    
## Documentation

By using music recommender named Melodi in this project, user can predict the genre of the song that he/she wants to know. The model works on random forest classification.
The random forest is a classification algorithm consisting of many decisions trees. It uses bagging and feature randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.

### Dataset

Here we have used the track dataset in which we will be dropping few columns as they won't be necessary for model training. Columns that were dropped were:
 * id 
 * uri
 * artist
 * key
 * mode 
 * time_signature
 * duration_ms

### Genres predicted by the model

The genres predicted by this model are:
* Slow & Somber Acoustics
* Happy & Danceable Instrumentals
* Upbeat Songs With Cheerful Vocals
* Fast & Danceable
* Fast, Upbeat & Cheerful
* Rap
* Full of energy
* Happy & Upbeat Instrumentals

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/tanmoyee04/Machine-Learning-projects/tree/main/melodi
```

Go to the project directory

```bash
  cd project-directory
```

Start the server

```bash
  python manage.py runserver
```

  

  