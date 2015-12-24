Parts Implemented by IŞIN KIRBAŞ
================================

Database Tables
---------------
.. figure:: static/member2db.png
      :scale: 100 %
      :alt: Database Tables

      Fig. 2.1: Entity Relationship Diagram of the User/Comment/Advertise tables.

3 tables are used to represent User/Comment/Advertise data.
User has no reference.
Comment references News.
Advertise has no reference.


User:
********

.. code-block:: plpgsql

   CREATE TABLE users (ID VARCHAR(100) NOT NULL,
   Firstname VARCHAR(40),
   Lastname VARCHAR(40),
   Age int,
   Gender VARCHAR(10),
   Email VARCHAR(100),
   AccountType VARCHAR(10),
   PRIMARY KEY (ID)) 

User table holds the information about user, it has no foreign keys.
First Name, Last Name, Age, Gender and Email are basic personal fields of User.
Account Type stands for type of User.



Comment:
*********

.. code-block:: plpgsql

   CREATE TABLE comments ( ID VARCHAR(100) NOT NULL,
   Username VARCHAR(40), 
   NewsID VARCHAR(100) REFERENCES news (ID),
   Title VARCHAR(100),
   Content VARCHAR,
   Date VARCHAR(20),
   PRIMARY KEY (ID))

Comment table holds the information about Comments, it has one foreign key.
News is which news comment belong to.
Username is the username of the person who wrote the comment.
Title is the title of comment.
Content is the essential part of the comment.
Date states the date that comment has made.

Advertise
*********

.. code-block:: plpgsql

      CREATE TABLE advertises (ID VARCHAR(100) NOT NULL, 
	ImageURL VARCHAR, 
	ExtURL VARCHAR, 
	SIZE VARCHAR(20),
	PRIMARY KEY (ID))

Advertise table holds the information about advertises, it has no foreign keys.
Image URL contains a URL to the picture of advertise.
External URL contains a URL to the website of the brand.
SIZE scales the image of advertise.


Class file of User:
**********************
.. code-block:: python

   class User:

   def __init__(self, id, firstname, lastname, age, gender, email,account_type):
        self.ID = id
        self.FirstName = firstname
        self.LastName = lastname
        self.Age = age
        self.Gender = gender
        self.Email = email
        self.AccountType = account_type

    def getID(self):
        return self.ID

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getAge(self):
        return self.Age

    def getGender(self):
        return self.Gender

    def getEmail(self):
        return self.Email

    def getAccountType(self):
        return self.AccountType 


Class file of Comment:
***********************
.. code-block:: python

    class Comment:

    def __init__(self, id, username, title, content, date):
        self.ID = id
        self.Username = username
        self.Title = title
        self.Content = content
        self.Date = date


    def getID(self):
        return self.ID

    def getUsername(self):
        return self.Username

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getDate(self):
        return self.Date 


Class file of Advertise:
**************************

.. code-block:: python

    class Advertise:

    def __init__(self, id, image_url, ext_url, size):
        self.ID = id
        self.ImageUrl = image_url
        self.ExtUrl = ext_url
        self.Size = size

    def getID(self):
        return self.ID

    def getImageUrl(self):
        return self.ImageUrl

    def getExtUrl(self):
        return self.ExtUrl

    def getSize(self):
        return self.Size 

User related part of server.py file:
***************************************

.. code-block:: python

    @app.route('/admin_panel/user', methods=['GET','POST'])
    def user():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _userList = dbmanager.getUsers(connection)
            return render_template('user.html', userList = _userList)

        if(request.form["action"] == "Add User"):
            return redirect(url_for('user'))

        if(request.form["action"] == "Delete"):
            return redirect(url_for('user'))

