import subprocess

from Queue import Queue
from threading import Thread

num_fetch_threads = 2
enclosure_queue = Queue()


def worker(i,q):
    while True:
        avail_urls2 = q.get()
        subprocess.call(['scrapy', 'crawl',  'page4_link_to_linkii', '-a', 'aval_urls='+avail_urls2])
        q.task_done()

    

def main():
    f = open("page3_watch_link")
    avail_urls = f.read().strip().split("\n")
    val = len(avail_urls)/25
    threads = []

    for i in range(num_fetch_threads):
        t = Thread(target=worker, args=(i, enclosure_queue,))
        t.setDaemon(True)
        t.start()

    for links in range(25):
        if avail_urls[:val]:
            avail_urls2 =  ','.join(avail_urls[:val])    
        else:
            avail_urls2 =  ','.join(avail_urls[:])

        avail_urls = avail_urls[val:]
        enclosure_queue.put(avail_urls2)

   
    
    enclosure_queue.join()

    
if __name__=="__main__":
    main()
