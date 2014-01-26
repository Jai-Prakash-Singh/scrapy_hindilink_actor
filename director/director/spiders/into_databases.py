import MySQLdb





if __name__=="__main__":
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","hindilink_actor")
    cursor = db.cursor()

    sql = """create table IF NOT EXISTS  actor_n_actor_links (date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,actor_name varchar(100), actro_link varchar(255));"""

    cursor.execute(sql)

    f  = open("page1_actors_n_links")

    for act_name_link in f:
        act_name_link = tuple(act_name_link.split(","))
        sql = """ insert  into actor_n_actor_links (actor_name, actro_link)  values ("%s","%s")"""%(act_name_link)
        cursor.execute(sql)
        db.commit()

