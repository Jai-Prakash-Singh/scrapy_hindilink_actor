import MySQLdb

def main():
    
    # http://www.hindilinks4u.net/2011/07/zindagi-na-milegi-dobara-2011.html,Zindagi Na Milegi Dobara (2011),
    #dailymotion,Watch Part 1,http://www.filmshowonline.net/videos/84403/

    
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","hindilink_actor")
    cursor = db.cursor()
    sql = """create table if not exists ml_mn_typ_part_wl ( id int not null auto_increment, movielink varchar(255), movie varchar(100),\
          type varchar(50), part varchar(50), watchlink varchar(255), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key(id, watchlink));"""

    cursor.execute(sql)


    f  = open("page3_ml_mn_tp_prt_wt")
    for l in f:
        values = tuple(l.split(","))
        try:
	    sql = """insert into ml_mn_typ_part_wl (movielink, movie, type, part, watchlink) values ("%s", "%s", "%s", "%s", "%s")"""%(values)
            print sql
	    cursor.execute(sql)
	    db.commit()
        except:
            db.rollback()

    db.close()
    f.close()



if __name__=="__main__":
    main()

