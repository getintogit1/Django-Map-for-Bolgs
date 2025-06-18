# Sights of Salzburg Website

## Description
This project is a Django-based website that utilizes HTML, CSS, JavaScript, Leaflet, and GeoJSON for mapping functionalities. It serves as a platform to showcase touristic attractions and blog fucntionalities for users. 

## Features
- Interactive mapping with Leaflet
- Integration of GeoJSON data
- Django-powered backend for dynamic content management
- Responsive frontend design using HTML and CSS
- Enhanced user experience with JavaScript functionalities

## Installation
1. Clone this repository to your local machine using:<br>
git clone "https://git.sbg.ac.at/s1086122/webproject_ss_24.git"

2. Navigate into the project directory:<br>
\path\to\your\dir>

3. Install the required dependencies:<br>
\path\to\your\dir> **pip install -r ./requirements.txt**

4. Apply migrations to set up the database:<br>
(make sure your manage.py file is inside this directory path)<br>
\path\to\your\dir> **python manage.py makemigrations** <br>
\path\to\your\dir> **python manage.py migrate**<br>
(you need to migrate everytime after you made changes to your database by making changes in django modely.py file)<br>


5. Start the development server:<br>
\path\to\your\dir> **python manage.py runserver**<br>


6. Access the website in your browser at `http://127.0.0.1:8000/`.

7.--> You wont see any Images at First, you need to visit admin site in step 8 and upload Description for in this case Attraction images etc. 

8. Access Django-Admin in your browser at `http://127.0.0.1:8000/admin/`

9. To use static files change your settings.py file accordingly and make sure you pointing to the right static dir

10. After you made your Static settings run : 
\path\to\your\dir> **py manage.py collectstatic**<br>


## Usage
- Upon accessing the website, explore the interactive map interface.<br>
- Use the provided functionalities to navigate through different attractions of Salzburg City.<br>
- Interact with other users by reading or posting blog articles.<br>

## Contributing

1. Fork the repository.<br>
2. Create a new branch (`git checkout -b feature/your-feature`).<br>
3. Make your changes.<br>
4. Commit your changes (`git commit -am 'Add new feature'`).<br>
5. Push to the branch (`git push origin feature/your-feature`).<br>
6. Create a new Pull Request.<br>

## License
[  GNU GENERAL PUBLIC LICENSE ](/webproject_ss_24/LiCENSE)

## Acknowledgements
- Leaflet: [Leaflet](https://leafletjs.com/)
- Django: [Django](https://www.djangoproject.com/)
- GeoJSON: [GeoJSON](https://geojson.org/)
- HTML: [HTML](https://html.com/)
- JavaScript: [JS](https://www.javascript.com/)



