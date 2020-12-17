# <u> Walmart Reviews Analysis</u>

![walmart_logo](images/walmart_logo.png)


# Overview


## Business Motivation
2020 has been a hectic year but it has shown the importance of technology across all sectors. One of the major sectors being retail. 
"Save Money, Live Better" is Walmart's motto and philosophy and inorder for Walmart to live by their slogan, they need to be able to get the "best" items out for their customers based on the customer's want and need, both in store and online. 

Walmart is known for being the [King of retail stores](https://www.pioneeringminds.com/walmart/) but this is taking the physical stores into account. Since 2017, Walmart has made strong initiative to strength their online presence. Amidst the pandemic, Walmart saw a [74% increase in online sales in the first quarter](https://www.supermarketnews.com/retail-financial/walmart-sees-q1-us-comps-jump-10-online-sales-soar-74) as people worked from home and required goods to be delivered due to limited access to physical locations. 

However, currently, Walmart's online market promotes clothing products by price range and brand. Within these subcategory, itesm are displayed by "clerance", "best seller" and then the new and regular items. 

Clerance are the items on sale - "save money, live better" - this makes sense. The "new" and regualr items are the rest of the goods that Walmart carries - this also makes sense. 

However, most of the "best seller" items that I found, had very few people rateings on them and some did not even contain any text reviews. Walmart might have generated these "best seller" items from their sales data but for an online space, where customers cannot touch or feel the products, its really important to get feedback from other purchasers. So recommending products based on purely sales records does not help in the online space.

Now if Walmart were able to analyze customer's reviews and promote goods based on customer's "recommended" score and descriptive keywords, Walmart's marketing team would then be better able to market products that resonates with more customers.
   
## Goal
This analysis will look at Walmart clothing reviews to find key features that predict whether a customer will recommend an item or not. The features that guide the predictions can then used to guide Walmart's online and/or in-store marketing/product campaigns. This investigation will be conducted using [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) packages and libraries. 

## Data
Data is scraped directly from the Walmart webpage between November 27 to November 30 using Selenium and BeautifulSoup . The webpage urls and item links can be found in [item_links folder](https://github.com/dorjeys3/Walmart_proj/tree/master/data/item_links) and in the [scraper notebook](https://github.com/dorjeys3/Walmart_proj/tree/master/Walmart_scraper) as well. 

One of the obstacles of scraping Walmart was the Captcha that it would require you complete. This maybe due to the high number of requests received by Walmart server from the scraping. To get around this, you can either extend the ```time.sleep()``` method or use a VPN. I used a VPN and although successful, it still ran into captchas. 

Overall, I was able to obtain 1,225 observations (308 men's items, 471 women's items, 154 boys' items and 292 girls' items). After data cleaning and preprocessing, this number was 1,149 observations. These dataframes can be found in the ```item_review``` folder or [here](https://github.com/dorjeys3/Walmart_proj/tree/master/data/Item_review).   



## Methods
Since this dataframe consist of both continuous variables and text, the project was divided into three notebooks:

1. [Data cleaning](https://github.com/dorjeys3/Walmart_proj/blob/master/1_walmart_product_review_nlp.ipynb) for the continuous variables 
2. [Data preprocesing](https://github.com/dorjeys3/Walmart_proj/blob/master/2_walmart_product_review_nlp.ipynb) for the text
3. [Modeling](https://github.com/dorjeys3/Walmart_proj/blob/master/3_walmart_product_review_nlp.ipynb) with feature extractions

### Data Cleaning:

This notebook consist of removing all duplicates in the dataframe as well as cleaning the continuous variables. These variables contained unnecessary noise generated through scraping and unwanted text and symbols. There are four continuous variables:

* price
* overall rating score for the item
* the number of people who rated the item
* the recommended score. 

Additionally, this notebook contains some preliminary exploratory data analysis on the the continuous variables. 


### Data Preprocessing: 
Once the continuous variables were cleaned and saved as a new dataframe, it was imported to this notebook for preprocessing the text data. The main focus in this notebook was the reviews given by the customers who had purchased the items. All reviews were grabbed together for each item, therefore all reviews appear in one row. Thess reviews were then cleaned and processed using:

* Regular Expression (Regex)
* Tokenizer
* Removal of stopwords
* Lemmatization
* Latent Dirichlet Allocation (LDA) Topic Modeling

The clean dataframe was then pickled for modeling. Pickle method was used because saving the clean dataframe as ```.csv``` file was corrupting and introducing unwanted noise, requiring additional cleaning and defeating the purpose of notebook 1 and 2. 


### Modeling
Once the text and continuous variables were cleaned and processed. Train-Test split was initialized. TfidfVectorization was used after Train-Test split to prevent data leakage. CountVectorization was also used but TfidfVectorization produced better results.
The models used were:

* Logistic Regression
* Bernoulli Naive Bayes
* Support Vector Classifer - Linear
* Support Vector Classifer - Radial Basis Funciton
* Random Forest Classifier
* GridSearchCV with Random Forest Classifier 
* GridSearchCV with Logistic Regression

 

## Results
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

## Conclusion
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

## Next Steps
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

## For More Information
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
## Repository Structure

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
