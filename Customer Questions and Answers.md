### Question 1:
Hello,

I'm new to search engines, and there are a lot of concepts I'm not educated on. To make my onboarding smoother, it'd help if you could provide me with some definitions of the following concepts:
- Records
- Indexing

I'm also struggling with understanding what types of metrics would be useful to include in the "Custom Ranking." 

Cheers,
George

### Answer 1:
Hi George, 

Thank you for reaching out. 


A record is an object you add to an index and want to search for. It can contain any number of attributes.
For example if you have an index about smartphones. Then each phone would be a record in your index. 
Here is an example of a record, formatted in JSON:
```
{
  "name": "Iphone 6 64Gb",
  "brand": "Apple",
  "color": "Gold",
  "categories": ["smartphone", "phone", "electronics"],
  "price": 789
}
```
[Here](https://support.algolia.com/hc/en-us/articles/4406981906833-What-is-a-record) you can find the official documentation about records. 


Indexing is the process of making all of your records searchable. 
Algolia’s engine restructures your data in a special way in order to provide fast and relevant search. 
By indexing all your data in advance, you can type in a search request and get millions of records in milliseconds. 
[Here](https://www.algolia.com/doc/integration/magento-2/how-it-works/indexing/?client=php) you can find the official documentation about indexing. 


As of custom rankings, you can consider them as tie-breakers. Think of your smartphone index. Say you are now searching for "Iphone". 
There is obviously more than one Iphone in your index. So which one should be shown first? This is where custom ranking comes in. 
You could sort it by price or by business metrics such as sales. 
By default Algolia sorts it by tectual relevance, but you can change this to whatever metric you see fit. 
However, the custom ranking field type needs to be numerical or boolean.

I recommend you to watch the following video for more explanations: 
https://www.youtube.com/watch?v=yUx9OE9mgV4


Please let me know if any of this is not clear or if you need further information. 

Have a nice day! 
John

Johannes Meuthen  
Solutions Engineer  
Algolia  

### Question 2:
Hello,

Sorry to give you the kind of feedback that I know you do not want to hear, but I really hate the new dashboard design. 
Clearing and deleting indexes are now several clicks away. I am needing to use these features while iterating, so this is inconvenient.

Regards,
Matt

### Answer 2:
Hi Matt, 

Thank you for your feedback! 

We're constantly working on improvíng our user experience. I am sorry to hear that this was not the case for you. 

I discussed it with our developer team. With the latest update the goal was to avoid unwanted data loss of our clients.

May I propose an alternative, that could facilitate your way of working? 
By using our API you can delete and clear indexes within in one line of code.
Here is our documentation about it: 
[Clearing](https://www.algolia.com/doc/api-reference/api-methods/clear-objects/)
[Deleting](https://www.algolia.com/doc/api-reference/api-methods/delete-index/)
 
Please let me know if this is an acceptable solution for you. 


Have a nice day!   
John

Johannes Meuthen  
Solutions Engineer  
Algolia


### Question 3:
Hi,

I'm looking to integrate Algolia in my website. Will this be a lot of development work for me? What's the high level process look like?

Regards,  
Leo

### Answer 3:
Hi Leo, 

Thank you for reaching out today!

I happily walk you through the high level process and answer any further questions you may have. 

In most cases the development work is very little, especially when following the default settings. 
But each case is different and customization can add some additional work. 
Overall, we at Algolia try to facilite this process for our clients as much as possible. 
That is why we provide extensive documentation, pre-built tools and libraries to make your experience as smooth as possible. 

In terms of the high level process, you have to create an index on Algolia with your data in csv or json format.
After that you configure your searchable attributes and then you can already test your search in our dashboard. 
No coding is required for this. 

To assess your case in detail I propose a first meeting, so that you can explain your website and if you like I can give a demo. 


Would you have time next week?


Have a nice day!   
John  

Johannes Meuthen  
Solutions Engineer  
Algolia
