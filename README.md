# Twitter Bot Plots

This repository contains python code to generate plots of Twitter followers similar to those in the New York Times article published January 27th 2018 with the title: [The Follower Factory](https://www.nytimes.com/interactive/2018/01/27/technology/social-media-bots.html). These types of plots can reveal Twitter users that have bought followers.

The plots are created by first retreiving the data via the Twitter API and then plotting the data using the Bokeh library.

# Using the code

In order to use this code the following steps must be performed:

* Clone this repository

```
git clone https:
```

* Install python prerequisites
```
pip install python-twitter
pip install bokeh
```

* Create a Twitter developer account by following the steps described in the [python-twitter documentation](http://python-twitter.readthedocs.io/en/latest/getting_started.html). Once you have created an account you should store your credentials in four files each containing just one line: `secrets/consumersecret`, `secrets/consumerkey`, `secrets/accesstoken` and `secrets/accesstokensecret`

* Retrieve the data:
```
python getTwitterData [twitteruser]
```
This command will create a file containing the join-dates of all followers of `[twitteruser]`. This may take a quite a while, because of limitations on the number of calls to the Twitter API. With a regular account you can make 15 API calls every 15 minutes, and with every calls it is possible to retrieve 200 followers. 

* Plot the data with Bokeh:
```
python scatterplot [twitteruser]
```
