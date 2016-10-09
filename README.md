# Wanderit (HackUPC Fall 2016 Project)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/367dbe254bf448b3be3b431917c92f5d)](https://www.codacy.com/app/crodriguezanton/wanderit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=crodriguezanton/wanderit&amp;utm_campaign=Badge_Grade) [![GitHub version](https://badge.fury.io/gh/crodriguezanton%2Fwanderit.svg)](https://badge.fury.io/gh/crodriguezanton%2Fwanderit) [![codecov](https://codecov.io/gh/crodriguezanton/wanderit/branch/master/graph/badge.svg)](https://codecov.io/gh/crodriguezanton/wanderit) [![Build Status](https://travis-ci.org/crodriguezanton/wanderit.svg?branch=master)](https://travis-ci.org/crodriguezanton/wanderit) [![Requirements Status](https://requires.io/github/crodriguezanton/wanderit/requirements.svg?branch=master)](https://requires.io/github/crodriguezanton/wanderit/requirements/?branch=master)

## Inspiration

It's been a long time that I wanted to do a cool project using the _skyscanner API_ and the idea of making this project came to me a couple weeks ago.

## What it does

[Wanderit](http://wanderit.com) is an automated travel search website that just with the list of places you've always wanted to go and your travel availability offers you the best travel combinations and recommends the best moment to book your ticket. To do so it searches in a 6-hour regular basis the possible combination for your flights and, after analyzing the historical data of prices as statistic parameters, it deduces the current trend of the prices and advises you about buying or not your tickets.

## How I built it

wanderit is built using Django as web framework and it is using the skyscanner Python API through a port to Django of this API that it's also built as part of this project ([GitHub django-skyscanner](https://github.com/crodriguezanton/django-skyscanner)).

## Challenges I ran into

* Using correctly the skyscanner API
* Optimizing the flight search cronjob in order not to overload the server
* Find the appropriate statistic parameters to analyze the prices trend
* Designing a good-looking front-end

## Accomplishments that I'm proud of

* wanderit is able to tell when flight prices will go up! (with a decent probability)
* wanderit optimizes the searches by searching the flights that are more relevant to more users and offers it to all of them with a single search
* Really nice looking front-end

## What I learned

* Using a API correctly
* Designing a front-end with css from the scratch.

## What's next for wanderit

I'd like to add some other functionalities to the website and allow everybody to use it!

## Challenges wanderit is elegible to

*  Best usage of Skyscanner API
* Best Use of AWS
* Best Domain Name from Domain.com (wanderit.com)
