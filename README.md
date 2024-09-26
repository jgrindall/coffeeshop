# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Backend

- Tested in Python 3.12

```bash
pip install -r requirements.txt
```


```bash
./run.sh
```

Hit the "/populate" route once to drop and re-populate the database


## Frontend

- Tested in node 16.x

```bash
sudo npm install -g @ionic/cli
```


```bash
npm i
```


> _note_: If you encounter issues with `node-sass`, ensure `sass` is installed instead:

```bash
npm uninstall node-sass
npm install node-sass@4.14.1
```

> _note_: If you encounter an error related to python2 while installing dependencies, you might need to install Python  Use the following command if necessary:
```bash
brew install python@2
```


```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```







