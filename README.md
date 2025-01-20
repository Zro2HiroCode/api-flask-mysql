MySQL Data CRUD API with Python and Flask

Created by Zro2HiroCode.

สวัสดีครับ! ยินดีต้อนรับสู่โครงการ MySQL Data CRUD API ของเรา ซึ่งใช้ Python และ Flask ในการสร้าง RESTful API สำหรับการทำงานกับฐานข้อมูล MySQL โครงการนี้เป็นคู่มือที่ครอบคลุมสำหรับการสร้าง API ที่สามารถจัดการข้อมูลได้อย่างมีประสิทธิภาพและปลอดภัย ทำให้เหมาะสมสำหรับแอปพลิเคชันต่างๆ ตั้งแต่เว็บแอปพลิเคชันง่ายๆ ไปจนถึงโครงการทางธุรกิจที่ซับซ้อน

โค้ดชุดนี้ถูกเก็บไว้สำหรับการทบทวนและการเรียนรู้ หวังว่าจะเป็นประโยชน์แก่ทุกคน ไม่ว่าจะเป็นผู้เริ่มต้นหรือผู้เชี่ยวชาญ ถ้ามีคำถามหรือต้องการความช่วยเหลือ กรุณาติดต่อผมที่ saengsaichaiyo@gmail.com

Features

Create: Add new records to the database.

Read: Retrieve existing records from the database.

Update: Modify existing records in the database.

Delete: Remove records from the database.

Authentication: Secure endpoints with user authentication.

Validation: Ensure data integrity with input validation.

Error Handling: Provide meaningful error messages for debugging and user feedback.

Technologies Used

Python: The programming language used for building the API.

Flask: A lightweight web framework for Python.

MySQL: A popular relational database management system.

SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.

Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs.

Flask-JWT-Extended: An extension for Flask that adds JSON Web Token (JWT) support for securing endpoints.

Getting Started

Clone the Repository:

git clone https://github.com/Zro2HiroCode/api-flask-mysql.git
cd api-flask-mysql

If you need to clone the repository, you can use the following link: https://github.com/Zro2HiroCode/api-flask-mysql

Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt

Configure the Database:

Create a MySQL database and user.

Update the database configuration in config.py.

Run the Application:

flask run

Access the API:

The API will be available at http://127.0.0.1:5000.

Use tools like Postman or cURL to interact with the API endpoints.

Endpoints

POST /api/items: Create a new item.

GET /api/items: Retrieve all items.

GET /api/items/<id>: Retrieve a specific item by ID.

PUT /api/items/<id>: Update a specific item by ID.

DELETE /api/items/<id>: Delete a specific item by ID.

Authentication

POST /api/auth/login: Log in and obtain a JWT token.

POST /api/auth/register: Register a new user.

Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Make your changes and commit them with descriptive messages.

Push your branch to your fork.

Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

For any questions or support, please contact saengsaichaiyo@gmail.com.