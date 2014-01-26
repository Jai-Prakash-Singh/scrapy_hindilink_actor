import MySQLdb

def main():
    
    # http://www.hindilinks4u.net/2011/07/zindagi-na-milegi-dobara-2011.html,Zindagi Na Milegi Dobara (2011),
    #dailymotion,Watch Part 1,http://www.filmshowonline.net/videos/84403/

    
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","hindilink_actor")
    cursor = db.cursor()
    sql = """create table if not exists wl_em ( id int not null auto_increment,  watchlink varchar(255), embedlink varchar(255), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key(id, watchlink));"""

    cursor.execute(sql)


    f  = open("page4_watch_link__emlink")
    for l in f:
        values = tuple(l.split(","))
        try:
	    sql = """insert into wl_em (watchlink, embedlink) values ("%s", "%s")"""%(values)
            print sql
	    cursor.execute(sql)
	    db.commit()
        except:
            db.rollback()

    db.close()
    f.close()



if __name__=="__main__":
    main()

