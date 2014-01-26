import MySQLdb
import sys

def main():
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","hindilink_actor")
    cursor = db.cursor()
    
    sql = """create table  IF NOT EXISTS actor_actorlink_movie_movielink ( date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, actor varchar(255), actorlink varchar(255), movie varchar(255), movielink varchar(255));"""
    cursor.execute(sql)
    db.commit()

    f = open("pag2_actor_movie_mlink")
    f2 = open("pag2_movielink", "a+")

    for l in f:
        an_a_am_aml = tuple(l.split(","))
	print >>f2, str(an_a_am_aml[3]).strip()
        actor = str(an_a_am_aml[0]).strip().replace("+", ' ')
	actor_link =  str(an_a_am_aml[1]).strip()
	movie = str(an_a_am_aml[2]).strip()
	movie_link = str(an_a_am_aml[3]).strip()
	an_a_am_aml = (actor, actor_link, movie, movie_link)
 
	sql = """insert into actor_actorlink_movie_movielink (actor, actorlink, movie, movielink) values ("%s", "%s", "%s", "%s")"""%(an_a_am_aml)       
        print sql 
	#sys.exit()
	cursor.execute(sql)
	db.commit()

    f.close()
    f2.close()
    db.close()



if __name__=="__main__":
    main()

        

