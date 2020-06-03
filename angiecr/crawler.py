import threading
import time
import requests

class Crawler:


    code = []
    turn = [0]
    code_lock = threading.Lock()

    def __init__(self):
        self.isFixed = False
        self.size = 4
        self.code = []
        self.result = []

        self.custom_set_path = None
        self.custom_dict_path = None
        self.dictionary = None
        self.url = None

        self.nthreads = 1

        self.final_set = []

        self.minus_selected = False
        self.minus = []

        self.mayus_selected = False
        self.mayus = []

        self.numbers_selected = False
        self.numbers = []

        self.special_selected = False
        self.special = []

        self.init_sets()

    def set_custom_set_path(self,p):
        self.custom_set_path = p

    def set_custom_dict_path(self,p):
        self.custom_dict_path = p

    def set_isFixed(self,f):
        self.isFixed = f

    def init_sets(self):
        for i in range(97,123):
            self.minus.append(chr(i))

        for j in range(65,91):
            self.mayus.append(chr(j))

        for k in range(48,58):
            self.numbers.append(chr(k))

        for n in range(33,48):
            self.special.append(chr(n))

    def set_url(self,u):
        self.url = u

    def set_nthreads(self,n):
        self.nthreads = n

    def set_size(self,s):
        self.size = s

    def select_sets(self,minus=False,mayus=False,numbers=False,special=False):
        self.minus_selected = minus
        self.mayus_selected = mayus
        self.numbers_selected = numbers
        self.special_selected = special

    def read_custom_set(self):
        f= open(self.custom_set_path,"r")
        st = f.read()

        st = st.replace('\n','') 
        a = st.split(',')


        positions = []
        for p,i in zip(range(len(a)),a):
            if i == '..':
                positions.append(p)
        for p in positions:
            a[p] = ','

        #para escribir una comma en el diccionario, usar ".."
        self.final_set = a

    def read_custom_dict(self):
        f= open(self.custom_dict_path,"r")
        st = f.read()
        a = st.split('\n')

        count = 0
        for p,i in zip(range(len(a)),a):
            if i == '':
                count += 1

        for p in range(count):
            a.remove('')

        self.dictionary = a

    def gen_one_combination(code_lock,result,final_set,size,url):

        while Crawler.code != -1:

            with Crawler.code_lock:

                final_string = "/"
                for c in Crawler.code:
                    final_string += final_set[c]

                print(final_string)
                Crawler.code.reverse()

                carry = 1
                for c in range(len(Crawler.code)):
                    Crawler.code[c] += carry
                    if Crawler.code[c] == len(final_set):
                        Crawler.code[c] = 0
                        carry = 1
                    else:
                        carry = 0

                Crawler.code.reverse()


                if carry == 1:
                    if len(Crawler.code) != size:
                        Crawler.code.insert(0,0)
                    else:
                        Crawler.code = -1

            r = requests.get(url + final_string)

            if r.status_code == 200 or r.status_code == 403:
                result.append(url+final_string)

    def request_from_dictionary(dictionary,result,url,turn,code_lock):
        if dictionary != None:
            while turn[0] < len(dictionary):
                with code_lock:
                
                    req = url + dictionary[turn[0]]
                    turn[0] += 1

                if req != None:
                    print("R: " + req)
                    r = requests.get(req)

                    if r.status_code == 200 or r.status_code == 403:
                        result.append(req)


    def begin_crawl(self,mode):

        if mode == 0:
            if self.custom_set_path != None:
                self.read_custom_set()
            else:
                if self.minus_selected:
                    self.final_set += self.minus

                if self.mayus_selected:
                    self.final_set += self.mayus

                if self.numbers_selected:
                    self.final_set += self.numbers

                if self.special_selected:
                    self.final_set += self.special

            if self.final_set != None:
                if self.isFixed:
                    for s in range(self.size):
                        Crawler.code.append(0)
                else:
                    Crawler.code.append(0)

            thread_list = []
            for i in range(self.nthreads):
                t = threading.Thread(target=Crawler.gen_one_combination,args=(self.code_lock,self.result,self.final_set,self.size,self.url,))
                t.start()
                thread_list.append(t)
                
                #prevención para que no omita crear hebras
                time.sleep(0.0001)

            for tt in thread_list:
                tt.join()

            
        elif mode == 1:
            if self.custom_dict_path != None:

                self.read_custom_dict()
                thread_list = []

                for i in range(self.nthreads):
                    t = threading.Thread(target=Crawler.request_from_dictionary,args=(self.dictionary,self.result,self.url,Crawler.turn,Crawler.code_lock))
                    t.start()
                    thread_list.append(t)
                
                    #prevención para que no omita crear hebras
                    time.sleep(0.0001)

                for tt in thread_list:
                    tt.join()

                print(str(self.result))