Comment related part of server.py file:
****************************************
.. code-block:: python

    @app.route('/admin_panel/comment', methods=['GET','POST'])
    def comment():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _commentList = dbmanager.getComments("null",connection)
            return render_template('comment.html', commentList = _commentList)

        if(request.form["action"] == "Add Comment"):
            dbmanager.addComment(request.form['comment_username'], request.form['comment_title'], request.form['comment_content'], request.form['comment_date'])
            return redirect(url_for('comment'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteComment(request.form['id'])
            return redirect(url_for('comment')) 

Advertise related part of server.py file:
*******************************************
.. code-block:: python

    @app.route('/admin_panel/advertise', methods=['GET','POST'])
    def advertise():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _advertiseList = dbmanager.getAdvertises(connection)
            return render_template('advertise.html', advertiseList = _advertiseList)

        if(request.form["action"] == "Add Advertise"):
            dbmanager.addAdvertise(request.form['advertise_imageurl'], request.form['advertise_exturl'], request.form['advertise_size'], connection)
            return redirect(url_for('advertise'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteAdvertise(request.form['id'], connection)
            return redirect(url_for('advertise'))

        return render_template('advertise.html') 


User related part of dbmanager.py file:
******************************************
.. code-block:: python

    def createUserTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (ID VARCHAR(100) NOT NULL,Firstname VARCHAR(40),Lastname VARCHAR(40),Age int,Gender VARCHAR(10),Email VARCHAR(100),AccountType VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

    def getUsers(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ")

    userList = []

    row = cursor.fetchone()
    while row:

       user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       userList.append(user)

       row = cursor.fetchone()

    return userList

    def checkUserLogin(username, password,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM userLogin WHERE userName = '%s' AND passWord = '%s'"%(username,password))

    result = cursor.fetchone()

    if result is None:
        return None

    cursor.execute("SELECT * FROM users WHERE id = '%s'"%(result[0]))

    row = cursor.fetchone()

    _user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

    _user.Username = result[1]

    return _user

    def addUser(firstname, lastname, age, gender, email,username,password,conn):

    try:

        cursor = conn.cursor()

        created_id = utils.generateID()

        cursor.execute("INSERT INTO users VALUES('%s','%s','%s','%s','%s','%s','%s')"%(created_id, firstname, lastname, age, gender, email, 'User'))

        cursor.execute("INSERT INTO userLogin VALUES('%s','%s','%s')"%(created_id,username,password))

        conn.commit()

        return 'OK'

    except Exception as e:
        print(str(e))
        return 'SameUsername'

    def deleteUser(id,conn):
 
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = '%s'"%(id))

    conn.commit()

Comment related part of dbmanager.py file:
*******************************************
.. code-block:: python

    def createCommentTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE comments (ID VARCHAR(100) NOT NULL, Username VARCHAR(40), NewsID VARCHAR(100) REFERENCES news (ID),Title VARCHAR(100),Content VARCHAR,Date VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

    def getComments(news_id, conn):

    cursor = conn.cursor()

    if(news_id != "null"):
        cursor.execute("SELECT * FROM comments WHERE newsID = '%s' "%(news_id))

    else:
        cursor.execute("SELECT * FROM comments")

    commentList = []

    row = cursor.fetchone()
    while row:

       _comment = Comment(row[0],row[1],row[3],row[4],row[5])

       commentList.append(_comment)

       row = cursor.fetchone()


    return commentList

    def addComment(username, newsid ,title, content, date, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO comments VALUES('%s','%s','%s','%s','%s','%s')"%(utils.generateID(), username, newsid, title, content, date))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

    def deleteComment(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM comments WHERE id = '%s'"%(id))

    conn.commit() 

Advertise related part of dbmanager.py file:
**********************************************
.. code-block:: python

    def createAdvertiseTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE advertises (ID VARCHAR(100) NOT NULL, ImageURL VARCHAR, ExtURL VARCHAR, SIZE VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

    def getAdvertises(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM advertises")

    advertiseList = []

    row = cursor.fetchone()
    while row:

       advertise = Advertise(row[0],row[1],row[2],row[3])

       advertiseList.append(advertise)

       row = cursor.fetchone()


    return advertiseList

    def addAdvertise(image_url, ext_url, size, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO advertises VALUES('%s','%s','%s','%s')"%(utils.generateID(), image_url, ext_url, size))

        conn.commit()



    except Exception as e:
        print(str(e))
        pass

    def deleteAdvertise(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM advertises WHERE id = '%s'"%(id))

    conn.commit()



