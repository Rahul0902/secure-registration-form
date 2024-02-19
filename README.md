<h1>Building Secure Forms with Flask</h1>

<h2>Project Overview</h2>
<p>
    The Flask application developed implements a comprehensive set of security measures to mitigate risks such as SQL injection, Cross-Site Scripting (XSS), and ensure the integrity and security of user-submitted data. Developed using Flask, SQLAlchemy, and other libraries, the project focuses on delivering a secure user authentication system while adhering to best practices in web application security.
</p>

<h3>1.1 SQL Injection Prevention:</h3>
<p>In my Flask application, I prioritise secure database interaction by leveraging SQLAlchemy ORM methods. Within my models.py file, I define the 'User' class, outlining the structure of the 'User' table with attributes such as username, email, and password. Throughout authentication routes like 'login' and 'register', I rely on SQLAlchemy ORM methods to interact with the 'User' table, ensuring efficient and safe database operations.</p>

<p>By utilising SQLAlchemy ORM, parameterised queries are automatically generated, significantly reducing the risk of SQL injection vulnerabilities. This approach allows me to securely handle user input, thereby enhancing the overall security of my application. Additionally, I adhere to best practices by avoiding direct concatenation of user input into SQL strings.</p>

<p>Instead, I utilise ORM methods and query parameters to ensure the safe handling of input data, minimising security risks associated with direct SQL string concatenation. This meticulous approach contributes to a robust security framework, safeguarding the application against potential threats and vulnerabilities.</p>

![Screenshot 2024-02-19 at 12 56 09](https://github.com/Rahul0902/secure-registration-form/assets/44233038/8ee6ead9-1312-4f9f-a7fb-5171500f6155)

![Screenshot 2024-02-19 at 13 06 45](https://github.com/Rahul0902/secure-registration-form/assets/44233038/1026d159-ff50-4aaa-b24e-d668969406ce)

![Screenshot 2024-02-19 at 13 52 08](https://github.com/Rahul0902/secure-registration-form/assets/44233038/02686cb0-0d46-45fc-8a32-726a3572285d)


<h3>1.2 XSS Prevention:</h3>
<p>
    <strong>Rendering Display Messages Safely:</strong><br>
In my Flask application, I employ Jinja2 templating engine to display server-generated messages, known as flash messages, on HTML pages. Although these messages themselves may not directly contain user input, they are dynamically generated content that requires careful handling to prevent security risks. By using Jinja2 template expressions like `{{ message }}` within alert messages in login.html and register.html templates, I ensure that any potentially harmful characters in these messages are automatically escaped, making it safe to display them without compromising security.

![Screenshot 2024-02-19 at 13 24 23](https://github.com/Rahul0902/secure-registration-form/assets/44233038/40558eca-9e6e-4d2f-b810-df03c3f5290a)

</p>
<p>
    <strong>Markupsafe's escape Function:</strong><br>
    Markupsafe's escape function is utilised to escape user input obtained from registration form fields, treating it as plain text to reduce the risk of XSS vulnerabilities.
</p>

![Screenshot 2024-02-19 at 13 27 34](https://github.com/Rahul0902/secure-registration-form/assets/44233038/faea417c-e042-4140-8eb5-57b26bd8df92)

![Screenshot 2024-02-19 at 13 50 38](https://github.com/Rahul0902/secure-registration-form/assets/44233038/8dd6033a-68a8-45f6-93c9-39c16aea31d8)


<h3>1.3 Password Hashing and Salting:</h3>
<p>
    In my Flask application, I've implemented robust password security measures to safeguard user credentials. Firstly, passwords undergo hashing using the scrypt algorithm, renowned for its resistance to brute-force attacks. Additionally, each password is salted with a unique value per user, thwarting attackers from exploiting precomputed rainbow tables. This salting technique further fortifies the security of hashed passwords. To seamlessly incorporate these security features, I've leveraged SQLAlchemy integration, ensuring hashed passwords are securely stored and authenticated within the database schema. This comprehensive approach strengthens the protection of user accounts against unauthorized access and data breaches.
</p>

![Screenshot 2024-02-19 at 13 40 14](https://github.com/Rahul0902/secure-registration-form/assets/44233038/0d6508ed-a509-46ff-b342-b2f4c140c956)

<img width="1468" alt="Screenshot 2024-02-19 at 13 40 58" src="https://github.com/Rahul0902/secure-registration-form/assets/44233038/029ec6d8-eca5-4578-82a7-6f55f70828e6">


<h3>1.4 Input Validation with Regular Expressions and Error Handling - Including Password Security</h3>
<p>
    In my Flask application, I've employed regular expressions (regex) to validate user input effectively. Usernames must consist of alphanumeric characters and underscores only, with a length between 5 and 20 characters. Similarly, email addresses are validated to match the typical email format, while passwords are required to meet specific criteria such as containing digits, lowercase and uppercase letters, special characters, and a minimum length of 12 characters.
</p>
<p>
    These regex patterns are crucially applied within the registration route to validate user input before proceeding with the registration process. In addition to regex validation, conditional statements are utilised to perform error checking during both the login and registration processes. When a user submits the login or registration form, the server-side code checks the input against predefined conditions. For instance, if a username is already in use or the password does not meet the required criteria, corresponding error messages are generated and displayed to the user, guiding them to correct their input before proceeding.
</p>


![Screenshot 2024-02-19 at 13 48 49](https://github.com/Rahul0902/secure-registration-form/assets/44233038/2d2aafc5-5d07-4edf-95c2-7e37d0d601a1)

![Screenshot 2024-02-19 at 13 48 08](https://github.com/Rahul0902/secure-registration-form/assets/44233038/624f6c5f-5805-4335-bc6f-2f33d50d4904)

![Screenshot 2024-02-19 at 13 48 49](https://github.com/Rahul0902/secure-registration-form/assets/44233038/a965d2e2-8753-4a8c-bb96-8e7bd717ea3d)

<h3>1.5 Restricted Access to Index Page</h3>
<p>
    To ensure secure access to sensitive pages, such as the index page ('index.html'), a measure has been implemented in the views.py file. By using the login_required decorator from Flask-Login, only authenticated users are permitted to access the index page. This restriction is enforced by decorating the route handler function for the index page ('home') within the views.py file. Any attempt to access the index page by an unauthenticated user will result in a redirection to the login page, thereby enhancing the overall security of the application.
</p>

![Screenshot 2024-02-19 at 14 38 53](https://github.com/Rahul0902/secure-registration-form/assets/44233038/0bd88fe2-e28c-4797-ab88-408ae394ed11)

<h2>Conclusion</h2>

<p>Reflecting on the project, I'm pleased with the robust security measures implemented, including leveraging SQLAlchemy ORM for secure database interaction and Jinja2 templating for safe rendering. Password hashing with scrypt algorithm and salting further enhanced security, alongside input validation using regular expressions and error handling. Additionally, restricting access to sensitive pages to authenticated users added an extra layer of security.</p>

<p>Looking ahead, potential developments include implementing CAPTCHA for bot protection, Multi-Factor Authentication (MFA) for enhanced user authentication, and client-side validation to improve user experience. These enhancements would bolster security and user-friendliness, ensuring the project evolves to meet changing web application standards.</p>




