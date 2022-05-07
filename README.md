# Blog-with-Translator

Link to the deployment : https://dry-island-83570.herokuapp.com/


Inspiration

The inspiration for this project came from my one of my other passions : language learning. I studied and majored in foriegn lanuages during my time in university and I wanted a way to combine that passion with software development. Along with human languages, I wanted to expand my knowledge of programming lanuages that we only had a brief glance at during this last section of the bootcamp. One of those languages that seemed appealing was Python, Django specifically. So I decided to build a blog app with Django. The setup and design is so far fairly simple, mostly because of the time constraints of the deadline and reading through the documentation in order to get an idea of what needs to be mapped out before I can start writing in the template language. The functionality of this website is a blog about fashion with a focus on Japanese-Americana reproduction brands. This is also something that I would consider a hobby of mine so it was fairly easy to setup the data for these posts.

Functionality

  The way this app works is fairly simple : there is a Home page which lists all the available blog posts, along with the author and a brief sample of what the content of the blog is. When a user clicks on the 'Read More' button it will direct them to the page for the article. There is a top navbar for easy navigation to the Home page, About us Page, and an Author Log In which takes advantage of the built in Django Admin Interface. In the About Us it describes the purpose for this Style Blog and How one could become an author in order to contribute to the page. Right now it isn't taking any new writers but that functionality will come soon with an email form and sample file of the aspiring authors work. In side the Author Log In, the admin can view, edit, delete posts, create or delete users, or create new tables for possible new forms of data. There is also a guest account which can only edit, delete, and create posts under their account. 
  
  Future Plans
  
  I originally had Django-Google_translate working locally, which was great because it was such an easy setup : install, add to installed apps, then place in the html template file where you wanted the dropdown to appear and it would translate the entire page into any language google translate had available. However, during deployment to Heroku I kept encountering a strange error that I unfortunately could not figure out why it wasn't allowing me to use django-google-translate, so that is on the back burner for now. Another functionality is to add images for each blog post, and perhaps a background image for the home page to beautify this app. Being that it is a style-blog we should have some pictures to show the reasons why someone would spend the extra cash for an article of clothing. 
  
  
  Technology Used:
  - Django: https://www.djangoproject.com/
  - Django Sqlite for local database which then was converted to Heroku's Postgres
  - Django- google- translate : https://pypi.org/project/django-google-translate/ created by Samir Phuyal : https://www.samirphuyal.com.np/
  - Bootstrap: https://getbootstrap.com/
  - Deployed on Heroku 
