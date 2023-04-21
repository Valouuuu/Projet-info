from mysql.connector import connect
bdd = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")

def not_in_bdd(id):
    cursor = bdd.cursor()

    cursor.execute("SELECT com_user FROM Compte")
    result = cursor.fetchall()

    for i in result :
        if i == id :
            return True 
        else :
            return False


def create_acc(id, mdp, age):
    
    cursor = bdd.cursor()
    
    sql = "INSERT INTO Compte(com_user, com_mdp, com_age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id, mdp, age,))
    bdd.commit()

        