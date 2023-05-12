# Analysis of French Twitter Data
This was an early 2022 Project made during the latest French elections where the objective was to see the misinformation and real infromation going on Twitter/Facebook.

The ultimate objective was to create a method and dataset where you can train an AI on its data to give you a % of misinformation on specific topics. The ones that were choosen for this were the Ukraine War, the Vaccination campaign and comments about Macron (as they are the spiciest/most controversial subjects).

## The hurdles
The project was made in a pre-ChatGPT world. We couldnt access the AI and the closest thing we had was Word2Vec as a form of embedding (see how close the cleaned words of the tweet) would correlate to choosen words of misinformation. As a secondary test we would also use an NLP framework to test if the message is angry, happy or other feelings. As that type of misinformation was targeted to create a sort of anger/debate it was a good proxy to add to the cleaned words.

This project also lacked in that Facebook and Twitter both have extremely limited API's for official use. We had to circumvent the TOS and use Pupeeter/Selenium based solutions to extract information and meta-information from Facebook and Twitter.

Another hurdle imoosed is that we had different servers running Docker containers and we used the Hadoop Framework to distribute calculation, tried to use Kafka for distributed messaging as well as PySpark to treat the massive data (multiple CSVs of 20MiB minimum).
