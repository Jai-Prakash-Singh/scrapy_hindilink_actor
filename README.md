scrapy_hindilink_actor
======================

scrapy_hindilink_actor

running step 

scrapy runspider page1.py
	# it will get the  links for actor/actoress
        # and savein file page1_actors_n_links ( contains actor name and actor links)
	# Aamir Khan , http://www.hindilinks4u.net/?s=Aamir+Khan
	# """ insert  into actor_n_actor_links (actor_name, actro_link)  values ("%s","%s")""" 


scrapy runspider page2_actor_movie_mlink.py
	# it collects links from file page1_actors_n_links
	# Aamir Khan , http://www.hindilinks4u.net/?s=Aamir+Khan
	# goes to actor links 
	# like http://www.hindilinks4u.net/?s=Aamir+Khan
	# and save information in pag2_actor_movie_mlink ( actor name, actor links, movie name, movie link)
	# bhay+Deol, http://www.hindilinks4u.net/?s=Abhay+Deol, Raanjhanaa (2013), http://www.hindilinks4u.net/2013/07/raanjhanaa-2013.html


python pag2_into_databases.py
	# it collect  movie link from pag2_actor_movie_mlink
	# it save movie link to pag2_movielink
	# and inset into data base
	# like 
	#"""insert into actor_actorlink_movie_movielink\
        # (actor, actorlink, movie, movielink) values ("%s", "%s", "%s", "%s")"""% (actor, actor_link, movie, movie_link)


scrapy runspider page3_movie_vidio_link.py
	# it cxollect  links from file pag2_movielink ( movie link, movie name, type, part,  watch link)
	# http://www.hindilinks4u.net/2011/07/zindagi-na-milegi-dobara-2011.html,Zindagi Na Milegi Dobara (2011),dailymotion,Watch Part 1,http://www.filmshowonline.net/videos/84403/
	# it save watch link to page3_watch_link( watch link)


python page3_into_database.py
	# read file page3_ml_mn_tp_prt_wt 
        # insert data in databases
        # table ml_mn_typ_part_wl
	# insert into ml_mn_typ_part_wl (movielink, movie, type, part, watchlink) values ("%s", "%s", "%s", "%s", "%s")"""%(values)
        
scrapy runspider page4_link_to_link.py
	# open file "page4_watch_link__emlink"
	# extract watch links it avail 
	# appand it to list extract_links 
	# open file "page3_watch_link"
	# extract wll watch links to list avail_links
	# 1/10 part of avail links to list avail_links
	# start_links = set(avail_links) - set(extract_link)
	# use start links
	# open file "page4_watch_link__emlink"
	# insert [watch_links, embed_links]

scrapy runspider page42_link_to_link.py
scrapy runspider page43_link_to_link.py
scrapy runspider page44_link_to_link.py
scrapy runspider page45_link_to_link.py
scrapy runspider page46_link_to_link.py
scrapy runspider page47_link_to_link.py
scrapy runspider page48_link_to_link.py
scrapy runspider page49_link_to_link.py
scrapy runspider page410_link_to_link.py


python python  page4_into_database.py
	# open file "page4_watch_link__emlink"
	# collect [watch_links, embed_links]
	#  insert into databases wl_em
	# sql = """insert into wl_em (watchlink, embedlink) values ("%s", "%s")"""%(values)
        

    Status
    API
    Training
    Shop
    Blog
    About

    © 2014 GitHub, Inc.
    Terms
    Privacy
    Security
    Contact


