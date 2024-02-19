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

![Screenshot 2024-02-19 at 13 09 16](https://github.com/Rahul0902/secure-registration-form/assets/44233038/855ff459-cfce-4d7e-a480-bd384b017af2)

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

![Screenshot 2024-02-19 at 13 28 35](https://github.com/Rahul0902/secure-registration-form/assets/44233038/3c58ddaa-091b-4f6e-85e6-a39bf74a8fce)


<h3>1.3 Password Hashing and Salting:</h3>
<p>
    <strong>Hashing with Scrypt:</strong><br>
    Passwords are hashed using the scrypt algorithm, which is a modern and secure key derivation function designed to be resistant to brute-force attacks.
</p>
<p>
    <strong>Salting:</strong><br>
    In addition to hashing, passwords are salted using a unique salt value for each user. Salting prevents attackers from using precomputed rainbow tables to crack hashed passwords more easily.
</p>
<p>
    <strong>SQLAlchemy Integration:</strong><br>
    SQLAlchemy is used to integrate password hashing and salting into the database schema, ensuring that hashed passwords are securely stored and compared during authentication.
</p>

<h3>Input Validation with Regular Expressions</h3>
<p>
    <strong>Regular Expressions (Regex):</strong><br>
    Client-side validation is implemented using regular expressions (<code>regex</code>) to ensure that the input provided by the user meets certain criteria before submitting the form data to the server.
</p>
