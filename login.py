print("Hello ")

   my_database = mysql.connector.connect(
            host="localhost",
            user="flash",
            password="nod12345",
            database="dang"
        )
        mysql_db = my_database.cursor()
        query = f"insert into login(name, login, password, age) values" \
                f"('{self.name}', '{self.login}', '{self.password}', {self.age})"
        mysql_db.execute(query)
        my_database.commit()
