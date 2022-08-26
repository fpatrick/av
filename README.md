# About(var)

Name meaning: About (Variable). The variable can be linux, gaming, news, etc.

**Live link: https://aboutv.herokuapp.com/**

#### A reddit inspired blog where users can share knowledge about linux, home lab, self-hosting, gaming and other technology related hobbies.
#### Open to anyone who wants to create an account, post freely and gain relevance by getting likes from other users.

![Screenshot 2022-08-26 at 16 31 48](https://user-images.githubusercontent.com/39106404/186940767-c76e2d14-32b7-4f2e-805a-f64d88fc5d87.png)

### What are this project goals?

* Provide a platform for tech-savvy people who would like to share their knowledge or learn something new.
* Be more simple and direct than reddit removing irrelevant posts and put the best posts on the spot.
* Be intuitive, direct to the point, simple, responsive and elegant.


## Development Choices

### User Stories and Agile

Agile methodology was applied. A small group of potential users was interview to understand and gather their needs. It was 
then analysed the viability for the project scope and made into a kanban board which [can be accessed clicking here.](https://github.com/users/fpatrick/projects/1/views/1 "About(var) Project board")

### Frameworks and Libraries

* Django for the batteries included nature, it delivered a simples but effective admin panel.
* Bootstrap for a speedy, beautiful and responsive design.
* Fontawesome to provide plenty of fancy icons.
* Summernote for a built-in editor for posts.
* Cloudinary to provide content such as images and static assets.
* Github as a git host, kanban board and user-stories.

### Colors

* Inspired by monokai color scheme. [Click here to access](https://monokai.pro "Monokai pro")

### Typography

* The main font for the project is Source Serif 4, which suits perfectly a blog style website.
* The font is provided by google fonts.
* Summernote also apply a user chosen font to posts.

## Main Features

### _Navbar_
![Screenshot 2022-08-26 at 16 37 05](https://user-images.githubusercontent.com/39106404/186941685-b0de692f-a79e-4496-a6cd-aa6cba3d7988.png)

* Home
* Contact
* Categories (dynamically generated)
* Search
* Sign-in/Sign-out
* Add or Edit Post or admin account

### _Home (Most liked posts)_
![Screenshot 2022-08-26 at 16 40 42](https://user-images.githubusercontent.com/39106404/186942361-27791137-3edb-4935-b70d-ee81a1d005f4.png)

* The posts with more likes stay on top

### _Newest Posts_
![Screenshot 2022-08-26 at 16 41 03](https://user-images.githubusercontent.com/39106404/186942430-3a44277a-0540-4851-81f4-457eab1207dc.png)

* New posts can be accessed by click on "Newest Posts" button

### _Categories_
![Screenshot 2022-08-26 at 16 41 26](https://user-images.githubusercontent.com/39106404/186942502-8dcd2e00-48e8-4388-b777-ca8dacd8f8bc.png)
* Posts can be accessed by its category

### _Search_
![Screenshot 2022-08-26 at 16 42 09](https://user-images.githubusercontent.com/39106404/186942644-a6cbf926-0dd3-4473-b46e-233c6088f941.png)
* Search posts based on its content

### _Sign-in, sign-out and sign-up_
![Screenshot 2022-08-26 at 16 42 36](https://user-images.githubusercontent.com/39106404/186942736-975b302e-8219-416c-9efa-1465b01b841c.png)
* Direct to the point form to enter, logout or create a account.

### _Contact_
![Screenshot 2022-08-26 at 16 42 58](https://user-images.githubusercontent.com/39106404/186942807-404d7c07-b3c0-46b9-9b4e-fbb23acd9bc7.png)
* Contact page with infos relevant to the website audience (technology savvy people), with links for where they can contact the website developer.

### _New post_
![Screenshot 2022-08-26 at 16 43 28](https://user-images.githubusercontent.com/39106404/186942923-39f97b0d-260a-45f4-b1bf-305eb1f5c0fd.png)
* Any user can register and make new post using summernote editor.

### _Change password or go back to blog_
![Screenshot 2022-08-26 at 16 43 47](https://user-images.githubusercontent.com/39106404/186942966-558b9af5-044b-4fab-bada-72c193539b77.png)
* Any user can easily change password, log-out or go back to blog.

### _Like Post_
![Screenshot 2022-08-26 at 16 58 13](https://user-images.githubusercontent.com/39106404/186945498-08a634ad-8e7d-46ed-aa99-a006f3447c5c.png)
* Any users can like posts and make them go up in the homepage

### _Comment_
![Screenshot 2022-08-26 at 16 58 43](https://user-images.githubusercontent.com/39106404/186945570-f4131d97-b92c-4e64-a3fb-2a7628b18af2.png)
* Any users can freely comment on any post


## Testing

### Validation

#### PIP8 Python Validator - http://pep8online.com
All python files edited for the project was tested with no warnings or errors.
It can be checked below:
<details>
<summary>admin.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186947855-a0060456-c30b-4e62-b77a-4e47cec52e2c.png" />
</details>

<details>
<summary>urls.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186947996-c207ba64-1d1e-4cd6-8c12-bbed99fb1016.png" />
</details>

<details>
<summary>views.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186948230-46fde90a-115a-4668-bb31-fc8518b5a0c6.png" />
</details>

<details>
<summary>models.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186948485-2c1b775b-6739-404e-9f14-70eb886c8a27.png" />
</details>

<details>
<summary>settings.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186948975-049e4c0b-e7af-42df-a3ac-882bce89d68c.png" />
</details>

<details>
<summary>forms.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186949159-4374898f-9f05-42af-a36c-49f440c5ba62.png" />
</details>

<details>
<summary>context_processors.py</summary>
<img src="https://user-images.githubusercontent.com/39106404/186949249-af9baa42-531b-4605-9cb2-de335e12dca2.png" />
</details>

#### Jigsaw W3C Validator - https://jigsaw.w3.org/css-validator
All CSS files edited for the project was tested with no warnings or errors.
It can be checked below:

<details>
<summary>style.css</summary>
<img src="https://user-images.githubusercontent.com/39106404/186950788-6cda187d-4bad-47c4-b243-bb51c75d2ecd.png" />
</details>

#### JSHint Validator - https://jshint.com
All javascript files edited for the project was tested with no errors. A few general browser warnings
It can be checked below:

<details>
<summary>script.js</summary>
<img src="https://user-images.githubusercontent.com/39106404/186951318-6af5aedf-1914-45d9-a47e-4f990274d5ff.png" />
</details>





<details>
<summary>admin.py</summary>
<img src="" />
</details>


